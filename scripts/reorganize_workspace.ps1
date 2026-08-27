$ErrorActionPreference = 'Stop'
$workspace = (Resolve-Path -LiteralPath (Split-Path -Parent $PSScriptRoot)).Path
if ($workspace -ne 'E:\image-course') { throw 'Unexpected workspace; review move targets' }
$moves = @()
1..10 | ForEach-Object {
    $name = 'Visual Course {0:D2}' -f $_
    $moves += @{ From = $name; To = "courses\$name" }
}
$moves += @{ From = 'project-architecture'; To = 'docs\case-studies\acme' }
$moves += @{ From = 'general-docs'; To = 'docs\general' }
$moves += @{ From = 'regen_volume8.py'; To = 'scripts\regen_volume8.py' }
$moves += @{ From = 'volume8_manual_data.json'; To = 'courses\Visual Course 08\volume8_manual_data.json' }
foreach ($move in $moves) {
    $source = (Resolve-Path -LiteralPath (Join-Path $workspace $move.From)).Path
    $target = [IO.Path]::GetFullPath((Join-Path $workspace $move.To))
    if (!$source.StartsWith($workspace + '\') -or !$target.StartsWith($workspace + '\')) { throw 'Path escapes workspace' }
    if (Test-Path -LiteralPath $target) { throw "Target exists: $target" }
}
$audit = @()
foreach ($move in $moves) {
    $source = (Resolve-Path -LiteralPath (Join-Path $workspace $move.From)).Path
    $target = [IO.Path]::GetFullPath((Join-Path $workspace $move.To))
    $item = Get-Item -LiteralPath $source
    $files = if ($item.PSIsContainer) { @(Get-ChildItem -LiteralPath $source -File -Recurse -Force) } else { @($item) }
    $before = @{}
    foreach ($file in $files) {
        $relative = if ($item.PSIsContainer) { $file.FullName.Substring($source.Length + 1) } else { '' }
        $before[$relative] = (Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash
    }
    $parent = Split-Path -Parent $target
    if (!(Test-Path -LiteralPath $parent)) { New-Item -ItemType Directory -Path $parent | Out-Null }
    Move-Item -LiteralPath $source -Destination $target
    foreach ($relative in $before.Keys) {
        $moved = if ($relative) { Join-Path $target $relative } else { $target }
        if ((Get-FileHash -LiteralPath $moved -Algorithm SHA256).Hash -ne $before[$relative]) { throw "Hash mismatch: $moved" }
    }
    $audit += [pscustomobject]@{ From=$move.From; To=$move.To; VerifiedFiles=$files.Count; Status='SHA256 identical immediately after move' }
}
$audit | Format-Table -AutoSize
