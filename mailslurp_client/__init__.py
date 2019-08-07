from __future__ import print_function
import time
import mailslurp_api_python_client
from mailslurp_api_python_client.rest import ApiException
from pprint import pprint

class ApiClient:

    def __init__(self, api_key):
        self.api_key = api_key

	# config api key
        configuration = mailslurp_api_python_client.Configuration()
        configuration.api_key['x-api-key'] = api_key
 
	# instantiate controllers	
	self.common_operations = mailslurp_api_python_client.CommonOperationsApi(mailslurp_api_python_client.ApiClient(configuration))
	self.extra_operations = mailslurp_api_python_client.ExtraOperationsApi(mailslurp_api_python_client.ApiClient(configuration))

    # common operations
    def create_new_email_address(self):
	return self.common_operations.create_new_email_address_using_post()

    def fetch_latest_email(self, inbox_email_address=inbox_email_address, inbox_id=inbox_id):
	return self.common_operations.fetch_latest_email_using_get(inbox_email_address=inbox_email_address, inbox_id=inbox_id)

    def send_email_simple(self, send_email_options):
	return self.common_operations.send_email_using_post(send_email_options)
