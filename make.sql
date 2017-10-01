/*DROP TABLE RolePermis cascade;
DROP TABLE DocSpecInfo cascade;
DROP TABLE NurSpecInfo cascade;
DROP TABLE MedAdminSpecInfo cascade;
DROP TABLE InsurAdminSpecInfo cascade;
DROP TABLE PatientSpecInfo cascade;
DROP TABLE DoctorExamRecord cascade;
DROP TABLE TestResults cascade;
DROP TABLE InsuranceClaim cascade;
DROP TABLE PatientDocCorr cascade;
DROP TABLE RawRec cascade;
DROP TABLE Note cascade;
DROP TABLE UserPro cascade;
DROP TABLE Record cascade;
DROP TABLE Role cascade;
DROP TABLE Permission cascade;*/

DROP DATABASE SMIRK;
commit;

CREATE DATABASE SMIRK;
commit;
USE SMIRK;



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

CREATE TABLE RolePermis
(
role VARCHAR(30)
, defaultPer VARCHAR(30)
, CONSTRAINT role_con UNIQUE (role)
, CONSTRAINT role_FK FOREIGN KEY (role) REFERENCES SMIRK.Role (role)
);



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


CREATE TABLE UserPro
(
username VARCHAR(20) 
, role  VARCHAR(20)
, permission VARCHAR(20)
, fName VARCHAR(20)
, lName VARCHAR(20)
, specInfo VARCHAR(30)
, CONSTRAINT username_PK PRIMARY KEY(username)
, CONSTRAINT username_con UNIQUE (username)
, CONSTRAINT permission_FK FOREIGN KEY (permission) REFERENCES SMIRK.Permission (permission)
);

CREATE TABLE Record
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

);


CREATE TABLE DocSpecInfo
(
praName VARCHAR(20)
, praAddress VARCHAR(20)
, recPhrase VARCHAR(20)
);

CREATE TABLE NurSpecInfo
(
praName VARCHAR(20)
, praAddress VARCHAR(20)
, associatedDoc VARCHAR(20)
);

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
, SSN VARCHAR(11)
, address VARCHAR(20)
);

CREATE TABLE Note
(
  DateofNote Date
, contents VARCHAR(50)
, CONSTRAINT content_unique UNIQUE(contents, DateofNote)
);

CREATE TABLE DoctorExamRecord
(
  DateOfDia DATE
, Doctor VARCHAR(20)
, Notes VARCHAR(20)
, CONSTRAINT EXAMnote_FK FOREIGN KEY (Notes) REFERENCES SMIRK.Note (contents)
);

CREATE TABLE TestResults
(
  DATEOfTest Date
, Doctor VARCHAR(20)
, Lab VARCHAR(20)
, Notes VARCHAR(20)
, CONSTRAINT TESTnote_FK FOREIGN KEY (Notes) REFERENCES SMIRK.Note (contents)
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
, File INT
);

commit;