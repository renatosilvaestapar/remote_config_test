import argparse
from google.auth.transport.requests import Request
from google.oauth2 import service_account
import requests

project_id = 'PROJECT_ID'
credentials_path = 'CREDENTIALS_PATH'
scopes = ['https://www.googleapis.com/auth/firebase.remoteconfig']
credentials = service_account.Credentials.from_service_account_file(credentials_path, scopes=scopes)
credentials.refresh(Request())
token = credentials.token
print(token)
response = requests.get(f'https://firebaseremoteconfig.googleapis.com/v1/projects/{project_id}/remoteConfig', headers = {'Authorization': f'Bearer {token}'})
print(response.json())