import * as azdev from "azure-devops-node-api";
import * as ba from "azure-devops-node-api/ReleaseApi";
import { ReleaseDefinition, ReleaseDefinitionEnvironment } from "azure-devops-node-api/interfaces/ReleaseInterfaces";

// your collection url
let orgUrlPrefix = "https://dev.azure.com/";

// ideally from config
let organization: string = "slb-swt"
let token: string = "rhmvmgrczohytlwnyusanbwzid25uaaie7acnqwe35docpdp4ega";
let vstsProject: string = "assetops"
let vstsReleaseDefinitionName = "New release pipeline"

let authHandler = azdev.getPersonalAccessTokenHandler(token);
let connection = new azdev.WebApi(orgUrlPrefix + organization, authHandler);

async function list_stages() {
    let release: ba.IReleaseApi = await connection.getReleaseApi();
    let rDefs: ReleaseDefinition[] = await release.getReleaseDefinitions(vstsProject);
    let releaseId = rDefs.find(d => d.name === vstsReleaseDefinitionName).id;
    let releaseDefinition: ReleaseDefinition = await release.getReleaseDefinition(vstsProject, releaseId);
    releaseDefinition.environments.forEach(e => {
        console.log(e.name)
    })
}


async function add_stage() {
    let release: ba.IReleaseApi = await connection.getReleaseApi();
    let rDefs: ReleaseDefinition[] = await release.getReleaseDefinitions(vstsProject);
    let releaseId = rDefs.find(d => d.name === vstsReleaseDefinitionName).id;
    let releaseDefinition: ReleaseDefinition = await release.getReleaseDefinition(vstsProject, releaseId);
    let env0: ReleaseDefinitionEnvironment = JSON.parse(JSON.stringify(releaseDefinition.environments[0]));
    env0.name = "hohoho";
    env0.rank++;
    env0.id = 0;
    releaseDefinition.environments.push(env0);
    await release.updateReleaseDefinition(releaseDefinition, vstsProject);
}

// list_stages();
add_stage();

// var arr = [1, 2];
// console.log(arr)
// console.log(arr.slice(1));
