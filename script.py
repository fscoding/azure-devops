from module.azure import azure_dev, save
import os
import json
import math

personal_access_token = os.environ.get('AZURE_DEVOPS')
organization=os.environ.get('AZURE_ORG')
project=os.environ.get('AZURE_PROJECT')

## Get release print out
# releaseId = 1617
releaseId = 1583
definitionId = 6

cred = {'username':'', 'password': os.environ.get('AZURE_DEVOPS')}
with azure_dev(cred) as client:

    ## Get all releases and run for loop.
    release = client.getRelease(organization, project, releaseId)
    save(release, 'release')


    for iter in release['environments']:
        print(f'ID :{str(iter["id"])}  Name: {iter["name"]} Status {iter["status"]}')

    ## Get release definition and run for lop
    release_definition = client.getReleaseDefinition(organization, project, definitionId)
    save(release_definition, 'release_definition')

    ## Give approval
    reassigned = client.giveApproval(organization, project, 8987, 'reassigned')

    ## This method will create actual release
    createRelease = client.createRelease(organization, project, definitionId)
    save(createRelease, 'createdRelease')
