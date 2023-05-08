import requests
import webbrowser
from settings import CLIENT_ID
from settings import SECRET_ID

#Obtener código de la url
def get_url_code():
    url = 'https://github.com/login/oauth/authorize'
    params = {
        'client_id':CLIENT_ID,
        'scope':'user'
    }

    response = requests.get(url, params=params)
    return response.url

#Obtener Access Token 
def get_access_token(code):
    url = 'https://github.com/login/oauth/access_token'
    params ={
        'client_id':CLIENT_ID,
        'client_secret':SECRET_ID,
        'code': code
            }
    headers = {'Accept':'application/json'}

    response = requests.post(url, params=params, headers = headers)

    if response.status_code == 200:
        payload = response.json().get('access_token')
    return payload
    
#Obtener el usuario autenticado

def get_user(token):
    url = 'https://api.github.com/user'
    headers = {
        "Accept": "application/vnd.github+json",
        'Authorization': f'Bearer {access_token}',
        "X-GitHub-Api-Version": "2022-11-28"
            }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        username =response.json()
    return username

if __name__ == '__main__':

    url = get_url_code()
    webbrowser.open(url)

    code = input('Ingresa el código: ')
    code = code.strip().replace('\n', '')

    access_token = get_access_token(code)

    user = get_user(access_token)

    print(user)
    pass
