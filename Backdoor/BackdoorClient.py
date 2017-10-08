import sys
import defusedxml.ElementTree as ET

def uploadAdmin(adminRoot):
	print "[*] Found an Administrator"
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v
	print "[*] End of Administrator"

def uploadDoctor(doctorRoot):
	print "[*] Found a Doctor"
	for child in doctorRoot:
		print ">>>>> ", child.tag, "With value ", child.text
	print "[*] End of Doctor"



def main():
	# Printing out the provided
	print "First Argument: ", sys.argv[1]
	# Determine what the XML root is
	e = ET.parse(sys.argv[1])
	# For testing purposes; returning the root.
	eRoot = e.getroot()
	eRootValue = eRoot.tag
	print "root for XML: ", eRootValue
	if eRootValue == "DBFile":
		for child in eRoot:
			if child.tag == "SystemAdministratorUserProfile":			
				uploadAdmin(child)			
			#elif child.tag == "DoctorUserProfile":			
				#uploadDoctor(child)
	else:
		print("[*] Wrong XML file provided.")
		exit(0)




if __name__ == "__main__":
    main()