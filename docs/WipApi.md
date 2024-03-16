# jiaozifs_client.WipApi

All URIs are relative to *http://localhost:34913/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**commit_wip**](WipApi.md#commit_wip) | **POST** /wip/{owner}/{repository}/commit | commit working in process to branch
[**delete_wip**](WipApi.md#delete_wip) | **DELETE** /wip/{owner}/{repository} | remove working in process
[**get_wip**](WipApi.md#get_wip) | **GET** /wip/{owner}/{repository} | get working in process
[**get_wip_changes**](WipApi.md#get_wip_changes) | **GET** /wip/{owner}/{repository}/changes | get working in process changes
[**list_wip**](WipApi.md#list_wip) | **GET** /wip/{owner}/{repository}/list | list wip in specific project and user
[**revert_wip_changes**](WipApi.md#revert_wip_changes) | **POST** /wip/{owner}/{repository}/revert | revert changes in working in process, empty path will revert all
[**update_wip**](WipApi.md#update_wip) | **POST** /wip/{owner}/{repository} | update wip

# **commit_wip**
> Wip commit_wip(owner, repository, ref_name, msg)

commit working in process to branch

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
api_instance = jiaozifs_client.WipApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
ref_name = 'ref_name_example' # str | ref name
msg = 'msg_example' # str | commit message

try:
    # commit working in process to branch
    api_response = api_instance.commit_wip(owner, repository, ref_name, msg)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WipApi->commit_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **ref_name** | **str**| ref name | 
 **msg** | **str**| commit message | 

### Return type

[**Wip**](Wip.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_wip**
> delete_wip(repository, owner, ref_name)

remove working in process

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
api_instance = jiaozifs_client.WipApi(jiaozifs_client.ApiClient(configuration))
repository = 'repository_example' # str | 
owner = 'owner_example' # str | 
ref_name = 'ref_name_example' # str | ref name

try:
    # remove working in process
    api_instance.delete_wip(repository, owner, ref_name)
except ApiException as e:
    print("Exception when calling WipApi->delete_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**|  | 
 **owner** | **str**|  | 
 **ref_name** | **str**| ref name | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wip**
> Wip get_wip(repository, owner, ref_name)

get working in process

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
api_instance = jiaozifs_client.WipApi(jiaozifs_client.ApiClient(configuration))
repository = 'repository_example' # str | 
owner = 'owner_example' # str | 
ref_name = 'ref_name_example' # str | ref name

try:
    # get working in process
    api_response = api_instance.get_wip(repository, owner, ref_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WipApi->get_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**|  | 
 **owner** | **str**|  | 
 **ref_name** | **str**| ref name | 

### Return type

[**Wip**](Wip.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_wip_changes**
> list[Change] get_wip_changes(owner, repository, ref_name, path=path)

get working in process changes

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
api_instance = jiaozifs_client.WipApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
ref_name = 'ref_name_example' # str | ref name
path = 'path_example' # str | path (optional)

try:
    # get working in process changes
    api_response = api_instance.get_wip_changes(owner, repository, ref_name, path=path)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WipApi->get_wip_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **ref_name** | **str**| ref name | 
 **path** | **str**| path | [optional] 

### Return type

[**list[Change]**](Change.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_wip**
> list[Wip] list_wip(owner, repository)

list wip in specific project and user

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
api_instance = jiaozifs_client.WipApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 

try:
    # list wip in specific project and user
    api_response = api_instance.list_wip(owner, repository)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WipApi->list_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 

### Return type

[**list[Wip]**](Wip.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revert_wip_changes**
> revert_wip_changes(repository, owner, ref_name, path_prefix=path_prefix)

revert changes in working in process, empty path will revert all

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
api_instance = jiaozifs_client.WipApi(jiaozifs_client.ApiClient(configuration))
repository = 'repository_example' # str | 
owner = 'owner_example' # str | 
ref_name = 'ref_name_example' # str | ref name
path_prefix = 'path_prefix_example' # str | prefix of path (optional)

try:
    # revert changes in working in process, empty path will revert all
    api_instance.revert_wip_changes(repository, owner, ref_name, path_prefix=path_prefix)
except ApiException as e:
    print("Exception when calling WipApi->revert_wip_changes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository** | **str**|  | 
 **owner** | **str**|  | 
 **ref_name** | **str**| ref name | 
 **path_prefix** | **str**| prefix of path | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_wip**
> update_wip(body, ref_name, repository, owner)

update wip

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
api_instance = jiaozifs_client.WipApi(jiaozifs_client.ApiClient(configuration))
body = jiaozifs_client.UpdateWip() # UpdateWip | 
ref_name = 'ref_name_example' # str | ref name
repository = 'repository_example' # str | 
owner = 'owner_example' # str | 

try:
    # update wip
    api_instance.update_wip(body, ref_name, repository, owner)
except ApiException as e:
    print("Exception when calling WipApi->update_wip: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateWip**](UpdateWip.md)|  | 
 **ref_name** | **str**| ref name | 
 **repository** | **str**|  | 
 **owner** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

