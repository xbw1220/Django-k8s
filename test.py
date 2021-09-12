from __future__ import print_function
import time
import kubernetes.client
from kubernetes.client.rest import ApiException
from pprint import pprint

configuration = kubernetes.client.Configuration()
configuration.verify_ssl = False
# Configure API key authorization: BearerToken
configuration.api_key['authorization'] = r'C:\Users\xbw12\PycharmProjects\k8s\ca.key'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['authorization'] = 'Bearer'

# Defining host is optional and default to http://localhost
configuration.host = "https://192.168.100.10:6443"

# Defining host is optional and default to http://localhost
configuration.host = "https://192.168.100.10:6443"
# Enter a context with an instance of the API kubernetes.client
with kubernetes.client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = kubernetes.client.AdmissionregistrationApi(api_client)

    try:
        api_response = api_instance.get_api_group()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AdmissionregistrationApi->get_api_group: %s\n" % e)