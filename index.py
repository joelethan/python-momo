import utils.set_env as env
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

def getAPIKey():
    headers = {
        'Ocp-Apim-Subscription-Key': env.env_var['Primary-Key']
    }
    url = 'https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/{}/apikey'.format(env.env_var['X-Reference-Id-User'])
    try:
        r = requests.post(url, headers=headers)
        print(r.status_code, r.text)
    except Exception as e:
        pass

def getUser():
    headers = {
        'Ocp-Apim-Subscription-Key': env.env_var['Primary-Key'],
    }
    url = 'https://sandbox.momodeveloper.mtn.com/v1_0/apiuser/%s'%env.env_var['X-Reference-Id-User']
    try:
        r = requests.get(url, headers=headers)
        print(r.status_code, r.text)
    except Exception as e:
        pass

def createAccessToken():
    usrPass = env.env_var['X-Reference-Id-User']+':'+env.env_var['APIKey']
    b64Val = base64.b64encode(usrPass.encode()).decode()
    headers = {
        'Authorization': 'Basic '+b64Val,
        'Ocp-Apim-Subscription-Key': env.env_var['Primary-Key']
    }
    url = 'https://sandbox.momodeveloper.mtn.com/collection/token/'
    try:
        r = requests.post(url, json={}, headers=headers)
        print(r.status_code, r.text)
    except Exception as e:
        pass
