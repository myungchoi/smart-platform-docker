# -*- coding: utf-8 -*-

import logging
from fhirclient import client
from fhirclient.models.medication import Medication
from fhirclient.models.medicationorder import MedicationOrder
from fhirclient.models.medicationadministration import MedicationAdministration
from fhirclient.models.medicationdispense import MedicationDispense

from flask import Flask, request, redirect, session

# app setup
# smart_defaults = {
#     'app_id': 'my_web_app',
#     'api_base': 'http://smart-wip.hdap.gatech.edu:8080/gt-fhir-webapp/base',
#     'redirect_uri': 'http://smart-wip.hdap.gatech.edu:8000/fhir-app/',
# }
smart_defaults = {
    'app_id': 'my_web_app',
    'api_base': 'http://https://gt-apps.hdap.gatech.edu/smart-fhir/gt-fhir-webapp/base',#'api_base': 'http://smart-fhir:8080/gt-fhir-webapp/base',
    'redirect_uri': 'http://smart-pythonapp:8000/fhir-app/',
}

app = Flask(__name__)

def _save_state(state):
    session['state'] = state

def _get_smart():
    state = session.get('state')
    if state:
        return client.FHIRClient(state=state, save_func=_save_state)
    else:
        return client.FHIRClient(settings=smart_defaults, save_func=_save_state)

def _logout():
    if 'state' in session:
        smart = _get_smart()
        smart.reset_patient()

def _reset():
    if 'state' in session:
        del session['state']

def _get_prescriptions(smart):
    bundle = MedicationOrder.where({'patient': smart.patient_id}).perform(smart.server)
    pres = [be.resource for be in bundle.entry] if bundle is not None and bundle.entry is not None else None
    if pres is not None and len(pres) > 0:
        return pres
    return None

def _get_med_dispense(smart):
    bundle = MedicationDispense.where({'patient': smart.patient_id}).perform(smart.server)
    dispense = [be.resource for be in bundle.entry] if bundle is not None and bundle.entry is not None else None
    if dispense is not None and len(dispense) > 0:
        return dispense
    return None

def _get_med_administration(smart):
    bundle = MedicationAdministration.where({'patient': smart.patient_id}).perform(smart.server)
    adm = [be.resource for be in bundle.entry] if bundle is not None and bundle.entry is not None else None
    if adm is not None and len(adm) > 0:
        return adm
    return None

def _med_name(prescription):
    if prescription.medicationCodeableConcept and prescription.medicationCodeableConcept.coding[0].display:
        return prescription.medicationCodeableConcept.coding[0].display
    if prescription.text and prescription.text.div:
        return prescription.text.div
    return "Unnamed Medication(TM)"


# views

@app.route('/')
@app.route('/index.html')
def index():
    """ The app's main page.
    """
    smart = _get_smart()
    body = "<h1>Hello</h1>"
    
    if smart.ready and smart.patient is not None:       # "ready" may be true but the access token may have expired, making smart.patient = None
        name = smart.human_name(smart.patient.name[0] if smart.patient.name and len(smart.patient.name) > 0 else 'Unknown')
        
        # generate simple body text
        body += "<p>You are authorized and ready to make API requests for <em>{0}</em>.</p>".format(name)
        pres = _get_prescriptions(smart)
        if pres is not None:
            body += "<p>{0} prescriptions: <ul><li>{1}</li></ul></p>".format("His" if 'male' == smart.patient.gender else "Her", '</li><li>'.join([_med_name(p) for p in pres]))
        else:
            body += "<p>(There are no prescriptions for {0})</p>".format("him" if 'male' == smart.patient.gender else "her")
        dispense = _get_med_dispense(smart)
        if dispense is not None:
            body += "<p>{0} medication dispenses: <ul><li>{1}</li></ul></p>".format("His" if 'male' == smart.patient.gender else "Her", '</li><li>'.join([_med_name(p) for p in dispense]))
        else:
            body += "<p>(There are no medication dispenses for {0})</p>".format("him" if 'male' == smart.patient.gender else "her")
        adm = _get_med_administration(smart)
        if adm is not None:
            body += "<p>{0} medication administrations: <ul><li>{1}</li></ul></p>".format("His" if 'male' == smart.patient.gender else "Her", '</li><li>'.join([_med_name(p) for p in adm]))
        else:
            body += "<p>(There are no medication administrations for {0})</p>".format("him" if 'male' == smart.patient.gender else "her")

        body += """<p><a href="/logout">Change patient</a></p>"""
    else:
        auth_url = smart.authorize_url
        if auth_url is not None:
            body += """<p>Please <a href="{0}">authorize</a>.</p>""".format(auth_url)
        else:
            body += """<p>Running against a no-auth server, nothing to demo here. """
        body += """<p><a href="/reset" style="font-size:small;">Reset</a></p>"""
    return body


@app.route('/fhir-app/')
def callback():
    """ OAuth2 callback interception.
    """
    smart = _get_smart()
    try:
        smart.handle_callback(request.url)
    except Exception as e:
        return """<h1>Authorization Error</h1><p>{0}</p><p><a href="/">Start over</a></p>""".format(e)
    return redirect('/')


@app.route('/logout')
def logout():
    _logout()
    return redirect('/')


@app.route('/reset')
def reset():
    _reset()
    return redirect('/')


# start the app
if '__main__' == __name__:
    import flaskbeaker
    flaskbeaker.FlaskBeaker.setup_app(app)
    
    logging.basicConfig(level=logging.DEBUG)
    app.run(host='0.0.0.0', debug=True, port=8000)
