import requests
import json
import random
import string
import re
import time

# Class containing core calls for validations


class CoreCalls():
	def __init__(self, core_services_url, system_id, user, password):
		self.core_services_url = core_services_url
		self.system_id = system_id
		self.user = user
		self.password = password

	def random_char(self):
		random_email = ''.join(random.choice(string.ascii_letters) for _ in range(10))
		return random_email

	def call_regex(self, url):
		flip = url[::-1]
		end = flip.find("/") 
		substring = flip[:end]
		flip_back = substring[::-1]
		return flip_back

	def create_subscriber(self):
		random_email = self.random_char()
		url = f"{self.core_services_url}/Subscriber/CreateSubscriber"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		# print(response)
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		subid = response_dict.get('Subscriber')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			exit()
		elif subid is None:
			raise KeyError(f"Failed {api}: No Subscriber object in response")
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			exit()
		else:
			returned_dict = dict()
			returned_dict['SubscriberId'] = response_dict['Subscriber']['Id']
			returned_dict['Login'] = response_dict['Subscriber']['Login']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def retrieve_subscriber(self, subscriber_id):
		url = f"{self.core_services_url}/SubscriberManagement/RetrieveSubscriber"

		payload = "{}"
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}",
		  'Content-Type': 'text/plain'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		# print(response)
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")
			return response_dict

	def update_subscriber(self, subscriber_id, body):
		url = f"{self.core_services_url}/SubscriberManagement/UpdateSubscriber"

		payload = json.dumps(body)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}",
		  'Content-Type': 'text/plain'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		# print(response)
		fault = response_dict.get('Fault')
		api = self.call_regex(url)
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def create_session(self, login):
		url = f"{self.core_services_url}/Subscriber/CreateSession"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-Language': 'en-US',
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(login)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(login)
			exit()
		else:
			returned_dict = dict()
			returned_dict['SessionId'] = response_dict['SessionId']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def create_address(self, session_id, subscriber_id):
		url = f"{self.core_services_url}/Subscriber/CreateAddress"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-SessionId': f"{session_id['SessionId']}",
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			returned_dict = dict()
			returned_dict['Address'] = response_dict['Address']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def register_device(self, session_id, subscriber_id):
		url = f"{self.core_services_url}/Subscriber/RegisterDevice"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-SessionId': f"{session_id['SessionId']}",
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			returned_dict = dict()
			returned_dict['DeviceId'] = response_dict['PhysicalDevice']['DeviceId']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def create_payment_instrument(self, address, subscriber_id):
		url = f"{self.core_services_url}/SubscriberManagement/CreatePaymentInstrument"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}",
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			returned_dict = dict()
			returned_dict['PaymentInstrumentId'] = response_dict['PaymentInstrument']['Id']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def retrieve_payment_instrument(self, subscriber_id, payment_instrument_id):
		url = f"{self.core_services_url}/SubscriberManagement/RetrievePaymentInstrument"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}",
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		fault = response_dict.get('Fault')
		api = self.call_regex(url)
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def create_product(self, subscriber_id):
		url = f"{self.core_services_url}/Catalog/CreateProductUsingTemplate"

		payload = json.dumps(<body>)
		headers = {
		  'cd-systemid': f'{self.system_id}',
		  'cd-language': 'en-US',
		  'content-type': 'application/json;charset=UTF-8',
		  'cd-user': f'{self.user}',
		  'cd-password': f'{self.password}'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			returned_dict = dict()
			returned_dict['ProductId'] = response_dict['Product']['Id']['Value']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def retrieve_product(self, product_id, subscriber_id):
		url = f"{self.core_services_url}/Catalog/RetrieveProduct"

		payload = json.dumps(<body>)

		headers = {
		  'cd-systemid': f'{self.system_id}',
		  'cd-language': 'en-US',
		  'content-type': 'application/json;charset=UTF-8',
		  'cd-user': f'{self.user}',
		  'cd-password': f'{self.password}'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def update_product_status(self, product_id, subscriber_id):
		url = f"{self.core_services_url}/Catalog/UpdateProductStatus"

		payload = json.dumps(<body>)
		headers = {
		  'cd-systemid': f'{self.system_id}',
		  'cd-language': 'en-US',
		  # 'content-type': 'application/json;charset=UTF-8',
		  'cd-user': f'{self.user}',
		  'cd-password': f'{self.password}'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def search_segments(self, subscriber_id):
		url = f"{self.core_services_url}/Catalog/SearchSegments"

		payload = json.dumps(<body>)
		headers = {
		  'cd-systemid': f'{self.system_id}',
		  'cd-jsonlongasstring': 'true',
		  'cd-language': 'en-US',
		  'accept-language': 'en-US,en;q=0.9',
		  'cd-user': f'{self.user}',
		  'cd-password': f'{self.password}',
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			returned_dict = dict()
			returned_dict['SegmentId'] = response_dict['Segments'][0]['Id']['Value']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def create_pricing_plan(self, product_id, segment_id, subscriber_id):
		url = f"{self.core_services_url}/Catalog/CreatePricingPlanUsingTemplate"

		payload = json.dumps(<body>)
		headers = {
		  'cd-systemid': f'{self.system_id}',
		  'cd-jsonlongasstring': 'true',
		  'cd-language': 'en-US',
		  'cd-user': f'{self.user}',
		  'cd-password': f'{self.password}',
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			returned_dict = dict()
			returned_dict['PricingPlanId'] = response_dict['PricingPlan']['Id']['Value']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def update_pricing_plan_status(self, pricing_plan_id, subscriber_id):
		url = f"{self.core_services_url}/Catalog/UpdatePricingPlanStatus"

		payload = json.dumps(<body>)
		headers = {
		  'cd-systemid': f'{self.system_id}',
		  'cd-language': 'en-US',
		  'cd-user': f'{self.user}',
		  'cd-password': f'{self.password}'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def retrieve_pricing_plan(self, pricing_plan_id, subscriber_id):
		url = f"{self.core_services_url}/Catalog/RetrievePricingPlan"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'Content-Type': 'application/json'
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def create_entitlement(self, product_id, pricing_plan_id, subscriber_id):
		url = f"{self.core_services_url}/SubscriberManagement/CreateEntitlements"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'Content-Type': 'application/json',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}"
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def remove_entitlements(self, locker_item_id, subscriber_id):
		url = f"{self.core_services_url}/SubscriberManagement/RemoveEntitlements"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'Content-Type': 'application/json',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}"
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def search_locker(self, subscriber_id):
		url = f"{self.core_services_url}/SubscriberManagement/SearchLocker"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'Content-Type': 'application/json',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}"
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			returned_dict = dict()
			returned_dict['LockerItemId'] = response_dict['LockerItems'][0]['Id']
			print(f"Successful {api}: {response.elapsed}")
			return returned_dict

	def submit_order(self, product_id, pricing_plan_id, subscriber_id):
		url = f"{self.core_services_url}/SubscriberManagement/SubmitOrder"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'Content-Type': 'application/json',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}"
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def submit_remove_order(self, product_id, subscriber_id):
		url = f"{self.core_services_url}/SubscriberManagement/SubmitRemoveOrder"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'Content-Type': 'application/json',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}"
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		api = self.call_regex(url)
		fault = response_dict.get('Fault')
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			self.anonymize_subscriber(subscriber_id)
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def anonymize_subscriber(self, subscriber_id):
		url = f"{self.core_services_url}/SubscriberManagement/AnonymizeSubscriber"

		payload = json.dumps(<body>)
		headers = {
		  'CD-SystemId': f'{self.system_id}',
		  'CD-JsonLongAsString': 'true',
		  'Content-Type': 'application/json',
		  'CD-User': f'{self.user}',
		  'CD-Password': f'{self.password}',
		  'CD-SubscriberId': f"{subscriber_id['SubscriberId']}"
		}

		response = requests.request("POST", url, headers=headers, data=payload)
		response_dict = response.json()
		returned_dict = dict()
		# print(response)
		fault = response_dict.get('Fault')
		api = self.call_regex(url)
		if fault is not None:
			print(f"Failed {api}: {response_dict['Fault']}")
			exit()
		elif response.status_code != 200:
			print(f"Failed {api} with: {response.status_code} | {response}")
			exit()
		else:
			print(f"Successful {api}: {response.elapsed}")

	def execute_validation(self):
		create_subscriber = self.create_subscriber()
		retrieve_subscriber = self.retrieve_subscriber(create_subscriber)
		self.update_subscriber(create_subscriber, retrieve_subscriber)
		create_session = self.create_session(create_subscriber)
		create_address = self.create_address(create_session, create_subscriber)
		register_device = self.register_device(create_session, create_subscriber)
		create_payment_instrument = self.create_payment_instrument(create_address, create_subscriber)
		self.retrieve_payment_instrument(create_subscriber, create_payment_instrument)
		create_product = self.create_product(create_subscriber)
		self.retrieve_product(create_product, create_subscriber)
		search_segments = self.search_segments(create_subscriber)	
		create_pricing_plan = self.create_pricing_plan(create_product, search_segments, create_subscriber)
		self.retrieve_pricing_plan(create_pricing_plan, create_subscriber)
		self.create_entitlement(create_product, create_pricing_plan, create_subscriber)
		search_locker = self.search_locker(create_subscriber)
		self.remove_entitlements(search_locker, create_subscriber)
		self.submit_order(create_product, create_pricing_plan, create_subscriber)
		time.sleep(2)
		self.submit_remove_order(create_product, create_subscriber)
		time.sleep(2)
		self.update_product_status(create_product, create_subscriber)
		self.update_pricing_plan_status(create_pricing_plan, create_subscriber)	
		self.anonymize_subscriber(create_subscriber)

