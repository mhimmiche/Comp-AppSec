import sys
import getpass as gp
import defusedxml.ElementTree as ET

def checkIfCanAdd(vals):
	for k,v in vals.items():
		if vals[k] == False:
			return False
	return True

def SystemAdministratorUserProfile(adminRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False}
	for child in adminRoot:
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
		# Query
		# "INSERT INTO UserPro (username, role, permission, fName, lName, specInfo) 
		# VALUES (%s, %s, %s, %s, %s, "None")", (vals[Username], vals[Roles], vals[Permissions], vals[FirstName], vals[LastName],)
	else:
		print "Some values were left blank."


def DoctorUserProfile(doctorRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"RecoveryPhrase":False}
	for child in doctorRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
		# Query
		# "INSERT INTO UserPro (username, role, permission, fName, lName, specInfo) 
		# VALUES (%s, %s, %s, %s, %s, "None")", (vals[Username], vals[Roles], vals[Permissions], vals[FirstName], vals[LastName],)
	else:
		print "Some values were left blank."

def NurseUserProfile(nurseRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"AssociatedDoctors":False}
	for child in nurseRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

def MedicalAdministratorUserProfile(medicalAdminRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"AssociatedDoctors":False,"AssociatedNurses":False}
	for child in medicalAdminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

def InsuranceAdministratorUserProfile(insuranceAdmin):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"CompanyName":False,"CompanyAddress":False}
	for child in insuranceAdmin:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

def PatientUserProfile(patientUserRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"DOB":False,"SSN":False,"Address":False}	
	for child in patientUserRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

def DoctorExamRecord(examRecordRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False}	
	for child in examRecordRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

def DiagnosisRecord(diagnosisRecordRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"Doctor":False,"Diagnosis":False}
	for child in diagnosisRecordRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

def TestResultsRecord(testResultRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"Doctor":False,"Lab":False,"Notes":False}
	for child in testResultRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

def InsuranceClaimRecord(insuranceClaimRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"MedicalAdministrator":False,"Amount":False,"Status":False}
	for child in insuranceClaimRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

def RawRecord(rawRecordRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Description":False,"File":False}
	for child in rawRecordRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	canAdd = checkIfCanAdd(vals)
	if canAdd:
		print "woo!"
	else:
		print "Some values were left blank."

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
	if len(sys.argv < 1):
		print "[*] Arguments need to be provided"
	else:
		if sys.argv[1] == "loadData":
			e = ET.parse(sys.argv[2])
			# For testing purposes; returning the root.
			eRoot = e.getroot()
			eRootValue = eRoot.tag
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
						methodName(child)
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
