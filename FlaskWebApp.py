# -*- coding: utf-8 -*-

from flask import (abort, flash, Flask, g,
    redirect, render_template, request, session, url_for)

from flask_principal import (ActionNeed, AnonymousIdentity,
    Identity, identity_changed, identity_loaded, Principal, 
	Permission, RoleNeed)

app = Flask(__name__)

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
addPatient.description = "System Administrator's permissions"
editPatient = Permission(be_admin, be_doctor, be_nurse, be_medAd)
editPatient.description = "Doctor's permissions"
addDoctor = Permission(be_admin)
addDoctor.description = "Nurse's permissions"
editDoctor = Permission(be_admin)
editDoctor.description = "Medical Administrator's permissions"
addMedAdmin = Permission(be_admin,be_doctor)
addMedAdmin.description = "Insurance Administrator's permissions"
editMedAdmin = Permission(be_admin,be_doctor)
editMedAdmin.description = "Insurance Administrator's permissions"
addInsAdmin = Permission(be_admin)
addInsAdmin.description = "Patient's permissions"
editInsAdmin = Permission(be_admin)
editInsAdmin.description = "Patient's permissions"
addNurse = Permission(be_admin, be_doctor)
addNurse.description = "Patient's permissions"
editNurse = Permission(be_admin, be_doctor)
editNurse.description = "Patient's permissions"
addSysAdmin = Permission(be_admin)
addSysAdmin.description = "Patient's permissions"
editSysAdmin = Permission(be_admin)
editSysAdmin.description = "Patient's permissions"
delUserP = Permission(be_admin)
delUserP.description = "Patient's permissions"
assignPerm = Permission(be_admin)
assignPerm.description = "Patient's permissions"
editRecordAccess = Permission(be_admin)
editRecordAccess.description = "Patient's permissions"
viewPII = Permission(be_medAd,be_insAd)
viewPII.description = "Patient's permissions"
all = Permission(be_admin,be_doctor,be_insAd,be_medAd,be_nurse,be_patient)
all.description = "all users permitted"
be_admin= Permission(be_admin)
be_doctor=Permission(be_doctor)
be_insAd=Permission(be_insAd)
be_medAd=Permission(be_medAd)
be_nurse=Permission(be_nurse)
be_patient=Permission(be_patient)

apps_needs = [be_admin, be_doctor, be_nurse, be_medAd, be_insAd, be_patient, to_sign_in]
apps_permissions = [addPatient, editPatient, addDoctor, editDoctor, addMedAdmin,editMedAdmin,addInsAdmin,editInsAdmin,addNurse,editNurse,addSysAdmin,
editSysAdmin,delUserP,assignPerm,editRecordAccess,viewPII]


def authenticate(email, password):
    if password == email + "admin":
        return "admin"
    elif password == email + "doctor":
        return "doctor"
    elif password == email + "nurse":
        return "nurse"
    elif password == email + "medAdmin":
		return "medAdmin"
    elif password == email + "insAdmin":
		return "insAdmin"
    elif password == email + "patient":
		return "patient"
    else:
        return None


def current_privileges():
    return (('{method} : {value}').format(method=n.method, value=n.value)
            for n in apps_needs if n in g.identity.provides)


@app.route('/')
@all.require(http_exception=403)
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_id = authenticate(request.form['email'],
                               request.form['password'])
        if user_id:
            identity = Identity(user_id)
            identity_changed.send(app, identity=identity)
            return redirect(url_for('index'))
        else:
            return abort(401)
    return render_template('login.html')
	
@app.route('/edit')
@all.require(http_exception=403)
def editor():
    return render_template('editor.html')

@app.route('/admin')
@be_admin.require(http_exception=403)
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
    return render_template('createPatient.html')

@app.route('/createDoctor')
@addDoctor.require(http_exception=403)
def createDoctor():
    return render_template('createDoctor.html')

@app.route('/createNurse')
@addNurse.require(http_exception=403)
def createNurse():
    return render_template('createNurse.html')	

@app.route('/createSysAdmin')
@addSysAdmin.require(http_exception=403)
def createSysAdmin():
    return render_template('createSysAdmin.html')

@app.route('/createMedAdmin')
@addMedAdmin.require(http_exception=403)
def createMedAdmin():
    return render_template('createMedAdmin.html')

