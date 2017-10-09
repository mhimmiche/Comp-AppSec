DROP DATABASE SMIRK;
commit;

CREATE DATABASE SMIRK;
commit;
USE SMIRK;

CREATE TABLE UserSpecInfo
(
  praName VARCHAR(20)
, praAddress VARCHAR(20)
, recPhrase VARCHAR(20)
, associatedDoc VARCHAR(20)
, associatedNur VARCHAR(20)
, companyName VARCHAR(20)
, companyAddress VARCHAR(20)
, DOB DATE
, SSN VARCHAR(11)
, address VARCHAR(20)
);

CREATE TABLE Role 
(
role VARCHAR(30)
, description VARCHAR(70)
, CONSTRAINT role_unique UNIQUE (role)
);



/*INSERT INTO Role VALUES ("System Administrator", "Highest default permissions. Administers the SMIRK system.");
INSERT INTO Role VALUES ("Doctor", "A medical doctor");
INSERT INTO Role VALUES ("Nurse", "A medical nurse");
INSERT INTO Role VALUES ("Medical Administrator", "Administers information for doctors and nurses. Primary tasks include interfacing with Insurance Administrators.");
INSERT INTO Role VALUES ("Insurance Administrator", "Insurance company representative.");
INSERT INTO Role VALUES ("Patient", "Medical patient");*/

CREATE TABLE Permission
(
permission VARCHAR(20)
, description VARCHAR(99)
, CONSTRAINT permission_con UNIQUE (permission)
);

/*INSERT INTO Permission VALUES ("Add Patient","Ability to add a patient user profile to the system.");
INSERT INTO Permission VALUES ("Edit Patient","Ability to edit an existing patient user profile information.");
INSERT INTO Permission VALUES ("Add Doctor","Ability to add a doctor user profile to the system.");
INSERT INTO Permission VALUES ("Edit Doctor","Ability to edit an existing doctor user profile information.");
INSERT INTO Permission VALUES ("Add Medical Administrator", "Ability to add a medical administrator user profile to the system.");
INSERT INTO Permission VALUES ("Edit Medical Administrator","Ability to edit an existing medical administrator user profile information.");
INSERT INTO Permission VALUES ("Add Insurance Administrator","Ability to add an insurance administrator user profile to the system.");
INSERT INTO Permission VALUES ("Edit Insurance Administrator", "Ability to edit an existing insurance administrator user profile information.");
INSERT INTO Permission VALUES ("Add Nurse", "Ability to add a nurse user profile to the system.");
INSERT INTO Permission VALUES ("Edit Nurse", "Ability to edit an existing nurse user profile information.");
INSERT INTO Permission VALUES ("Add System Administrator", "Ability to add a system administrator user profile to the system.");
INSERT INTO Permission VALUES ("Edit System Administrator", "Ability to edit an existing system administrator user profile information.");
INSERT INTO Permission VALUES ("Remove User Profile","Ability to remove an existing user profile.");
INSERT INTO Permission VALUES ("Assign Permissions","Ability to assign permissions to user profiles.");
INSERT INTO Permission VALUES ("Edit Record Access","Ability to edit record View Permissions also Edit Permissions lists fields.");
INSERT INTO Permission VALUES ("View PII","Ability to view personally identifiable information (PII) held in the system.");*/


/*CREATE TABLE RolePermis
(
role VARCHAR(30)
, defaultPer VARCHAR(30)
, CONSTRAINT role_con UNIQUE (role)
, CONSTRAINT role_FK FOREIGN KEY (role) REFERENCES SMIRK.Role (role)
, CONSTRAINT defaultPer_FK FOREIGN KEY (defaultPer) REFERENCES SMIRK.Permission (permission)
);*/



