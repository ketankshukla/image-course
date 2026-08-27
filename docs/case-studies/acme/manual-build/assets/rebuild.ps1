$ErrorActionPreference = 'Stop'
$lessonRoot = Split-Path -Parent $PSScriptRoot
$pandoc = 'C:\Users\ketan\AppData\Local\Pandoc\pandoc.exe'
Push-Location -LiteralPath $lessonRoot
try {
    foreach ($lesson in Get-ChildItem -File -Filter '*.md') {
        if ($lesson.BaseName -notmatch '^\d\d-') { continue }
        & $pandoc $lesson.Name --from=gfm --to=html5 --standalone --embed-resources --toc --toc-depth=2 --template=assets/template.html --css=../architecture-assets/document.css --metadata "title=$($lesson.BaseName) - Manual Build Workbook" --output="$($lesson.BaseName).html"
        if ($LASTEXITCODE -ne 0) { throw "Failed to build $($lesson.Name)" }
    }
} finally { Pop-Location }
