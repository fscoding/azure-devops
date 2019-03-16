def update_release_approval(self, approval, project, approval_id):
        """UpdateReleaseApproval.
        Update status of an approval
        :param :class:`<ReleaseApproval> <azure.devops.v5_0.release.models.ReleaseApproval>` approval: ReleaseApproval object having status, approver and comments.
        :param str project: Project ID or project name
        :param int approval_id: Id of the approval.
        :rtype: :class:`<ReleaseApproval> <azure.devops.v5_0.release.models.ReleaseApproval>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if approval_id is not None:
            route_values['approvalId'] = self._serialize.url('approval_id', approval_id, 'int')
        content = self._serialize.body(approval, 'ReleaseApproval')
        response = self._send(http_method='PATCH',
                              location_id='9328e074-59fb-465a-89d9-b09c82ee5109',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseApproval', response)




def create_release_definition(self, release_definition, project):
        """CreateReleaseDefinition.
        Create a release definition
        :param :class:`<ReleaseDefinition> <azure.devops.v5_0.release.models.ReleaseDefinition>` release_definition: release definition object to create.
        :param str project: Project ID or project name
        :rtype: :class:`<ReleaseDefinition> <azure.devops.v5_0.release.models.ReleaseDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(release_definition, 'ReleaseDefinition')
        response = self._send(http_method='POST',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseDefinition', response)


def create_release_definition(self, release_definition, project):
        """CreateReleaseDefinition.
        Create a release definition
        :param :class:`<ReleaseDefinition> <azure.devops.v5_0.release.models.ReleaseDefinition>` release_definition: release definition object to create.
        :param str project: Project ID or project name
        :rtype: :class:`<ReleaseDefinition> <azure.devops.v5_0.release.models.ReleaseDefinition>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(release_definition, 'ReleaseDefinition')
        response = self._send(http_method='POST',
                              location_id='d8f96f24-8ea7-4cb6-baab-2df8fc515665',
                              version='5.0',
                              route_values=route_values,
                              content=content)
        return self._deserialize('ReleaseDefinition', response)