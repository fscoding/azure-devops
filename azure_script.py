from azure.devops.connection import Connection
from msrest.authentication import BasicAuthentication
import pprint
import os
import json

# Fill in with your personal access token and org URL
personal_access_token = os.environ.get('AZURE_DEVOPS')
organization_url = 'https://dev.azure.com/' + os.environ.get('AZURE_ORG')
project=os.environ.get('AZURE_PROJECT')


releaseId = 1583
definitionId = 6

# Create a connection to the org
credentials = BasicAuthentication('', personal_access_token)
connection = Connection(base_url=organization_url, creds=credentials)


## This line will get actuall release
release_client = connection.clients_v5_0.get_release_client()

release_definitions = release_client.get_release_definition(project, 6)


release_client.update_release_definition(release_definitions, project)


release_definitions.deserialize(data)
