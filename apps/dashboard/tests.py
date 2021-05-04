
from django.test import TestCase, Client
from django.urls import reverse
from .models import Employee,Asset,AssetAssign,Designation,Category
from rest_framework.test import APIClient
from rest_framework import status
from rest_framework import status
from rest_framework import serializers
	

#..........................api...................

# class TestEmployeeViews(TestCase):
#     def test_employee_view_GET(self):
#         client = Client()
#         response = client.get(reverse('dashboard:view_employee'))
#         self.assertEqual(response.status_code,200)
#         # self.assertTemplateUsed(response,'dashboard/employee_list.html')

class EmployeeTestCase(TestCase):
	def setUp(self):
		# """Define the test client and other test variables."""
		self.client = APIClient()
		self.designation_data={'name':'php developer'}
		self.employee_data = {"id":1,"name": "poornima","email": "poornima@gmail.com","phone": "123456789","address": "indore", "designation": 1}
		self.response = self.client.post(
			reverse('api_designation_create'),
			self.designation_data,
			format="json")
		self.response = self.client.post(
			reverse('api_employee_create'),
			self.employee_data,
			format="json")
	
	def test_01_api_can_create_a_employeelist(self):
	#     """Test the api has employee creation capability."""
		response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
	

	def test_02_api_can_get_a_employeelist(self):
		# """Test the api can get a given bucketlist."""
		employeelist = Employee.objects.last()
		response = self.client.get(reverse('api_employee_list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, employeelist)
	

	def test_03_api_can_update_employeelist(self):
		employeelist = Employee.objects.last()
		self.employee_data = {"id":1,"name": "poornima","email": "poornima@gmail.com","phone": "123456789","address": "indore", "designation": 1}
		response = self.client.put(
			reverse('api_employee_update', kwargs={'pk':employeelist.id}),self.employee_data,
			 format='json'
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	
	def test_04_api_can_delete_employeelist(self):
		employeelist = Employee.objects.last()
		response = self.client.delete(
			reverse('api_employee_delete', kwargs={'pk':employeelist.id}),self.employee_data,
			 format='json'
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)



class AssetTestCase(TestCase):
	def setUp(self):
		# """Define the test client and other test variables."""
		self.client = APIClient()
		self.category_data={'name':'electronics'}
		self.asset_data =    {
		"id": 1,
		"name": "Dslr Cameras",
		"model_number": "mi-node14",
		"expire_date": "2021-04-04T06:00:00Z",
		"category": 1
	}
		self.response = self.client.post(
			reverse('api_category_create'),
			self.category_data,
			format="json")#category create
		self.response = self.client.post(
			reverse('api_create_asset'),
			self.asset_data,
			format="json")#asset create
	
	def test_01_api_can_create_a_assetlist(self):
	#     """Test the api has employee creation capability."""
		response=self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
	

	def test_02_api_can_get_a_assetlist(self):#get and view
		# """Test the api can get a given bucketlist."""
		assetlist = Asset.objects.last()
		response = self.client.get(reverse('api_asset_list'))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertContains(response, assetlist)
	

	def test_03_api_can_update_assetlist(self):#02 get and update
		assetlist = Asset.objects.last()
		self.asset_data =    {
		"id": 1,
		"name": "Dslr Cameras",
		"model_number": "mi-node14",
		"expire_date": "2021-04-04T06:00:00Z",
		"category": 1
	}       
		response = self.client.put(
			reverse('api_asset_update', kwargs={'pk':assetlist.id}),self.asset_data,
			 format='json'
		)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

	



	def test_04_api_can_delete_assetlist(self):
		assetlist = Asset.objects.last()
		response = self.client.delete(
			reverse('api_asset_delete', kwargs={'pk':assetlist.id}),self.asset_data,
			 format='json'
		)
		self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)