/*INSERT INTO RolePermis Values ("System Administrator", "Add Patient");
INSERT INTO RolePermis Values ("System Administrator", "Edit Patient");
INSERT INTO RolePermis Values ("System Administrator", "Add Doctor");
INSERT INTO RolePermis Values ("System Administrator","Edit Doctor");
INSERT INTO RolePermis Values ("System Administrator", "Add Medical Administrator");
INSERT INTO RolePermis Values ("System Administrator", "Edit Medical Administrator");
INSERT INTO RolePermis Values ("System Administrator", "Add Insurance Administrator");
INSERT INTO RolePermis Values ("System Administrator", "Edit Insurance Administrator");
INSERT INTO RolePermis Values ("System Administrator", "Add Nurse");
INSERT INTO RolePermis Values ("System Administrator", "Edit Nurse");
INSERT INTO RolePermis Values ("System Administrator", "Add System Administrator");
INSERT INTO RolePermis Values ("System Administrator", "Edit System Administrator");
INSERT INTO RolePermis Values ("System Administrator", "Remove User Profile");
INSERT INTO RolePermis Values ("System Administrator", "Assign Permissions");
INSERT INTO RolePermis Values ("System Administrator", "Assign Permissions");
INSERT INTO RolePermis Values ("Doctor", "Add Patient");
INSERT INTO RolePermis Values ("Doctor", "Edit Patient");
INSERT INTO RolePermis Values ("Doctor", "Add Medical Administrator");
INSERT INTO RolePermis Values ("Doctor", "Edit Medical Administrator");
INSERT INTO RolePermis Values ("Doctor", "Add Nurse");
INSERT INTO RolePermis Values ("Doctor", "Edit Nurse");
INSERT INTO RolePermis Values ("Nurse", "Add Patient");
INSERT INTO RolePermis Values ("Nurse", "Edit Patient");
INSERT INTO RolePermis Values ("Medical Administrator", "Add Patient");
INSERT INTO RolePermis Values ("Medical Administrator", "Edit Patient");
INSERT INTO RolePermis Values ("Medical Administrator", "View PII");
INSERT INTO RolePermis Values ("Insurance Administrator", "View PII");*/


CREATE TABLE UserPro
(
username VARCHAR(20) 
, role  VARCHAR(20)
, permission VARCHAR(20)
, fName VARCHAR(20)
, lName VARCHAR(20)
, specInfo VARCHAR(30)
, CONSTRAINT username_PK PRIMARY KEY(username)
, CONSTRAINT username_UQ UNIQUE (username)
, CONSTRAINT permission_FK FOREIGN KEY (permission) REFERENCES SMIRK.Permission (permission)
, CONSTRAINT specInfo_check_con CHECK(specInfo = "DocSpecInfo" OR specInfo = "NurSpecInfo" OR specInfo = "PatientSpecInfo" OR specInfo = "MedAdminSpecInfo" OR specInfo = "InsurAdminSpecInfo")
#, CONSTRAINT UProle_FK FOREIGN KEY (role) REFERENCES SMIRK.Role (role)
);
/*
CREATE TABLE DocSpecInfo
(
praName VARCHAR(20)
, praAddress VARCHAR(20)
, recPhrase VARCHAR(20)
);
*/
/*
create or replace trigger timeoverlaptrig
  before insert on reservations
  for each row
declare
  v_startdatetime date;
  v_enddatetime date;
begin
  select startdatetime into v_startdatetime from reservations where (:new.startdatetime between startdatetime and enddatetime) and bedid=:new.bedid;
  select enddatetime into v_enddatetime from reservations where (:new.enddatetime between startdatetime and enddatetime) and bedid=:new.bedid;
  if v_startdatetime is not null or v_enddatetime is not null THEN RAISE_APPLICATION_ERROR(-20002, 'Time overlap');
  END IF;
END;
/
commit;
*/

/*create or replace trigger assdoctrig 
	before insert on NurSpecInfo
	for each row
declare
	v_docUname varchar(20);
BEGIN
	select Username into v_docUname from UserPro where role='Doctor' AND (:new.Username=docUser);
#		return 'True'
#	select startdatetime into v_startdatetime from reservations where (:new.startdatetime between startdatetime and enddatetime) and bedid=:new.bedid;
	if v_docUname is null then RAISE_APPLICATION_ERROR(-20002, 'Error Adding Doctor');
	END
	*/

/*
Create SQL security invoker view assDocQuery as
	SELECT username from UserPro where role = 'Doctor';

CREATE TABLE NurSpecInfo
(
praName VARCHAR(20)
, praAddress VARCHAR(20)
, associatedDoc VARCHAR(20)
#, CONSTRAINT ass_doc_ck CHECK (associatedDoc IN (SELECT username from UserPro where role = 'Doctor'))
#, CONSTRAINT ass_doc_ck CHECK (associatedDoc in assDocQuery)
#, CONSTRAINT ass_doc_FK FOREIGN KEY (associatedDoc) REFERENCES SMIRK.UserPro(username)
);

#INSERT INTO NurSpecInfo VALUES ("DocApt Inc.", "123 Fake Lane", "anolen3");

CREATE TABLE MedAdminSpecInfo
(
praName VARCHAR(20)
, praAddress VARCHAR(20)
, associatedDoc VARCHAR(20)
, associatedNur VARCHAR(20)
);

CREATE TABLE InsurAdminSpecInfo
(
  companyName VARCHAR(20)
, companyAddress VARCHAR(20)
);

CREATE TABLE PatientSpecInfo
(
  DOB DATE
, SSN VARCHAR(9)
, address VARCHAR(20)
);
*/


