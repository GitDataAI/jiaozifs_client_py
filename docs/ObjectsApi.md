# jiaozifs_client.ObjectsApi

All URIs are relative to *http://localhost:34913/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_object**](ObjectsApi.md#delete_object) | **DELETE** /object/{owner}/{repository} | delete object. Missing objects will not return a NotFound error.
[**get_files**](ObjectsApi.md#get_files) | **GET** /object/{owner}/{repository}/files | get files by pattern
[**get_object**](ObjectsApi.md#get_object) | **GET** /object/{owner}/{repository} | get object content
[**head_object**](ObjectsApi.md#head_object) | **HEAD** /object/{owner}/{repository} | check if object exists
[**upload_object**](ObjectsApi.md#upload_object) | **POST** /object/{owner}/{repository} | 

# **delete_object**
> delete_object(owner, repository, ref_name, path)

delete object. Missing objects will not return a NotFound error.

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
api_instance = jiaozifs_client.ObjectsApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
ref_name = 'ref_name_example' # str | branch/tag to the ref
path = 'path_example' # str | relative to the ref

try:
    # delete object. Missing objects will not return a NotFound error.
    api_instance.delete_object(owner, repository, ref_name, path)
except ApiException as e:
    print("Exception when calling ObjectsApi->delete_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **ref_name** | **str**| branch/tag to the ref | 
 **path** | **str**| relative to the ref | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_files**
> list[str] get_files(owner, repository, ref_name, type, pattern=pattern)

get files by pattern

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
api_instance = jiaozifs_client.ObjectsApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
ref_name = 'ref_name_example' # str | branch/tag to the ref
type = jiaozifs_client.RefType() # RefType | files to retrieve from wip/branch/tag/commit, default branch
pattern = 'pattern_example' # str | glob pattern for match file path (optional)

try:
    # get files by pattern
    api_response = api_instance.get_files(owner, repository, ref_name, type, pattern=pattern)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_files: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **ref_name** | **str**| branch/tag to the ref | 
 **type** | [**RefType**](.md)| files to retrieve from wip/branch/tag/commit, default branch | 
 **pattern** | **str**| glob pattern for match file path | [optional] 

### Return type

**list[str]**

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_object**
> str get_object(owner, repository, ref_name, path, type, range=range)

get object content

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
api_instance = jiaozifs_client.ObjectsApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
ref_name = 'ref_name_example' # str | branch/tag to the ref
path = 'path_example' # str | relative to the ref
type = jiaozifs_client.RefType() # RefType | type indicate to retrieve from wip/branch/tag, default branch
range = 'range_example' # str | Byte range to retrieve (optional)

try:
    # get object content
    api_response = api_instance.get_object(owner, repository, ref_name, path, type, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->get_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **ref_name** | **str**| branch/tag to the ref | 
 **path** | **str**| relative to the ref | 
 **type** | [**RefType**](.md)| type indicate to retrieve from wip/branch/tag, default branch | 
 **range** | **str**| Byte range to retrieve | [optional] 

### Return type

**str**

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **head_object**
> head_object(owner, repository, ref_name, path, type, range=range)

check if object exists

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
api_instance = jiaozifs_client.ObjectsApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
ref_name = 'ref_name_example' # str | branch/tag to the ref
path = 'path_example' # str | relative to the ref
type = jiaozifs_client.RefType() # RefType | type indicate to retrieve from wip/branch/tag, default branch
range = 'range_example' # str | Byte range to retrieve (optional)

try:
    # check if object exists
    api_instance.head_object(owner, repository, ref_name, path, type, range=range)
except ApiException as e:
    print("Exception when calling ObjectsApi->head_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **ref_name** | **str**| branch/tag to the ref | 
 **path** | **str**| relative to the ref | 
 **type** | [**RefType**](.md)| type indicate to retrieve from wip/branch/tag, default branch | 
 **range** | **str**| Byte range to retrieve | [optional] 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_object**
> ObjectStats upload_object(ref_name, path, owner, repository, content=content, is_replace=is_replace)



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
api_instance = jiaozifs_client.ObjectsApi(jiaozifs_client.ApiClient(configuration))
ref_name = 'ref_name_example' # str | branch/tag to the ref
path = 'path_example' # str | relative to the ref
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
content = 'content_example' # str |  (optional)
is_replace = true # bool | indicate to replace existing object or not (optional)

try:
    api_response = api_instance.upload_object(ref_name, path, owner, repository, content=content, is_replace=is_replace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ObjectsApi->upload_object: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ref_name** | **str**| branch/tag to the ref | 
 **path** | **str**| relative to the ref | 
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **content** | **str**|  | [optional] 
 **is_replace** | **bool**| indicate to replace existing object or not | [optional] 

### Return type

[**ObjectStats**](ObjectStats.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: multipart/form-data, application/octet-stream
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

