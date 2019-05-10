# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .build_step_properties_update_parameters_py3 import BuildStepPropertiesUpdateParameters


class DockerBuildStepUpdateParameters(BuildStepPropertiesUpdateParameters):
    """The properties for updating a docker build step.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Constant filled by server.
    :type type: str
    :param branch: The repository branch name.
    :type branch: str
    :param image_names: The fully qualified image names including the
     repository and tag.
    :type image_names: list[str]
    :param is_push_enabled: The value of this property indicates whether the
     image built should be pushed to the registry or not.
    :type is_push_enabled: bool
    :param no_cache: The value of this property indicates whether the image
     cache is enabled or not.
    :type no_cache: bool
    :param docker_file_path: The Docker file path relative to the source
     control root.
    :type docker_file_path: str
    :param context_path: The relative context path for a docker build in the
     source.
    :type context_path: str
    :param build_arguments: The custom arguments for building this build step.
    :type build_arguments:
     list[~azure.mgmt.containerregistry.v2018_02_01_preview.models.BuildArgument]
    :param base_image_trigger: The type of the auto trigger for base image
     dependency updates. Possible values include: 'All', 'Runtime', 'None'
    :type base_image_trigger: str or
     ~azure.mgmt.containerregistry.v2018_02_01_preview.models.BaseImageTriggerType
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'branch': {'key': 'branch', 'type': 'str'},
        'image_names': {'key': 'imageNames', 'type': '[str]'},
        'is_push_enabled': {'key': 'isPushEnabled', 'type': 'bool'},
        'no_cache': {'key': 'noCache', 'type': 'bool'},
        'docker_file_path': {'key': 'dockerFilePath', 'type': 'str'},
        'context_path': {'key': 'contextPath', 'type': 'str'},
        'build_arguments': {'key': 'buildArguments', 'type': '[BuildArgument]'},
        'base_image_trigger': {'key': 'baseImageTrigger', 'type': 'str'},
    }

    def __init__(self, *, branch: str=None, image_names=None, is_push_enabled: bool=None, no_cache: bool=None, docker_file_path: str=None, context_path: str=None, build_arguments=None, base_image_trigger=None, **kwargs) -> None:
        super(DockerBuildStepUpdateParameters, self).__init__(**kwargs)
        self.branch = branch
        self.image_names = image_names
        self.is_push_enabled = is_push_enabled
        self.no_cache = no_cache
        self.docker_file_path = docker_file_path
        self.context_path = context_path
        self.build_arguments = build_arguments
        self.base_image_trigger = base_image_trigger
        self.type = 'Docker'