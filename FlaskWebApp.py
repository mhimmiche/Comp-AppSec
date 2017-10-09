# -*- coding: utf-8 -*-

from flask import (abort, flash, Flask, g,
    redirect, render_template, request, session, url_for)

from flask_principal import (ActionNeed, AnonymousIdentity,
    Identity, identity_changed, identity_loaded, Principal, 
	Permission, RoleNeed)
from flask.ext.bcrypt import Bcrypt

app = Flask(__name__)
bcrypt = Bcrypt(app)

app.config.update(
    DEBUG=True,
    SECRET_KEY='secret_xxx')


principals = Principal(app, skip_static=True)

# Needs
be_admin = RoleNeed('admin')
be_doctor = RoleNeed('doctor')
be_nurse = RoleNeed('nurse')
be_medAd = RoleNeed('medAdmin')
be_insAd = RoleNeed('insAdmin')
be_patient = RoleNeed('patient')
to_sign_in = ActionNeed('sign in')

# Permissions
addPatient = Permission(be_admin, be_doctor, be_nurse, be_medAd)
addPatient.description = "add patient permission"
editPatient = Permission(be_admin, be_doctor, be_nurse, be_medAd)
editPatient.description = "edit patient permission"
addDoctor = Permission(be_admin)
addDoctor.description = "add doctor permission"
editDoctor = Permission(be_admin)
editDoctor.description = "edit doctor permission"
addMedAdmin = Permission(be_admin,be_doctor)
addMedAdmin.description = "add Medical Administrator permission"
editMedAdmin = Permission(be_admin,be_doctor)
editMedAdmin.description = "edit Medical Administrator permission"
addInsAdmin = Permission(be_admin)
addInsAdmin.description = "add Insurance Admin permission"
editInsAdmin = Permission(be_admin)
editInsAdmin.description = "edit Insurance Admin permission"
addNurse = Permission(be_admin, be_doctor)
addNurse.description = "add Nurse permission"
editNurse = Permission(be_admin, be_doctor)
editNurse.description = "edit Nurse permission"
addSysAdmin = Permission(be_admin)
addSysAdmin.description = "add System Admin permission"
editSysAdmin = Permission(be_admin)
editSysAdmin.description = "edit System Admin permission"
delUserP = Permission(be_admin)
delUserP.description = "delete User Permission permission"
assignPerm = Permission(be_admin)
assignPerm.description = "assign Permission permission"
editRecordAccess = Permission(be_admin)
editRecordAccess.description = "edit Record Acess permission"
viewPII = Permission(be_medAd,be_insAd)
viewPII.description = "View PII permission"
all = Permission(be_admin,be_doctor,be_insAd,be_medAd,be_nurse,be_patient)
all.description = "all users permitted"
beAdmin= Permission(be_admin)
beDoctor=Permission(be_doctor)
beInsAd=Permission(be_insAd)
beMedAd=Permission(be_medAd)
beNurse=Permission(be_nurse)
bePatient=Permission(be_patient)

apps_needs = [be_admin, be_doctor, be_nurse, be_medAd, be_insAd, be_patient, to_sign_in]
apps_permissions = [addPatient, editPatient, addDoctor, editDoctor, addMedAdmin,editMedAdmin,addInsAdmin,editInsAdmin,addNurse,editNurse,addSysAdmin,
editSysAdmin,delUserP,assignPerm,editRecordAccess,viewPII]


def authenticate(ID, password):
    #get password and role associated with ID
	role = ""
	pass = ""
    if bcrypt.check_password_hash(pw_hash, password):
        return role
		#rest is del if bcrypt works
    elif password == ID + "doctor":
        return "doctor"
    elif password == ID + "nurse":
        return "nurse"
    elif password == ID + "medAdmin":
        return "medAdmin"
    elif password == ID + "insAdmin":
        return "insAdmin"
    elif password == ID + "patient":
        return "patient"
    else:
        return None


def current_privileges():
    return (('{method} : {value}').format(method=n.method, value=n.value)
            for n in apps_needs if n in g.identity.provides)


@app.route('/')
@all.require(http_exception=403)
def index():
    return render_template('login.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = authenticate(request.form['ID'],
                               request.form['password'])
        if user_id:
            identity = Identity(user_id)
            identity_changed.send(app, identity=identity)
            return render_template('privileges.html', priv=current_privileges())
        else:
            return abort(401)
    return render_template('login.html')
	
@app.route('/edit')
@all.require(http_exception=403)
def editor():
    return render_template('editor.html')

@app.route('/admin')
@beAdmin.require(http_exception=403)
def admin():
    return render_template('admin.html')



@app.route("/logout")
def logout():
    for key in ['identity.name', 'identity.auth_type']:
        session.pop(key, None)
    identity_changed.send(app, identity=AnonymousIdentity())
    return render_template('logout.html')


	
