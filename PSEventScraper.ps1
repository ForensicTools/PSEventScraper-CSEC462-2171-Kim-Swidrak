<#
.Synopsis
   Exports items from Windows Event Logs that are forensically interesting.
.DESCRIPTION
   TBD
.EXAMPLE
   Get-ForensicEvents
.EXAMPLE
   Get-ForensicEvents
#>
function Get-ForensicEvents
{
    [CmdletBinding()]
    [Alias()]
    [OutputType([int])]
    Param
    (
        <# Param1 help description
        [Parameter(Mandatory=$true,
                   ValueFromPipelineByPropertyName=$true,
                   Position=0)]
        $Param1,

        # Param2 help description
        [int]
        $Param2 #>
    )

    Begin
    {
    }
    Process
    {
    }
    End
    {
    }
}