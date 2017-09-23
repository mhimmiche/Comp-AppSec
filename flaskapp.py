#Russell Dixon
#September 18, 2017
#Flask framework to build web server
#Very basic Draft

from flask import Flask
from flask import Response
flask_app = Flask('flaskapp')


@flask_app.route('/createPatient')
def createPatient():
	return Response(
        'Create the patient!\n',
        mimetype='text/plain'
    )
	return
@flask_app.route('/createDoctor')
def createDoctor():
    return Response(
        'Create the Doctor\n',
        mimetype='text/plain'
    )
@flask_app.route('/createSysAdmin')
def createSysAdmin():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )

@flask_app.route('/createMedAdmin')
def createMedAdmin():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )

@flask_app.route('/createInsAdmin')
def createInsAdmin():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )

@flask_app.route('/editPerm')
def editPerm():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )

@flask_app.route('/addTestResultRecord')
def addTestResultRecord():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/addDiagnosisRecord')
def addDiagnosisRecord():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/addInsuranceClaimRecord')
def addInsuranceClaimRecord():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/addRawRecord')
def addRawRecord():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/createCorrespondenceRecord')
def createCorrespondenceRecord():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/addCorrespondenceNote')
def addCorrespondenceNote():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/listRecords')
def listRecords():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/viewRecord')
def viewRecord():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/editRecordPerm')
def editRecordPerm():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/editPatient')
def editPatient():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/editDoctor')
def editDoctor():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/editNurse')
def editNurse():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )

@flask_app.route('/editSysAdmin')
def editSysAdmin():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/editMedAdmin')
def editMedAdmin():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/editInsAdmin')
def editInsAdmin():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/viewPatientProfile')
def viewPatientProfile():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/viewRecoveryPhase')
def viewRecoveryPhase():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	
@flask_app.route('/removeUserProfile')
def removeUserProfile():
    return Response(
        'blahblahblah\n',
        mimetype='text/plain'
    )
	

app = flask_app.wsgi_app