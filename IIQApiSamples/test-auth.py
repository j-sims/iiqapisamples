import requests
import json
import urllib3
# Supresses the self signed cert warning
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

IIQServerIP = 'CHANGEME'
PORT = 8000
USER = 'administrator'
PASS = 'CHANGEME'

uri = "https://%s:%s" % (IIQServerIP, PORT)

data = json.dumps(
    {'username': USER, 'password': PASS, 'services': ['platform']})

# uri of the cluster used in the referer header
uri = f"https://{IIQServerIP}:{PORT}"

# Set header as content will provided in json format
headers = {'Content-Type': 'application/json'}

# Create json dictionary for auth
data = json.dumps(
    {'username': USER, 'password': PASS })

# create a session object to hold cookies
session = requests.Session()

# Establish session using auth credentials
response = session.post(uri + "/insightiq/rest/security-iam/v1/auth/login",
                        data=data, headers=headers, verify=False)

if 200 <= response.status_code < 299:
    # Set headers for CSRF protection. Without these two headers all further calls with be "auth denied"
    session.headers['x-csrf-token'] = session.cookies.get('isicsrf')
    print("Authorization Successful")
else:
    print("Authorization Failed")
    print(response.content)

endpoint = '/insightiq/rest/security-iam/v1/auth/session/'

response = session.get(uri + endpoint, verify=False)

print(response.content)
