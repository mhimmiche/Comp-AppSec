$drive=Get-PSDrive
$loc
foreach ($d in $drive) {
	if ($d.Free -gt 0) {
		echo "Looking in $d drive"
		$tmp= (gci -path $d.Root -filter "Python27" -Recurse -ErrorAction SilentlyContinue).FullName 
	}
	if ($tmp) {
		$loc = $tmp
		echo "Found it in $tmp, stopping the search"
		break
	}
}
echo $loc
echo "[*] Updating the PATH variable [*]"
[Environment]::SetEnvironmentVariable("Path", $env:Path + ";" + $loc + ";" + $loc + "\Scripts", [EnvironmentVariableTarget]::Machine)
echo "[*] Done with the update - Initiating Pip installation[*]"
$curr=$pwd
cd $loc
$pipInstall=curl https://bootstrap.pypa.io/get-pip.py
$pipInstall.Content | .\python.exe
cd $curr
echo "[*] Done with setting everything up. Please close this Powershell window and open a new one. That should work! [*]"