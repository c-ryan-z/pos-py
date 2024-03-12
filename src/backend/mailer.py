import json
import platform
import requests
import os
from dotenv import load_dotenv

load_dotenv()


domain = os.getenv('MG_DOMAIN')
api_key = os.getenv('MG_API_KEY')


def two_factor_auth(user_name, email, code):
    ip_address = requests.get('https://api64.ipify.org').text
    ip_info = requests.get(f'https://ipinfo.io/{ip_address}/json').json()
    location = f"{ip_info['city']}, {ip_info['region']}, {ip_info['country']}"

    device_info = platform.system() + " " + platform.release()

    api_vars = {
        "TFA": code,
        "ip-add": location,
        "location": device_info
    }

    return requests.post(
        f"https://api.mailgun.net/v3/{domain}/messages",
        auth=("api", api_key),
        data={"from": f"Login Attempt <info@{domain}>",
              "to": f"{user_name} <{email}>",
              "subject": "2FA Code",
              "template": "2fa-test",
              "h:X-Mailgun-Variables": json.dumps(api_vars)})
