$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$pandoc = 'C:\Users\ketan\AppData\Local\Pandoc\pandoc.exe'
Push-Location $projectRoot
try {
    foreach ($edition in @('HYBRID', 'TYPESCRIPT')) {
        & $pandoc "$edition-ARCHITECTURE.md" --from=gfm --to=html5 --standalone --embed-resources --toc --toc-depth=2 --template=companion-architecture-assets/document.template.html --css=architecture-assets/document.css --metadata "title=Acme Agent Platform - $edition Architecture" --metadata "edition=$edition" --output="$edition-ARCHITECTURE.html"
        if ($LASTEXITCODE -ne 0) { throw "Document rendering failed: $edition" }
    }
} finally {
    Pop-Location
}
