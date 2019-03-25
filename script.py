from module.azure import azure_dev, saveJson, loadYaml, loadJson, saveYaml
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

cred = {'username': '', 'password': os.environ.get('AZURE_DEVOPS')}
with azure_dev(cred) as client:

    ## Get all releases and run for loop.
    # saveJson(release, 'release')

    # ## This method will create actual release
    # createRelease = client.createRelease(organization, project, definitionId)
    # saveJson(createRelease, 'createdRelease')

    # ## Give approval
    # reassigned = client.giveApproval(organization, project, 8987, 'reassigned')

    # data = client.createReleaseDefinition(organization, project, data)

    # resp = client.createReleaseDefinition(organization, project, data)
    ## Get release definition and run for lop
    release_definition = client.getReleaseDefinition(organization, project, definitionId)
    saveJson(release_definition, 'data')
    #
    data = loadJson('data.json')


    # for i in data['environments']:
    #     if 'Stage 1' in i['name']:
    #         i['name'] = 'Stage fucker'

    # approver = loadJson('approver.json')
    # for i in data['environments']:
    #     if 'Stage 1' in i['name']:
    #         i['preDeployApprovals']['approvals'].append(approver)
    #         print(i['preDeployApprovals']['approvals'])

    # Add approval
    approver = loadJson('secondapprover.json')
    for i in data['environments']:
        if 'Stage 1' in i['name']:
            i['postDeployApprovals']['approvals'].append(approver)
            print(i['postDeployApprovals']['approvals'])



    resp = client.update_release_definition(organization, project, data)
    with open('response.json', 'w') as file:
        json.dump(resp, file, indent=2)
