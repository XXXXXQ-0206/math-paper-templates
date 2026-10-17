# Replay every finite certificate and compare against the stored copies.
# Exits 0 only if every check passes and every stored certificate matches.
$ErrorActionPreference = 'Stop'

$root   = Split-Path -Parent $MyInvocation.MyCommand.Path
$out    = Join-Path $root '_verification-output'
$stored = Join-Path $root 'certificates'

if (Test-Path $out) { Remove-Item -Recurse -Force $out }
New-Item -ItemType Directory -Force -Path $out | Out-Null

# Assertions must be live: refuse to run under an optimizing interpreter.
if ($env:PYTHONOPTIMIZE) {
  Write-Host "PYTHONOPTIMIZE is set; unset it so that assertions run."
  exit 1
}

$failed = @()

Write-Host "=== checks/scalar_checks.py ==="
python (Join-Path $root 'checks/scalar_checks.py') $out
if ($LASTEXITCODE -ne 0) { $failed += 'scalar_checks.py' }

Write-Host "=== checks/matrix_checks.py ==="
python (Join-Path $root 'checks/matrix_checks.py') $out
if ($LASTEXITCODE -ne 0) { $failed += 'matrix_checks.py' }

Write-Host ""
Write-Host "=== comparing against stored certificates ==="

# Variable metadata that legitimately differs between runs.
$volatile = @('wall_seconds', 'seconds', 'python')

function Compare-Certificate($name) {
  $a = Join-Path $stored $name
  $b = Join-Path $out $name
  if (-not (Test-Path $a)) { Write-Host "MISSING stored $name"; return $false }
  if (-not (Test-Path $b)) { Write-Host "MISSING replay $name"; return $false }

  $ja = Get-Content $a -Raw | ConvertFrom-Json
  $jb = Get-Content $b -Raw | ConvertFrom-Json
  foreach ($k in $volatile) {
    if ($ja.PSObject.Properties.Name -contains $k) { $ja.PSObject.Properties.Remove($k) }
    if ($jb.PSObject.Properties.Name -contains $k) { $jb.PSObject.Properties.Remove($k) }
  }
  $sa = $ja | ConvertTo-Json -Depth 20 -Compress
  $sb = $jb | ConvertTo-Json -Depth 20 -Compress
  if ($sa -ne $sb) {
    Write-Host "DIFF $name"
    return $false
  }
  Write-Host "MATCH $name"
  return $true
}

foreach ($n in @('scalar-certificate.json', 'matrix-certificate.json')) {
  if (-not (Compare-Certificate $n)) { $failed += $n }
}

Write-Host ""
if ($failed.Count -gt 0) {
  Write-Host "FAILED: $($failed -join ', ')"
  exit 1
}
Write-Host "All certificates passed and match the stored copies."
