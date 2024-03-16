# jiaozifs_client.MergerequestApi

All URIs are relative to *http://localhost:34913/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_merge_request**](MergerequestApi.md#create_merge_request) | **POST** /repos/{owner}/{repository}/mergerequest | create merge request
[**get_merge_request**](MergerequestApi.md#get_merge_request) | **GET** /repos/{owner}/{repository}/mergerequest/{mrSeq} | get merge request
[**list_merge_requests**](MergerequestApi.md#list_merge_requests) | **GET** /repos/{owner}/{repository}/mergerequest | get list of merge request in repository
[**merge**](MergerequestApi.md#merge) | **POST** /repos/{owner}/{repository}/mergerequest/{mrSeq}/merge | merge a mergerequest
[**update_merge_request**](MergerequestApi.md#update_merge_request) | **POST** /repos/{owner}/{repository}/mergerequest/{mrSeq} | update merge request

# **create_merge_request**
> MergeRequest create_merge_request(body, owner, repository)

create merge request

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
api_instance = jiaozifs_client.MergerequestApi(jiaozifs_client.ApiClient(configuration))
body = jiaozifs_client.CreateMergeRequest() # CreateMergeRequest | 
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 

try:
    # create merge request
    api_response = api_instance.create_merge_request(body, owner, repository)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergerequestApi->create_merge_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateMergeRequest**](CreateMergeRequest.md)|  | 
 **owner** | **str**|  | 
 **repository** | **str**|  | 

### Return type

[**MergeRequest**](MergeRequest.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_merge_request**
> MergeRequestFullState get_merge_request(owner, repository, mr_seq)

get merge request

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
api_instance = jiaozifs_client.MergerequestApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
mr_seq = 56 # int | 

try:
    # get merge request
    api_response = api_instance.get_merge_request(owner, repository, mr_seq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergerequestApi->get_merge_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **mr_seq** | **int**|  | 

### Return type

[**MergeRequestFullState**](MergeRequestFullState.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_merge_requests**
> MergeRequestList list_merge_requests(owner, repository, after=after, amount=amount, state=state)

get list of merge request in repository

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
api_instance = jiaozifs_client.MergerequestApi(jiaozifs_client.ApiClient(configuration))
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
after = 789 # int | return items after this value (optional)
amount = 100 # int | how many items to return (optional) (default to 100)
state = 56 # int |  (optional)

try:
    # get list of merge request in repository
    api_response = api_instance.list_merge_requests(owner, repository, after=after, amount=amount, state=state)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergerequestApi->list_merge_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **after** | **int**| return items after this value | [optional] 
 **amount** | **int**| how many items to return | [optional] [default to 100]
 **state** | **int**|  | [optional] 

### Return type

[**MergeRequestList**](MergeRequestList.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **merge**
> list[Commit] merge(body, owner, repository, mr_seq)

merge a mergerequest

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
api_instance = jiaozifs_client.MergerequestApi(jiaozifs_client.ApiClient(configuration))
body = jiaozifs_client.MergeMergeRequest() # MergeMergeRequest | 
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
mr_seq = 56 # int | 

try:
    # merge a mergerequest
    api_response = api_instance.merge(body, owner, repository, mr_seq)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MergerequestApi->merge: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MergeMergeRequest**](MergeMergeRequest.md)|  | 
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **mr_seq** | **int**|  | 

### Return type

[**list[Commit]**](Commit.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_merge_request**
> update_merge_request(body, owner, repository, mr_seq)

update merge request

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
api_instance = jiaozifs_client.MergerequestApi(jiaozifs_client.ApiClient(configuration))
body = jiaozifs_client.UpdateMergeRequest() # UpdateMergeRequest | 
owner = 'owner_example' # str | 
repository = 'repository_example' # str | 
mr_seq = 56 # int | 

try:
    # update merge request
    api_instance.update_merge_request(body, owner, repository, mr_seq)
except ApiException as e:
    print("Exception when calling MergerequestApi->update_merge_request: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateMergeRequest**](UpdateMergeRequest.md)|  | 
 **owner** | **str**|  | 
 **repository** | **str**|  | 
 **mr_seq** | **int**|  | 

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

