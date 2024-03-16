# jiaozifs_client.MemberApi

All URIs are relative to *http://localhost:34913/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invite_member**](MemberApi.md#invite_member) | **POST** /repos/{owner}/{repository}/member/invite | invite member
[**revoke_member**](MemberApi.md#revoke_member) | **DELETE** /repos/{owner}/{repository}/member | Revoke member in repository
[**update_member_group**](MemberApi.md#update_member_group) | **POST** /repos/{owner}/{repository}/member | update member by user id and change group role

# **invite_member**
> invite_member(owner, repository, user_id, group_id)

invite member

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
api_instance = jiaozifs_client.MemberApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # invite member
    api_instance.invite_member(owner, repository, user_id, group_id)
except ApiException as e:
    print("Exception when calling MemberApi->invite_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **user_id** | [**str**](.md)|  | 
 **group_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revoke_member**
> revoke_member(owner, repository, user_id)

Revoke member in repository

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
api_instance = jiaozifs_client.MemberApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # Revoke member in repository
    api_instance.revoke_member(owner, repository, user_id)
except ApiException as e:
    print("Exception when calling MemberApi->revoke_member: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **user_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_member_group**
> update_member_group(owner, repository, user_id, group_id)

update member by user id and change group role

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
api_instance = jiaozifs_client.MemberApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
user_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 
group_id = '38400000-8cf0-11bd-b23e-10b96e4ef00d' # str | 

try:
    # update member by user id and change group role
    api_instance.update_member_group(owner, repository, user_id, group_id)
except ApiException as e:
    print("Exception when calling MemberApi->update_member_group: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **user_id** | [**str**](.md)|  | 
 **group_id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

