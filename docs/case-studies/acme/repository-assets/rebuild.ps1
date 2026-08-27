$ErrorActionPreference = 'Stop'
$documentRoot = Split-Path -Parent $PSScriptRoot
$pandoc = 'C:\Users\ketan\AppData\Local\Pandoc\pandoc.exe'
Push-Location -LiteralPath $documentRoot
try {
    & $pandoc REPOSITORIES-AND-DEPLOYMENT.md --from=gfm --to=html5 --standalone --embed-resources --toc --toc-depth=2 --template=companion-architecture-assets/document.template.html --css=architecture-assets/document.css --metadata 'title=Where the Projects Live - Repositories and Deployment' --metadata 'edition=Repository & Deployment' --metadata 'diagramcount=Two' --output=REPOSITORIES-AND-DEPLOYMENT.html
    if ($LASTEXITCODE -ne 0) { throw 'Document conversion failed' }
} finally { Pop-Location }
