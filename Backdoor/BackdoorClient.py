import sys
<<<<<<< HEAD
import getpass as gp
import defusedxml.ElementTree as ET

def uploadAdmin(adminRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False}
=======
import defusedxml.ElementTree as ET

def uploadAdmin(adminRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadDoctor(doctorRoot):
<<<<<<< HEAD
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"RecoveryPhrase":False}
=======
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"RecoveryPhrase":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadNurse(nurseRoot):
<<<<<<< HEAD
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"AssociatedDoctors":False}
=======
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"AssociatedDoctors":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadMedicalAdmin(medicalAdminRoot):
<<<<<<< HEAD
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"AssociatedDoctors":False,"AssociatedNurses":False}
=======
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"AssociatedDoctors":False,"AssociatedNurses":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadInsuranceAdmin(insuranceAdmin):
<<<<<<< HEAD
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"CompanyName":False,"CompanyAddress":False}
=======
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"CompanyName":False,"CompanyAddress":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadPatientUser(patientUserRoot):
<<<<<<< HEAD
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"DOB":False,"SSN":False,"Address":False}
=======
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"DOB":False,"SSN":False,"Address":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadDoctorExamRecord(examRecordRoot):
<<<<<<< HEAD
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False}
=======
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadDiagnosisRecord(diagnosisRecordRoot):
<<<<<<< HEAD
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"Doctor":False,"Diagnosis":False}
=======
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"Doctor":False,"Diagnosis":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadTestResultsRecord(testResultRoot):
<<<<<<< HEAD
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"Doctor":False,"Lab":False,"Notes":False}
=======
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"Doctor":False,"Lab":False,"Notes":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadInsuranceClaimRecord(insuranceClaimRoot):
<<<<<<< HEAD
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"MedicalAdministrator":False,"Amount":False,"Status":False}
=======
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"MedicalAdministrator":False,"Amount":False,"Status":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadrawRecord(rawRecordRoot):
<<<<<<< HEAD
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Description":False,"File":False}
=======
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Description":False,"File":False}	
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

<<<<<<< HEAD
def setITAdmin():
	username = input('Please enter a username: ')
	password = gp.getpass('Please enter a new password: ')
	pw_confirm = gp.getpass('Please confirm your password: ')
	firstName = input('First name: ')
	lastName = input('LastName: ')
	if password != pw_confirm:
		print "Password did not match, exiting program."
		exit(0)
	else:
		print "Woo!"


def main():
=======
def main():
	# Printing out the provided
	print "First Argument: ", sys.argv[1]
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
	# Determine what the XML root is
	if len(sys.argv < 1):
		print "[*] Arguments need to be provided"
	else:
<<<<<<< HEAD
		if sys.argv[1] == "loadData":
=======
		if sys.argv[1] == "loadData":			
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
			e = ET.parse(sys.argv[2])
			# For testing purposes; returning the root.
			eRoot = e.getroot()
			eRootValue = eRoot.tag
<<<<<<< HEAD
			if eRootValue == "DBFile":
				for child in eRoot:
					#TODO: Change funtion names to tag names
					methodName = child.tag
					possibleMethods = globals().copy()
					possibleMethods.update(locals())
					rightMethod = possibleMethods.get(methodName)
					if not rightMethod:
						print "Wrong tag provided: ", methodName
					else:
						methodName()
			else:
				print("[*] Wrong XML file provided.")
				exit(0)
		elif sys.argv[1] == "setITAdmin":
			setITAdmin()
		else:
			print "Wrong option specified."
			exit(0)

if __name__ == "__main__":
    main()
=======
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
>>>>>>> c399cde5e4d1befadf5bcfb22ded0b1bf1c1def3
