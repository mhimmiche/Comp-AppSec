import sys
import defusedxml.ElementTree as ET

def uploadAdmin(adminRoot):
	for child in adminRoot:
		print child.tag, "With value ", child.text

def main():
	# Printing out the provided
	print "First Argument: ", sys.argv[1]
	# Determine what the XML root is
	e = ET.parse(sys.argv[1])
	# For testing purposes; returning the root.
	eRoot = e.getroot()
	eRootValue = eRoot.tag
	print "root for XML: ", eRootValue
	if eRootValue == "SystemAdministratorUserProfile":
		uploadAdmin(eRoot)


if __name__ == "__main__":
    main()