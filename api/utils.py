import os
from twilio.rest import Client
from flask import jsonify

account_sid = os.getenv("TWILIO_ACCOUNT_SID")
auth_token = os.getenv("TWILIO_AUTH_TOKEN")
service_sid = os.getenv("TWILIO_VERIFY_SERVICE_SID")
twilio_client = Client(account_sid, auth_token)


def send_otp(receiver):
    verification = twilio_client.verify.v2.services(
        service_sid
    ).verifications.create(to=receiver, channel="sms")

    return jsonify({
        "status": verification.status,
        "channel": "sms"
    }), 200

def verify_otp(receiver, otp):
    verification = twilio_client.verify.v2.services(
        service_sid
    ).verification_checks.create(to=receiver, code=otp)

    return jsonify({
        "status": verification.status,
        "channel": "sms"
    }), 200