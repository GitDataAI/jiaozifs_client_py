# jiaozifs_client.CommitApi

All URIs are relative to *http://localhost:34913/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compare_commit**](CommitApi.md#compare_commit) | **GET** /repos/{owner}/{repository}/compare/{basehead} | compare two commit
[**get_commit_changes**](CommitApi.md#get_commit_changes) | **GET** /repos/{owner}/{repository}/changes/{commit_id} | get changes in commit
[**get_entries_in_ref**](CommitApi.md#get_entries_in_ref) | **GET** /repos/{owner}/{repository}/contents | list entries in ref

# **compare_commit**
> list[Change] compare_commit(owner, repository, basehead, path=path)

compare two commit

### Example
```python
from __future__ import print_function
import time
import jiaozifs_client
from jiaozifs_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic_auth
configuration = jiaozifs_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: cookie_auth
configuration = jiaozifs_client.Configuration()
configuration.api_key['internal_auth_session'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['internal_auth_session'] = 'Bearer'

# create an instance of the API class
api_instance = jiaozifs_client.CommitApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
basehead = 'basehead_example' # str | 
path = 'path_example' # str | specific path, if not specific return entries in root (optional)

try:
    # compare two commit
    api_response = api_instance.compare_commit(owner, repository, basehead, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitApi->compare_commit: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **basehead** | **str**|  | 
 **path** | **str**| specific path, if not specific return entries in root | [optional] 

### Return type

[**list[Change]**](Change.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_commit_changes**
> list[Change] get_commit_changes(owner, repository, commit_id, path=path)

get changes in commit

### Example
```python
from __future__ import print_function
import time
import jiaozifs_client
from jiaozifs_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic_auth
configuration = jiaozifs_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: cookie_auth
configuration = jiaozifs_client.Configuration()
configuration.api_key['internal_auth_session'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['internal_auth_session'] = 'Bearer'

# create an instance of the API class
api_instance = jiaozifs_client.CommitApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
commit_id = 'commit_id_example' # str | 
path = 'path_example' # str | specific path, if not specific return entries in root (optional)

try:
    # get changes in commit
    api_response = api_instance.get_commit_changes(owner, repository, commit_id, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitApi->get_commit_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **commit_id** | **str**|  | 
 **path** | **str**| specific path, if not specific return entries in root | [optional] 

### Return type

[**list[Change]**](Change.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_entries_in_ref**
> list[FullTreeEntry] get_entries_in_ref(owner, repository, type, path=path, ref=ref, recursive=recursive, pattern=pattern)

list entries in ref

### Example
```python
from __future__ import print_function
import time
import jiaozifs_client
from jiaozifs_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: basic_auth
configuration = jiaozifs_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: cookie_auth
configuration = jiaozifs_client.Configuration()
configuration.api_key['internal_auth_session'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['internal_auth_session'] = 'Bearer'

# create an instance of the API class
api_instance = jiaozifs_client.CommitApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
type = jiaozifs_client.RefType() # RefType | type indicate to retrieve from wip/branch/tag/commit, default branch
path = 'path_example' # str | specific path, if not specific return entries in root (optional)
ref = 'ref_example' # str | specific( ref name, tag name, commit hash), for wip and branchm, branch name default to repository default branch(HEAD), (optional)
recursive = true # bool | recursive get entries (include sub files) (optional)
pattern = true # bool | pattern to get files (optional)

try:
    # list entries in ref
    api_response = api_instance.get_entries_in_ref(owner, repository, type, path=path, ref=ref, recursive=recursive, pattern=pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommitApi->get_entries_in_ref: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **type** | [**RefType**](.md)| type indicate to retrieve from wip/branch/tag/commit, default branch | 
 **path** | **str**| specific path, if not specific return entries in root | [optional] 
 **ref** | **str**| specific( ref name, tag name, commit hash), for wip and branchm, branch name default to repository default branch(HEAD), | [optional] 
 **recursive** | **bool**| recursive get entries (include sub files) | [optional] 
 **pattern** | **bool**| pattern to get files | [optional] 

### Return type

[**list[FullTreeEntry]**](FullTreeEntry.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

