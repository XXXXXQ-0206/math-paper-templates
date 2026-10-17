# Build every manuscript in this family.
# Each manuscript is independent; failures are reported but do not stop
# the remaining builds.
$ErrorActionPreference = 'Continue'
$root = Split-Path -Parent $MyInvocation.MyCommand.Path
$failed = @()

$targets = @(
  (Join-Path $root 'principal'),
  (Join-Path $root 'companions/companion-a'),
  (Join-Path $root 'companions/companion-b')
)

foreach ($t in $targets) {
  if (-not (Test-Path (Join-Path $t 'main.tex'))) {
    Write-Host "skip (no main.tex): $t"
    continue
  }
  Write-Host "=== building $t ==="
  Push-Location $t
  try {
    latexmk -pdf -interaction=nonstopmode main.tex | Out-Null
    if (Test-Path 'main.pdf') {
      Write-Host "OK   $t"
    } else {
      Write-Host "FAIL $t"
      $failed += $t
    }
  } catch {
    Write-Host "FAIL $t : $_"
    $failed += $t
  } finally {
    Pop-Location
  }
}

if ($failed.Count -gt 0) {
  Write-Host ""
  Write-Host "Failed: $($failed -join ', ')"
  exit 1
}
Write-Host ""
Write-Host "All manuscripts built."
