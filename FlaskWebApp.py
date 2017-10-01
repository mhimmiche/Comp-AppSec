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
admin = Permission(to_sign_in)
admin.description= "System Admin"
doctor = Permission(to_sign_in)
doctor.description= "System Admin"
nurse = Permission(to_sign_in)
nurse.description= "System Admin"
medAd = Permission(to_sign_in)
medAd.description= "System Admin"
insAd = Permission(to_sign_in)
insAd.description= "System Admin"
patient = Permission(to_sign_in)
patient.description= "System Admin"

apps_permissions = [admin, doctor, nurse, medAd, insAd, patient]
apps_needs = [addPatient, editPatient, addDoctor, editDoctor, addMedAd,editMedAd,addInsAd,editInsAd,addNurse,editNurse,addSysAd,
editSysAd,delUserP,assignPerm,editRec,viewPII]


def authenticate(email, password):
    if password == email + "admin":
        return "admin"
    elif password == email + "doctor":
        return "doctor"
    elif password == email + "editor":
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


@app.route('/admin')
@admin.require(http_exception=403)
def admin():
    return render_template('admin.html')


@app.route('/nurse')
@nurse.require(http_exception=403)
def editor():
    return render_template('admin.html')

@app.route("/logout")
def logout():
    for key in ['identity.name', 'identity.auth_type']:
        session.pop(key, None)
    identity_changed.send(app, identity=AnonymousIdentity())
    return render_template('logout.html')


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

    if identity.id in ('edit', 'admin'):
		needs.append(addPatient)

    if identity.id == 'admin':
		needs.append(addPatient)

    for n in needs:
        identity.provides.add(n)



if __name__ == "__main__":
    app.run()