/*CREATE TABLE Record
(
  recordID INT
, recordType VARCHAR(30)
, recordDate DATE
, owner VARCHAR(20)
, patient VARCHAR(20)
, editPermissions VARCHAR(20)
, viewPermissions VARCHAR(20)
, recordTypeSpec VARCHAR(20)
, CONSTRAINT record_unique UNIQUE (recordID)
, CONSTRAINT owner_valid_FK FOREIGN KEY (owner) REFERENCES SMIRK.UserPro (username)
, CONSTRAINT type_check_con CHECK(recordType = "DoctorExamRecord" OR recordType = "TestResults" OR recordType = "Diagnosis" OR recordType = "InsuranceClaim" OR recordType = "PatientDocCorr" OR recordType = "RawRec")
);
*/

CREATE TABLE RecordInfo
(
  RecordID INT #change name?; unique identifier for the user
, RecordDate Date #DoctorExam, Diagnosis, TestResult, InsuranceClaim
, DoctorUname VARCHAR(20) #DoctorExam, Diagnosis, TestResult, PatientDocCor
, Notes VARCHAR(100) #DoctorExam, TestResults, PatientDocCor
, Diagnosis VARCHAR(20) #Diagnosis
, Lab VARCHAR(20) #TestResults
, MedAdmin VARCHAR(20) DEFAULT NULL #InsuranceClaim; a username; nullable?
, Amount FLOAT #InsuranceClaim
, Status VARCHAR(20) #InsuranceClaim
, Description VARCHAR(100) #RawRecord
, File BINARY #RawRecord
, CONSTRAINT recordID_UQ UNIQUE(RecordID)
, CONSTRAINT DoctorUname_FK FOREIGN KEY (DoctorUname) REFERENCES SMIRK.UserPro(username)
, CONSTRAINT status_ck CHECK(Status='Filed' OR Status='Examining' OR Status='Rejected' OR Status='Accepted' OR Status='Paid')
, CONSTRAINT MedAdmin_FK FOREIGN KEY (MedAdmin) REFERENCES SMIRK.UserPro(username)
);

CREATE TABLE Note
(
  DateofNote Date
, contents VARCHAR(50)
, CONSTRAINT content_unique UNIQUE(contents, DateofNote)
);

/* CREATE TABLE DoctorExamRecord
(
  DateOfDiag DATE
, Doctor VARCHAR(20)
, Notes VARCHAR(20)
, CONSTRAINT EXAMnote_FK FOREIGN KEY (Notes) REFERENCES SMIRK.Note (contents)
);

CREATE TABLE TestResults
(
  DateOfTest Date
, Doctor VARCHAR(20)
, Lab VARCHAR(20)
, Notes VARCHAR(20)
, CONSTRAINT TESTnote_FK FOREIGN KEY (Notes) REFERENCES SMIRK.Note (contents)
);

CREATE TABLE Diagnosis
(
  DateOfTest Date
, Doctor VARCHAR(20)
, Diagnosis VARCHAR(100)
);

CREATE TABLE InsuranceClaim
(
  DateOfClaim DATE
, MedAdmin VARCHAR(20)
, Amount INT
, Status VARCHAR(20)
);

CREATE TABLE PatientDocCorr
(
  Doctor VARCHAR(20)
, Notes VARCHAR(20)
, CONSTRAINT PATnote_FK FOREIGN KEY (Notes) REFERENCES SMIRK.Note (contents)
);

CREATE TABLE RawRec
(
  Description VARCHAR(99)
, File BINARY(99)
);

CREATE TABLE UserPass
(
  Username VARCHAR(20)
, Password VARCHAR(120)
#, CONSTRAINT username_exists_FK FOREIGN KEY (Username) REFERENCES SMIRK.UserPro (username)
);*/

#DELIMITER //
/*CREATE TRIGGER addToUserPass
AFTER INSERT ON SMIRK.UserPro
FOR EACH ROW
	INSERT INTO UserPass VALUES (New.Username, "p@ssw0rd");
*/
#INSERT INTO UserPro VALUES ("anolen3", "Nurse", "Add Patient", "Andrew", "Nolen", "DocSpecInfo");
commit;