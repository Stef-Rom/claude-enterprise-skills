$ErrorActionPreference = "Stop"

$SourceDir = Resolve-Path (Join-Path $PSScriptRoot "..")
$TargetDir = if ($env:CLAUDE_SKILLS_DIR) { $env:CLAUDE_SKILLS_DIR } else { Join-Path $env:USERPROFILE ".claude\skills" }

New-Item -ItemType Directory -Force $TargetDir | Out-Null

Get-ChildItem -Path (Join-Path $SourceDir "skills") -Directory | ForEach-Object {
    Get-ChildItem -Path $_.FullName -Directory | ForEach-Object {
        $Name = $_.Name
        $Dest = Join-Path $TargetDir $Name
        Write-Host "Installing $Name -> $Dest"
        if (Test-Path $Dest) { Remove-Item -Recurse -Force $Dest }
        Copy-Item -Recurse $_.FullName $Dest
    }
}

Write-Host "Done. Restart Claude Code or open a new session."
