$drive=Get-PSDrive
$loc
foreach ($d in $drive) {
	if ($d.Free -gt 0) {
		echo "Looking in $d drive"
		$tmp= (gci -path $d.Root -filter "Project3" -Recurse -ErrorAction SilentlyContinue).FullName 
	}
	if ($tmp) {
		echo $tmp
	}
}


