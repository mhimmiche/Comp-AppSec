import sys
import defusedxml.ElementTree as ET

def uploadAdmin(adminRoot):
	# For now it just prints the values, will add SQL query later.
	print "[*] Found an Administrator [*]"
	for child in adminRoot:
		print ">>>>> ", child.tag, "With value ", child.text
	print "[*] End of Administrator [*]"

def uploadDoctor(doctorRoot):
	# For now it just prints the values, will add SQL query later.
	print "[*] Found a Doctor [*]"
	for child in doctorRoot:
		print ">>>>> ", child.tag, "With value ", child.text
	print "[*] End of Doctor [*]"

def main():
	# Printing out the provided
	print "First Argument: ", sys.argv[1]
	# Determine what the XML root is
	e = ET.parse(sys.argv[1])
	# For testing purposes; returning the root.
	eRoot = e.getroot()
	eRootValue = eRoot.tag
	print "root for XML: ", eRootValue
	for child in eRoot:
		if child.tag == "SystemAdministratorUserProfile":			
			uploadAdmin(child)			
		elif child.tag == "DoctorUserProfile":			
			uploadDoctor(child)
			


if __name__ == "__main__":
    main()