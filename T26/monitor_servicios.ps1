param(
[string]$ReportPath = "$PSScriptRoot\EXPORTSERVICE.csv"

)

Get-Service | Select-Object name, displayname, status, starttype | Export-Csv -Path $ReportPath -NoTypeInformation
