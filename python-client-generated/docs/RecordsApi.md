# swagger_client.RecordsApi

All URIs are relative to *http://localhost:8080*

Method | HTTP request | Description
------------- | ------------- | -------------
[**artists_get**](RecordsApi.md#artists_get) | **GET** /artists | 
[**artists_post**](RecordsApi.md#artists_post) | **POST** /artists | 
[**artists_username_delete**](RecordsApi.md#artists_username_delete) | **DELETE** /artists/{username} | Delete an artist by username
[**artists_username_get**](RecordsApi.md#artists_username_get) | **GET** /artists/{username} | 
[**artists_username_put**](RecordsApi.md#artists_username_put) | **PUT** /artists/{username} | Update an artist by username

# **artists_get**
> list[Artist] artists_get(limit=limit, offset=offset)



Returns a list of artists

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Limits the number of items on a page (optional)
offset = 56 # int | Specifies the page number of the artists to be displayed (optional)

try:
    api_response = api_instance.artists_get(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**| Limits the number of items on a page | [optional] 
 **offset** | **int**| Specifies the page number of the artists to be displayed | [optional] 

### Return type

[**list[Artist]**](Artist.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artists_post**
> artists_post(body)



Lets a user post a new artist

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Artist() # Artist | 

try:
    api_instance.artists_post(body)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Artist**](Artist.md)|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artists_username_delete**
> artists_username_delete(username)

Delete an artist by username

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | 

try:
    # Delete an artist by username
    api_instance.artists_username_delete(username)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_username_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artists_username_get**
> Artist artists_username_get(username)



Obtain information about an artist from his or her unique username

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
username = 'username_example' # str | 

try:
    api_response = api_instance.artists_username_get(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_username_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **username** | **str**|  | 

### Return type

[**Artist**](Artist.md)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **artists_username_put**
> artists_username_put(body, username)

Update an artist by username

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint
# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Artist() # Artist | 
username = 'username_example' # str | 

try:
    # Update an artist by username
    api_instance.artists_username_put(body, username)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_username_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Artist**](Artist.md)|  | 
 **username** | **str**|  | 

### Return type

void (empty response body)

### Authorization

[BasicAuth](../README.md#BasicAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

