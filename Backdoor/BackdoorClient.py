import sys
import defusedxml.ElementTree as ET

def uploadAdmin(adminRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadDoctor(doctorRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"RecoveryPhrase":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadNurse(nurseRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"AssociatedDoctors":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadMedicalAdmin(medicalAdminRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"PracticeName":False,"PracticeAddress":False,"AssociatedDoctors":False,"AssociatedNurses":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadInsuranceAdmin(insuranceAdmin):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"CompanyName":False,"CompanyAddress":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadPatientUser(patientUserRoot):
	vals = {"Username":False,"Roles":False,"Permissions":False,"FirstName":False,"LastName":False,"DOB":False,"SSN":False,"Address":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadDoctorExamRecord(examRecordRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadDiagnosisRecord(diagnosisRecordRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"Doctor":False,"Diagnosis":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadTestResultsRecord(testResultRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"Doctor":False,"Lab":False,"Notes":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadInsuranceClaimRecord(insuranceClaimRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Date":False,"MedicalAdministrator":False,"Amount":False,"Status":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

def uploadrawRecord(rawRecordRoot):
	vals = {"RecordID":False,"RecordType":False,"RecordDate":False,"Owner":False,"Patient":False,"EditPermissions":False,"ViewPermissions":False,"Description":False,"File":False}	
	for child in adminRoot:
		#print ">>>>> ", child.tag, "With value ", child.text
		for k,v in vals.items():
			if child.tag == k:
				vals[k] = child.text
	for k,v in vals.items():
		print k, v

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