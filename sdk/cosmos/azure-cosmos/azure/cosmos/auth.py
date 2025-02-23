﻿#The MIT License (MIT)
#Copyright (c) 2014 Microsoft Corporation

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

"""Authorization helper functions in the Azure Cosmos database service.
"""

from hashlib import sha256
import hmac
import six
import base64

from . import http_constants

def GetAuthorizationHeader(cosmos_client_connection,
                           verb,
                           path,
                           resource_id_or_fullname,
                           is_name_based,
                           resource_type,
                           headers):
    """Gets the authorization header.

    :param cosmos_client_connection.CosmosClient cosmos_client:
    :param str verb:
    :param str path:
    :param str resource_id_or_fullname:
    :param str resource_type:
    :param dict headers:

    :return:
        The authorization headers.
    :rtype: dict
    """
    # In the AuthorizationToken generation logic, lower casing of ResourceID is required as rest of the fields are lower cased
    # Lower casing should not be done for named based "ID", which should be used as is
    if resource_id_or_fullname is not None and not is_name_based:
        resource_id_or_fullname = resource_id_or_fullname.lower()

    if cosmos_client_connection.master_key:
        return __GetAuthorizationTokenUsingMasterKey(verb,
                                                    resource_id_or_fullname,
                                                    resource_type,
                                                    headers,
                                                    cosmos_client_connection.master_key)
    elif cosmos_client_connection.resource_tokens:
        return __GetAuthorizationTokenUsingResourceTokens(
            cosmos_client_connection.resource_tokens, path, resource_id_or_fullname)




def __GetAuthorizationTokenUsingMasterKey(verb,
                                         resource_id_or_fullname,
                                         resource_type,
                                         headers,
                                         master_key):
    """Gets the authorization token using `master_key.

    :param str verb:
    :param str resource_id_or_fullname:
    :param str resource_type:
    :param dict headers:
    :param str master_key:

    :return:
        The authorization token.
    :rtype: dict

    """


    # decodes the master key which is encoded in base64    
    key = base64.b64decode(master_key)
    
    # Skipping lower casing of resource_id_or_fullname since it may now contain "ID" of the resource as part of the fullname
    text = '{verb}\n{resource_type}\n{resource_id_or_fullname}\n{x_date}\n{http_date}\n'.format(
        verb=(verb.lower() or ''),
        resource_type=(resource_type.lower() or ''),
        resource_id_or_fullname=(resource_id_or_fullname or ''),
        x_date=headers.get(http_constants.HttpHeaders.XDate, '').lower(),
        http_date=headers.get(http_constants.HttpHeaders.HttpDate, '').lower())
   
    if six.PY2:
        body = text.decode('utf-8')
        digest = hmac.new(key, body, sha256).digest()
        signature = digest.encode('base64')
    else:
        # python 3 support
        body = text.encode('utf-8')
        digest = hmac.new(key, body, sha256).digest()
        signature = base64.encodebytes(digest).decode('utf-8')

    master_token = 'master'
    token_version = '1.0'
    return  'type={type}&ver={ver}&sig={sig}'.format(type=master_token,
                                                    ver=token_version,
                                                    sig=signature[:-1])

def __GetAuthorizationTokenUsingResourceTokens(resource_tokens,
                                              path,
                                              resource_id_or_fullname):
    """Get the authorization token using `resource_tokens`.

    :param dict resource_tokens:
    :param str path:
    :param str resource_id_or_fullname:

    :return:
        The authorization token.
    :rtype: dict

    """
    if resource_tokens and len(resource_tokens) > 0:
        # For database account access(through GetDatabaseAccount API), path and resource_id_or_fullname are '', 
        # so in this case we return the first token to be used for creating the auth header as the service will accept any token in this case
        if not path and not resource_id_or_fullname:
            return next(six.itervalues(resource_tokens))

        if resource_tokens.get(resource_id_or_fullname):
            return resource_tokens[resource_id_or_fullname]
        else:
            path_parts = []
            if path:
                path_parts = path.split('/')
            resource_types = ['dbs', 'colls', 'docs', 'sprocs', 'udfs', 'triggers',
                              'users', 'permissions', 'attachments', 'media',
                              'conflicts', 'offers']
            # Get the last resource id or resource name from the path and get it's token from resource_tokens
            for one_part in reversed(path_parts):
                if not one_part in resource_types and one_part in resource_tokens:
                    return resource_tokens[one_part]
    return None