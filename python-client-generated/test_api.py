import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint



# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'admin'
configuration.password = 'secret'
# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
limit = 56 # int | Limits the number of items on a page (optional)
offset = 56 # int | Specifies the page number of the artists to be displayed (optional)
try:
    api_response = api_instance.artists_get(limit=limit, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_get: %s\n" % e)



# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'admin'
configuration.password = 'secret'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Artist("Artist55", "Genre2", 4, "username55") # Artist | 

try:
    api_instance.artists_post(body)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_post: %s\n" % e)




# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'admin'
configuration.password = 'secret'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
username = 'username55' # str | 

try:
    api_response = api_instance.artists_username_get(username)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_username_get: %s\n" % e)


# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'admin'
configuration.password = 'secret'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
body = swagger_client.Artist("Name100", "Genre5", 44, "username55") # Artist | 
username = 'username55' # str | 

try:
    # Update an artist by username
    api_instance.artists_username_put(body, username)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_username_put: %s\n" % e)



# Configure HTTP basic authorization: BasicAuth
configuration = swagger_client.Configuration()
configuration.username = 'admin'
configuration.password = 'secret'

# create an instance of the API class
api_instance = swagger_client.RecordsApi(swagger_client.ApiClient(configuration))
username = 'username55' # str | 

try:
    # Delete an artist by username
    api_instance.artists_username_delete(username)
except ApiException as e:
    print("Exception when calling RecordsApi->artists_username_delete: %s\n" % e)