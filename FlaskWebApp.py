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
addPatient = RoleNeed('add patient')
editPatient = RoleNeed('edit patient')
addMedAd = RoleNeed('add medical admin')
editMedAd = RoleNeed('edit medical admin')
addInsAd = RoleNeed('add insurance admin')
editInsAd = RoleNeed('edit insurance admin')
addNurse = RoleNeed('add nurse')
editNurse = RoleNeed('edit nurse')
editDoctor = RoleNeed('edit doctor')
addDoctor = RoleNeed('add doctor')
addSysAd = RoleNeed('add system admin')
editSysAd = RoleNeed('edit system admin')
delUserP = RoleNeed('delete user permission')
editRec = RoleNeed('edit record access')
viewPII = RoleNeed('view PII')
assignPerm = RoleNeed('assing permission')
to_sign_in = ActionNeed('sign in')

# Permissions
admin = Permission(to_sign_in, addPatient, editPatient,addDoctor,editDoctor,addMedAd,editMedAd
,addInsAd,editInsAd,addNurse,editNurse,addSysAd,editSysAd,delUserP,assignPerm,editRec)
admin.description= "System Administrator"
doctor = Permission(to_sign_in,addPatient,editPatient,addMedAd,editMedAd,addNurse,editNurse)
doctor.description= "Doctor"
nurse = Permission(to_sign_in,addPatient,editPatient)
nurse.description= "Nurse"
medAd = Permission(to_sign_in,addPatient,editPatient,viewPII)
medAd.description= "Medical Administrator"
insAd = Permission(to_sign_in, viewPII)
insAd.description= "Insurance Admin"
patient = Permission(to_sign_in)
patient.description= "Patient"

apps_permissions = [admin, doctor, nurse, medAd, insAd, patient]
apps_needs = [addPatient, editPatient, addDoctor, editDoctor, addMedAd,editMedAd,addInsAd,editInsAd,addNurse,editNurse,addSysAd,
editSysAd,delUserP,assignPerm,editRec,viewPII]


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
@patient.require(http_exception=403)
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
@admin.require(http_exception=403)
def editor():
    return render_template('editor.html')

@app.route('/admin')
@admin.require(http_exception=403)
def admin():
    return render_template('admin.html')



@app.route("/logout")
def logout():
    for key in ['identity.name', 'identity.auth_type']:
        session.pop(key, None)
    identity_changed.send(app, identity=AnonymousIdentity())
    return render_template('logout.html')


	
@app.route('/createPatient')
@doctor.require(http_exception=403)
def createPatient():
    return render_template('createPatient.html')

@app.route('/createDoctor')
@doctor.require(http_exception=403)
def createDoctor():
    return render_template('createDoctor.html')

@app.route('/createNurse')
@doctor.require(http_exception=403)
def createNurse():
    return render_template('createNurse.html')	

@app.route('/createSysAdmin')
@doctor.require(http_exception=403)
def createSysAdmin():
    return render_template('createSysAdmin.html')

@app.route('/createMedAdmin')
@doctor.require(http_exception=403)
def createMedAdmin():
    return render_template('createMedAdmin.html')

@app.route('/createInsAdmin')
@doctor.require(http_exception=403)
def createInsAdmin():
    return render_template('createInsAdmin.html')
	
@app.route('/editPerm')
@doctor.require(http_exception=403)
def editPerm():
    return render_template('editPerm.html')

@app.route('/addDoctorExamRecord')
@doctor.require(http_exception=403)
def addDoctorExamRecord():
    return render_template('addDoctorExamRecord')
	
@app.route('/addTestResultRecord')
@doctor.require(http_exception=403)
def addTestResultRecord():
    return render_template('addTestResultRecord.html')
	
@app.route('/addDiagnosisRecord')
@doctor.require(http_exception=403)
def addDiagnosisRecord():
    return render_template('addDiagnosisRecord.html')
	
@app.route('/addInsuranceClaimRecord')
@doctor.require(http_exception=403)
def addInsuranceClaimRecord():
    return render_template('addInsuranceClaimRecord.html')
	
@app.route('/addRawRecord')
@doctor.require(http_exception=403)
def addRawRecord():
    return render_template('addRawRecord.html')
	
@app.route('/createCorrespondenceRecord')
@doctor.require(http_exception=403)
def createCorrespondenceRecord():
    return render_template('createCorrespondenceRecord.html')
	
@app.route('/addCorrespondenceNote')
@doctor.require(http_exception=403)
def addCorrespondenceNote():
    return render_template('addCorrespondenceNote.html')
	
@app.route('/listRecords')
@doctor.require(http_exception=403)
def listRecords():
    return render_template('listRecords.html')
	
@app.route('/viewRecord')
@doctor.require(http_exception=403)
def viewRecord():
    return render_template('viewRecord.html')
	
@app.route('/editRecordPerm')
@doctor.require(http_exception=403)
def editRecordPerm():
    return render_template('editRecordPerm.html')
	
@app.route('/editPatient')
@doctor.require(http_exception=403)
def editPatient():
    return render_template('editPatient.html')
	
@app.route('/editDoctor')
@doctor.require(http_exception=403)
def editDoctor():
    return render_template('editDoctor.html')
	
@app.route('/editNurse')
@doctor.require(http_exception=403)
def editNurse():
    return render_template('editNurse.html')
	
@app.route('/editSysAdmin')
@doctor.require(http_exception=403)
def editSysAdmin():
    return render_template('editSysAdmin.html')
	
@app.route('/editMedAdmin')
@doctor.require(http_exception=403)
def editMedAdmin():
    return render_template('editMedAdmin.html')
	
@app.route('/editInsAdmin')
@doctor.require(http_exception=403)
def editInsAdmin():
    return render_template('editInsAdmin.html')
	
@app.route('/viewPatientProfile')
@doctor.require(http_exception=403)
def viewPatientProfile():
    return render_template('viewPatientProfile.html')
	
@app.route('/viewRecoveryPhrase')
@doctor.require(http_exception=403)
def viewRecoveryPhrase():
    return render_template('viewRecoveryPhrase.html')
	
@app.route('/removeUserProfile')
@doctor.require(http_exception=403)
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
		needs.append(addPatient)

    if identity.id == 'doctor':
		needs.append(addPatient)

    for n in needs:
        identity.provides.add(n)



if __name__ == "__main__":
    app.run()
