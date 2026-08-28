param([string]$Root = (Split-Path $PSScriptRoot -Parent))
$ErrorActionPreference = 'Stop'
Add-Type -AssemblyName System.Speech
$source = Join-Path $Root 'docs/presentations/course-01/lesson-01/slides.json'
$scratch = Join-Path $Root '.slide-build/lesson-01'
$output = Join-Path $Root 'public/presentations'
$lesson = Get-Content -LiteralPath $source -Raw | ConvertFrom-Json
$synth = New-Object System.Speech.Synthesis.SpeechSynthesizer
$synth.SelectVoice('Microsoft Zira Desktop')
$synth.Rate = -1
$synth.Volume = 100
$concat = [System.Collections.Generic.List[string]]::new()
$chapters = [System.Collections.Generic.List[object]]::new()
$offset = 0.0
try {
  for ($i=0; $i -lt $lesson.slides.Count; $i++) {
    $number = '{0:D2}' -f ($i+1)
    $wav = Join-Path $scratch "voice-$number.wav"
    $segment = Join-Path $scratch "segment-$number.mp4"
    $slide = Join-Path $scratch "final-slide-$number.png"
    if (!(Test-Path -LiteralPath $slide)) { throw "Missing rendered slide: $slide" }
    $spoken = $lesson.slides[$i].narration -replace '\bMCP\b','M C P' -replace '\bA2A\b','A to A' -replace '\bAPI\b','A P I'
    $synth.SetOutputToWaveFile($wav)
    $synth.Speak($spoken)
    $synth.SetOutputToNull()
    $audioDuration = [double](& ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 $wav)
    $duration = $audioDuration + 1.5
    if ($i -eq 13) { $duration += 8 }
    & ffmpeg -hide_banner -loglevel error -y -loop 1 -framerate 10 -i $slide -i $wav -af 'apad,loudnorm=I=-18:TP=-2:LRA=7' -t $duration.ToString('F3',[cultureinfo]::InvariantCulture) -c:v libx264 -preset ultrafast -tune stillimage -crf 23 -pix_fmt yuv420p -c:a aac -b:a 128k -ar 48000 -movflags +faststart $segment
    if ($LASTEXITCODE -ne 0) { throw "Encoding failed at slide $number" }
    $concat.Add("file '$($segment.Replace('\','/'))'")
    $chapters.Add([pscustomobject]@{ slide=$i+1; title=$lesson.slides[$i].title; start=[math]::Round($offset,3); duration=[math]::Round($duration,3) })
    $offset += $duration
    Write-Output "Rendered slide $number ($([math]::Round($duration)) seconds)"
  }
} finally { $synth.Dispose() }
$list = Join-Path $scratch 'segments.txt'
[IO.File]::WriteAllLines($list,$concat,[Text.UTF8Encoding]::new($false))
$target = Join-Path $output 'course-01-lesson-01.mp4'
& ffmpeg -hide_banner -loglevel error -y -f concat -safe 0 -i $list -c copy -movflags +faststart $target
if ($LASTEXITCODE -ne 0) { throw 'Final video assembly failed' }
$timing = @{ voice='Microsoft Zira Desktop'; type='Local synthetic narration'; chapters=$chapters; durationSeconds=$offset } | ConvertTo-Json -Depth 5
[IO.File]::WriteAllText((Join-Path $output 'course-01-lesson-01-timing.json'),$timing,[Text.UTF8Encoding]::new($false))
Write-Output "Created $target ($([math]::Round($offset)) seconds)"
