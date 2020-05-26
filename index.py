import utils.set_env as env
import http.client, urllib.parse
import requests, base64

def createUser():
    headers = {
        'X-Reference-Id': env.env_var['X-Reference-Id-User'],
        'Content-Type': 'application/json',
        'Ocp-Apim-Subscription-Key': env.env_var['Primary-Key'],
    }

    payload = {'providerCallbackHost': env.env_var['callback']}
    try:
        r = requests.post('https://sandbox.momodeveloper.mtn.com/v1_0/apiuser', json=payload, headers=headers)
        print(r.status_code, r.text)
    except Exception as e:
        pass
