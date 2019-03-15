import requests
from requests.auth import HTTPBasicAuth
import os
import json

personal_access_token = os.environ.get('AZURE_DEVOPS')
organization=os.environ.get('AZURE_ORG')
project=os.environ.get('AZURE_PROJECT')

## Get release print out
releaseId=1583
url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases/{releaseId}?ap'

class azure_dev:

    def __init__(self, credentials=None):
        self._user = credentials['username']
        self._password = credentials['password']
        self._session = None

    def __enter__(self):
        self._session = requests.Session()
        self._session.auth = (self._user, self._password)
        self._session.headers.update({'content-type': 'application/json'})
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        if self._session is not None:
            self._session.close()
            self._session = None

    def get_release(self, organization, project, releaseId):
        """
            This method will get release and return as dictionary
        """
        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases/{releaseId}?ap'
        return self._session.get(url).json()


    def create_release(self, organization, project, description):
        """
            This method will create release and return as dictionary.
        """
        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases?api-version=5.0'
        object = { "definitionId": 6,
        "description": description,
        "artifacts": [ { "alias": "Fabrikam.CI", "instanceReference": { "id": "2", "name": None }} ],
          "isDraft": False,
          "reason": "none",
          "manualEnvironments": None
        }

        return self._session.post(url, json=object).json()


cred = {'username':'', 'password': os.environ.get('AZURE_DEVOPS')}
with azure_dev(cred) as azure_client:
    data = azure_client.get_release(organization, project, releaseId)
    for iter in data['environments']:
        print(f'ID :{str(iter["id"])}  Name: {iter["name"]} Status {iter["status"]}')
