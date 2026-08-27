$ErrorActionPreference = 'Stop'
$guideRoot = Split-Path -Parent $PSScriptRoot
$pandoc = 'C:\Users\ketan\AppData\Local\Pandoc\pandoc.exe'
Push-Location -LiteralPath $guideRoot
try {
    & $pandoc THE-WHOLE-PROJECT-IN-PLAIN-ENGLISH.md --from=gfm --to=html5 --standalone --embed-resources --toc --toc-depth=2 --template=companion-architecture-assets/document.template.html --css=architecture-assets/document.css --metadata 'title=The Whole Project in Plain English' --metadata 'edition=Beginner Guide' --metadata 'diagramcount=Two' --output=THE-WHOLE-PROJECT-IN-PLAIN-ENGLISH.html
    if ($LASTEXITCODE -ne 0) { throw 'Guide conversion failed' }
} finally { Pop-Location }
