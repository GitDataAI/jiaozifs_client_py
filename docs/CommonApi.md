# jiaozifs_client.CommonApi

All URIs are relative to *http://localhost:34913/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_setup_state**](CommonApi.md#get_setup_state) | **GET** /setup | check if jiaozifs setup
[**get_version**](CommonApi.md#get_version) | **GET** /version | return program and runtime version

# **get_setup_state**
> SetupState get_setup_state()

check if jiaozifs setup

### Example
```python
from __future__ import print_function
import time
import jiaozifs_client
from jiaozifs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jiaozifs_client.CommonApi()

try:
    # check if jiaozifs setup
    api_response = api_instance.get_setup_state()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_setup_state: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SetupState**](SetupState.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version**
> VersionResult get_version()

return program and runtime version

### Example
```python
from __future__ import print_function
import time
import jiaozifs_client
from jiaozifs_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = jiaozifs_client.CommonApi()

try:
    # return program and runtime version
    api_response = api_instance.get_version()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_version: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**VersionResult**](VersionResult.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

