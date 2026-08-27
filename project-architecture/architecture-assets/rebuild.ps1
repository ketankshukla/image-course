$ErrorActionPreference = 'Stop'
$projectRoot = Split-Path -Parent $PSScriptRoot
$pandocCommand = Get-Command pandoc -ErrorAction Stop
Push-Location -LiteralPath $projectRoot
try {
    & $pandocCommand.Source 'PROJECT-ARCHITECTURE.md' --from=gfm --to=html5 --standalone --embed-resources --toc --toc-depth=2 --template='architecture-assets/document.template.html' --css='architecture-assets/document.css' --output='PROJECT-ARCHITECTURE.html'
    if ($LASTEXITCODE -ne 0) { throw 'Document build failed.' }
} finally {
    Pop-Location
}
