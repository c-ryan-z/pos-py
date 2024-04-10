import json
import requests
import os
from dotenv import load_dotenv
from src.backend.Utilities import email_infos

load_dotenv()

domain = os.getenv('MG_DOMAIN')
api_key = os.getenv('MG_API_KEY')


def send_email(user_name, email, code, subject, template):
    location, os_info = email_infos()

    api_vars = {
        "code": code,
        "ip-add": location,
        "location": os_info
    }

    if template == "2fa-test":
        email_name = "Login Attempt"
    else:
        email_name = "Password Reset"

    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": f"{email_name} <info@{domain}>",
              "to": f"{user_name} <{email}>",
              "subject": subject,
              "template": template,
              "h:X-Mailgun-Variables": json.dumps(api_vars)})


def two_factor_auth(user_name, email, code):
    return send_email(user_name, email, code, "2FA Code", "2fa-test")


def password_reset(user_name, email, code):
    return send_email(user_name, email, code, "Password Reset Code", "forgot-password")