@app.route('/createPatient')
@addPatient.require(http_exception=403)
def createPatient():
	if request.method == 'POST':
	    First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
        DOB = request.form['DOB']
        SSN = request.form['SSN']
		Addr = request.form['Address']
		
    return render_template('createPatient.html')

@app.route('/createDoctor')
@addDoctor.require(http_exception=403)
def createDoctor():
	if request.method == 'POST':
	    First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		PracticeName = request.form['PracticeName']
		PracticeAddress = request.form['PracticeAdd']
		RecoveryPhrase = request.form['RecPhrase']
    return render_template('createDoctor.html')

@app.route('/createNurse')
@addNurse.require(http_exception=403)
def createNurse():
	if request.method == 'POST':
	    First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		PracticeName = request.form['PracticeName']
		PracticeAddress = request.form['PracticeAdd']
		AssociatedDoc = request.form['AssociatedDoc']
    return render_template('createNurse.html')	

@app.route('/createSysAdmin')
@addSysAdmin.require(http_exception=403)
def createSysAdmin():
	if request.method == 'POST':
		First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		
    return render_template('createSysAdmin.html')

@app.route('/createMedAdmin')
@addMedAdmin.require(http_exception=403)
def createMedAdmin():
	if request.method == 'POST':
		First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		PracticeName = request.form['PracticeName']
		PracticeAdd = request.form['PracticeAdd']
		AssociatedDoc = request.form['AssociatedDoc']
		AssociatedNur = request.form['AssociatedNur]
    return render_template('createMedAdmin.html')

@app.route('/createInsAdmin')
@addInsAdmin.require(http_exception=403)
def createInsAdmin():
	if request.method == 'POST':
		First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		CompName = request.form['CompanyName']
		CompAdd = request.form['CompanyAddr']
    return render_template('createInsAdmin.html')
	
@app.route('/editPerm')
@assignPerm.require(http_exception=403)
def editPerm():
	if request.method == 'POST':
		UserN = request.form['UserN']
		Permission = request.form['perm']
		#role =   #SQL To find UserN role
	
	    identity.provides()
    return render_template('editPerm.html')

@app.route('/addDoctorExamRecord')
@beDoctor.require(http_exception=403)
@beNurse.require(http_exception=403)
@beMedAd.require(http_exception=403)
def addDoctorExamRecord():
	if request.method == 'POST':
		Date = request.form['Date']
		Doctor = request.form['Doctor']
		Notes = request.form['Notes']
		
    return render_template('addDoctorExamRecord')
	
@app.route('/addTestResultRecord')
@beDoctor.require(http_exception=403)
@beNurse.require(http_exception=403)
@beMedAd.require(http_exception=403)
def addTestResultRecord():
	if request.method == 'POST':
		Date = request.form['Date']
		Doctor = request.form['Doctor']
		Lab = request.form['Lab']
		Notes = request.form['Notes']
    return render_template('addTestResultRecord.html')
	
@app.route('/addDiagnosisRecord')
@beDoctor.require(http_exception=403)
def addDiagnosisRecord():
    if request.method == 'POST':
		Date = request.form['Date']
		Doctor = request.form['Doctor']
		Diagnosis = request.form['Diagnosis']
    return render_template('addDiagnosisRecord.html')
	
@app.route('/addInsuranceClaimRecord')
@beInsAd.require(http_exception=403)
@beMedAd.require(http_exception=403)
def addInsuranceClaimRecord():
	if request.method == 'POST':
		Date = request.form['Date']
		MedUserID = request.form['MedUserID']
		Amount = request.form['Amount']
		Status = request.form['Status']
    return render_template('addInsuranceClaimRecord.html')
	
@app.route('/addRawRecord')
@all.require(http_exception=403)
def addRawRecord():
	if request.method == 'POST':
		Desc = request.form['Description']
		File = request.form['file']
    return render_template('addRawRecord.html')
	
@app.route('/createCorrespondenceRecord')
@beDoctor.require(http_exception=403)
@bePatient.require(http_exception=403)
def createCorrespondenceRecord():
	if request.method == 'POST':
		DocUserID = request.form['DoctorUserID']
		NoteDate = request.form['NoteDate']
		NoteText = request.form['NoteText']
    return render_template('createCorrespondenceRecord.html')
	
@app.route('/addCorrespondenceNote')
@beDoctor.require(http_exception=403)
@bePatient.require(http_exception=403)
def addCorrespondenceNote():
	if request.method == 'POST':
		CorrNum = request.form['CorrNum']
		NoteDate = request.form['NoteDate']
		NoteText = request.form['NoteText']
    return render_template('addCorrespondenceNote.html')
	
@app.route('/listRecords')
@all.require(http_exception=403)
def listRecords():
#sql statement to string
    return render_template('listRecords.html') #,string list
	
	
@app.route('/viewRecord')
@beDoctor.require(http_exception=403)
def viewRecord():
	if request.method == 'POST':
		recordID = request.form['recordID']
	#sql retrieve recordID
	#seperate retrieve checking for diagnosis record and doctor perm
    return render_template('viewRecord.html')
	
@app.route('/editRecordPerm')
@editRecordAccess.require(http_exception=403)
def editRecordPerm():
	if request.method == 'POST':
	    RecID = request.form['First']
		EditPerm = request.form['editPerm']
		ViewPerm = request.form['viewPerm']
        
    return render_template('editRecordPerm.html')
	
@app.route('/editPatient')
@editPatient.require(http_exception=403)
def editPatient():
    if request.method == 'POST':
		UserID = request.form['UserID']
	    First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
        DOB = request.form['DOB']
        SSN = request.form['SSN']
		Addr = request.form['Address']
    return render_template('editPatient.html')
	
@app.route('/editDoctor')
@editDoctor.require(http_exception=403)
def editDoctor():
    if request.method == 'POST':
		UserID = request.form['UserID']
	    First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		PracticeName = request.form['PracticeName']
		PracticeAddress = request.form['PracticeAdd']
		RecoveryPhrase = request.form['RecPhrase']
    return render_template('editDoctor.html')
	
@app.route('/editNurse')
@editNurse.require(http_exception=403)
def editNurse():
    if request.method == 'POST':
		UserID = request.form['UserID']
	    First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		PracticeName = request.form['PracticeName']
		PracticeAddress = request.form['PracticeAdd']
		AssociatedDoc = request.form['AssociatedDoc']
    return render_template('editNurse.html')
	
@app.route('/editSysAdmin')
@editSysAdmin.require(http_exception=403)
def editSysAdmin():
    if request.method == 'POST':
	    UserID = request.form['UserID']
		First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
    return render_template('editSysAdmin.html')
	
@app.route('/editMedAdmin')
@editMedAdmin.require(http_exception=403)
def editMedAdmin():
    if request.method == 'POST':
	    UserID = request.form['UserID']
		First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		PracticeName = request.form['PracticeName']
		PracticeAdd = request.form['PracticeAdd']
		AssociatedDoc = request.form['AssociatedDoc']
		AssociatedNur = request.form['AssociatedNur]
    return render_template('editMedAdmin.html')
	
@app.route('/editInsAdmin')
@editInsAdmin.require(http_exception=403)
def editInsAdmin():
    if request.method == 'POST':
	    UserID = request.form['UserID']
		First = request.form['First']
		Last = request.form['Last']
		Npass = request.form['Npass']
		CompName = request.form['CompanyName']
		CompAdd = request.form['CompanyAddr']
    return render_template('editInsAdmin.html')
	
@app.route('/viewPatientProfile')
@viewPII.require(http_exception=403)
def viewPatientProfile():
    if request.method == 'POST':
	    PatientID = request.form['PID']
    return render_template('viewPatientProfile.html')
	
@app.route('/viewRecoveryPhrase')
@beAdmin.require(http_exception=403)
def viewRecoveryPhrase():
    if request.method == 'POST':
	    DocID = request.form['DID']
    return render_template('viewRecoveryPhrase.html')
	
@app.route('/removeUserProfile')
@delUserP.require(http_exception=403)
def removeUserProfile():
	if request.method == 'POST':
	    UserID = request.form['UID']
    return render_template('removeUserProfile.html')
	
@app.errorhandler(401)
def authentication_failed(e):
    flash('Authenticated failed.')
    return redirect(url_for('login'))


@app.errorhandler(403)
def authorisation_failed(e):
    flash(('Your current identity is {id}. You need special privileges to'
           ' access this page').format(id=g.identity.id))

    return render_template('privileges.html', priv=current_privileges())


@identity_loaded.connect_via(app)
def on_identity_loaded(sender, identity):
    needs = []

    if identity.id in ('admin', 'doctor', 'nurse', 'medAdmin'
						,'insAdmin', 'patient', 'sign in'):
		needs.append(to_sign_in)
		
    if identity.id == "admin":
		needs.append(be_admin)

    if identity.id == 'doctor':
		needs.append(be_admin)
		
    if identity.id == 'nurse':
		needs.append(be_nurse)

    if identity.id == 'medAdmin':
		needs.append(be_medAd)
		
    if identity.id == 'insAdmin':
		needs.append(be_insAd)
		
    if identity.id == 'patient':
		needs.append(be_patient)
		
    for n in needs:
        identity.provides.add(n)



if __name__ == "__main__":
    app.run()
