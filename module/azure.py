import requests
import json
import os
import yaml

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

    def getRelease(self, organization, project, releaseId):
        """
            This method will get release and return as dictionary
        """
        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases/{releaseId}?api-version=5.0'
        return self._session.get(url).json()

    def getReleaseDefinition(self, organization, project, definitionId):
        """
            This method will get release definition and return as dictionary
        """
        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions/{definitionId}?api-version=5.0'
        return self._session.get(url).json()

    def createRelease(self, organization, project, definitionId, description=None, tags=None):
        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/releases?api-version=5.0'
        object = { "definitionId": definitionId,
        "description": None,
        "artifacts": [ { "alias": "_prodops-components tests",
        "instanceReference": { "id": "2", "name": None } } ], "isDraft": False, "reason": "none", "manualEnvironments": None }
        if description:
            object['description'] = description
        if tags:
            object['tags'] = tags
        return self._session.post(url, json=object).json()

    def deleteReleaseDefinition(self, organization, project, definitionId):
        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions/{definitionId}?api-version=5.0'
        return self._session.delete(url).json()

    def createReleaseDefinition(self, organization, project, data):
        """
            This method will create release definition
        """

        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions?api-version=5.0'
        if data:
            object=data
        return self._session.post(url, json=object).json()

    def giveApproval(self, organization, project, approvalId, status, comment=None):
        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/approvals/{approvalId}?api-version=5.0'
        if comment:
            object = { "status": status.lower(), "comments": comment}
        object = {"status": status.lower(), "comments": "Good to go!"}
        self._session.patch(url, json=object).json()

    def update_release_definition(self, organization, project, data=None):
        """ UpdateReleaseDefinition.
        """
        url = f'https://vsrm.dev.azure.com/{organization}/{project}/_apis/release/definitions?api-version=5.0'
        if data:
            object = data
        else:
            return 'Error you have to give data'
        return self._session.put(url, json=object).json()




def loadYaml(filename):
    if os.path.isfile(filename):
        try:
            return yaml.load(open(filename),  Loader=yaml.FullLoader)
        except:
            return 'file does not .yaml'
    else:
        return 'File does not exist!'

def saveYaml(filename, data):
    try:
        with open(filename, 'w') as file:
            yaml.dump(data, file)
    except:
        return 'file does not .yaml'

def loadJson(filename):
    if os.path.isfile(filename):
        try:
            return json.load(open(filename))
        except:
            return 'file does not .json'
    else:
        return 'File does not exist!'

def saveJson(data, fileName=None):
    if fileName:
        with open(fileName + '.json', 'w') as file:
            json.dump(data, file, indent=2)
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=2)
