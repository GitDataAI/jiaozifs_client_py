# jiaozifs_client.AuthApi

All URIs are relative to *http://localhost:34913/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_info**](AuthApi.md#get_user_info) | **GET** /users/user | get information of the currently logged-in user
[**login**](AuthApi.md#login) | **POST** /auth/login | perform a login
[**logout**](AuthApi.md#logout) | **POST** /auth/logout | perform a logout
[**refresh_token**](AuthApi.md#refresh_token) | **GET** /users/refreshtoken | refresh token for more time
[**register**](AuthApi.md#register) | **POST** /users/register | perform user registration

# **get_user_info**
> UserInfo get_user_info()

get information of the currently logged-in user

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
api_instance = jiaozifs_client.AuthApi(jiaozifs_client.ApiClient(configuration))

try:
    # get information of the currently logged-in user
    api_response = api_instance.get_user_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->get_user_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login**
> AuthenticationToken login(body=body)

perform a login

### Example
```python
from __future__ import print_function
import time
import jiaozifs_client
from jiaozifs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jiaozifs_client.AuthApi()
body = jiaozifs_client.AuthLoginBody() # AuthLoginBody |  (optional)

try:
    # perform a login
    api_response = api_instance.login(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AuthLoginBody**](AuthLoginBody.md)|  | [optional] 

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout**
> logout()

perform a logout

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
api_instance = jiaozifs_client.AuthApi(jiaozifs_client.ApiClient(configuration))

try:
    # perform a logout
    api_instance.logout()
except ApiException as e:
    print("Exception when calling AuthApi->logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[basic_auth](../README.md#basic_auth), [cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **refresh_token**
> AuthenticationToken refresh_token()

refresh token for more time

### Example
```python
from __future__ import print_function
import time
import jiaozifs_client
from jiaozifs_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: cookie_auth
configuration = jiaozifs_client.Configuration()
configuration.api_key['internal_auth_session'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['internal_auth_session'] = 'Bearer'

# create an instance of the API class
api_instance = jiaozifs_client.AuthApi(jiaozifs_client.ApiClient(configuration))

try:
    # refresh token for more time
    api_response = api_instance.refresh_token()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->refresh_token: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AuthenticationToken**](AuthenticationToken.md)

### Authorization

[cookie_auth](../README.md#cookie_auth), [jwt_token](../README.md#jwt_token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **register**
> UserInfo register(body=body)

perform user registration

### Example
```python
from __future__ import print_function
import time
import jiaozifs_client
from jiaozifs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jiaozifs_client.AuthApi()
body = jiaozifs_client.UserRegisterInfo() # UserRegisterInfo |  (optional)

try:
    # perform user registration
    api_response = api_instance.register(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->register: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserRegisterInfo**](UserRegisterInfo.md)|  | [optional] 

### Return type

[**UserInfo**](UserInfo.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

