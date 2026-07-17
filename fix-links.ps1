$files = Get-ChildItem -Path .\*.html, .\*.js -File
foreach ($f in $files) {
    $content = Get-Content $f.FullName -Raw
    $new = $content -replace '/fek-flow/admin\.html', '/admin.html'
    $new = $new -replace '/fek-flow/projects\.html', '/projects.html'
    $new = $new -replace '/fek-flow/users\.html', '/users.html'
    $new = $new -replace '/fek-flow/dashboard\.html', '/dashboard.html'
    Set-Content -Path $f.FullName -Value $new -NoNewline
    Write-Host "Corrigido: $($f.Name)"
}