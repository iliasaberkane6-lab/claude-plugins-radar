# Local refresh for Claude Plugins Radar (Windows / PowerShell)
# Usage:
#   ./scripts/refresh.ps1              # live refresh (uses GH_TOKEN if set)
#   ./scripts/refresh.ps1 -Offline     # no network, registry values only
#   ./scripts/refresh.ps1 -Token ghp_xxx

param(
    [switch]$Offline,
    [string]$Token
)

$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
Set-Location $root

if ($Token) { $env:GH_TOKEN = $Token }

$cmd = @("refresh", "--registry", "data/entries.yml", "--readme", "README.md", "--json", "awesome.json")
if ($Offline) { $cmd += "--offline" }

python -m awesome_guard @cmd