@app.route('/createInsAdmin')
@addInsAdmin.require(http_exception=403)
def createInsAdmin():
    return render_template('createInsAdmin.html')
	
@app.route('/editPerm')
@assignPerm.require(http_exception=403)
def editPerm():
    return render_template('editPerm.html')

@app.route('/addDoctorExamRecord')
@be_doctor.require(http_exception=403)
@be_nurse.require(http_exception=403)
@be_medAd.require(http_exception=403)
def addDoctorExamRecord():
    return render_template('addDoctorExamRecord')
	
@app.route('/addTestResultRecord')
@be_doctor.require(http_exception=403)
@be_nurse.require(http_exception=403)
@be_medAd.require(http_exception=403)
def addTestResultRecord():
    return render_template('addTestResultRecord.html')
	
@app.route('/addDiagnosisRecord')
@be_doctor.require(http_exception=403)
def addDiagnosisRecord():
    return render_template('addDiagnosisRecord.html')
	
@app.route('/addInsuranceClaimRecord')
@be_insAd.require(http_exception=403)
@be_medAd.require(http_exception=403)
def addInsuranceClaimRecord():
    return render_template('addInsuranceClaimRecord.html')
	
@app.route('/addRawRecord')
@all.require(http_exception=403)
def addRawRecord():
    return render_template('addRawRecord.html')
	
@app.route('/createCorrespondenceRecord')
@be_doctor.require(http_exception=403)
@be_patient.require(http_exception=403)
def createCorrespondenceRecord():
    return render_template('createCorrespondenceRecord.html')
	
@app.route('/addCorrespondenceNote')
@be_doctor.require(http_exception=403)
@be_patient.require(http_exception=403)
def addCorrespondenceNote():
    return render_template('addCorrespondenceNote.html')
	
@app.route('/listRecords')
@all.require(http_exception=403)
def listRecords():
    return render_template('listRecords.html')
	
@app.route('/viewRecord')
@be_doctor.require(http_exception=403)
def viewRecord():
    return render_template('viewRecord.html')
	
@app.route('/editRecordPerm')
@editRecordAccess.require(http_exception=403)
def editRecordPerm():
    return render_template('editRecordPerm.html')
	
@app.route('/editPatient')
@editPatient.require(http_exception=403)
def editPatient():
    return render_template('editPatient.html')
	
@app.route('/editDoctor')
@editDoctor.require(http_exception=403)
def editDoctor():
    return render_template('editDoctor.html')
	
@app.route('/editNurse')
@editNurse.require(http_exception=403)
def editNurse():
    return render_template('editNurse.html')
	
@app.route('/editSysAdmin')
@editSysAdmin.require(http_exception=403)
def editSysAdmin():
    return render_template('editSysAdmin.html')
	
@app.route('/editMedAdmin')
@editMedAdmin.require(http_exception=403)
def editMedAdmin():
    return render_template('editMedAdmin.html')
	
@app.route('/editInsAdmin')
@editInsAdmin.require(http_exception=403)
def editInsAdmin():
    return render_template('editInsAdmin.html')
	
@app.route('/viewPatientProfile')
@viewPII.require(http_exception=403)
def viewPatientProfile():
    return render_template('viewPatientProfile.html')
	
@app.route('/viewRecoveryPhrase')
@be_admin.require(http_exception=403)
def viewRecoveryPhrase():
    return render_template('viewRecoveryPhrase.html')
	
@app.route('/removeUserProfile')
@delUserP.require(http_exception=403)
def removeUserProfile():
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

    if identity.id == 'admin':
		needs.extend((addPatient,editPatient,addDoctor,editDoctor,addMedAdmin
		,editMedAdmin,addInsAdmin,editInsAdmin,addNurse,editNurse,addSysAdmin
		,editSysAdmin,delUserP,assignPerm,editRecordAccess,all))

    if identity.id == 'doctor':
		needs.extend((addPatient,editPatient,addMedAdmin,editMedAdmin
		,addNurse,editNurse,all))
		
    if identity.id == 'nurse':
		needs.extend((addPatient,editPatient,all))	

    if identity.id == 'medAdmin':
		needs.extend((addPatient,editPatient,viewPII,all))
		
    if identity.id == 'insAdmin':
		needs.extend((viewPII,all))
		
    if identity.id == 'patient':
		needs.append(all)
		
    for n in needs:
        identity.provides.add(n)



if __name__ == "__main__":
    app.run()
