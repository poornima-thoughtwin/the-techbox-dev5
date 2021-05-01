from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import render,redirect,HttpResponse
from rest_framework.pagination import PageNumberPagination
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework import response, decorators, permissions, status
from django.contrib.admin.views.decorators import staff_member_required
from rest_framework_simplejwt.views import (TokenObtainPairView,TokenRefreshView,)
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
#curl=settings.CURRENT_URL
from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework import serializers
from .models import *
from django.conf import settings
from rest_framework.response import Response
from .models import AssetAssign
from .serializers import *
from rest_framework.views import APIView
from django.http import Http404
from rest_framework.response import Response
from rest_framework import status
from .models import *

@api_view(['POST'])
@permission_classes([AllowAny])
#@ensure_csrf_cookie
def mylogin(request):
    response = Response()

    username = request.data.get('username')
    password = request.data.get('password')
    obj = User.objects.filter(username=username).first()
    user = authenticate(username=username,password=password)

    refresh = ''
    access = ''
    user_type = ''
    status = 201
    verified_status = ''

    if username is None:
        message = 'username is required.'
    
    elif password is None:
        message = 'password is required.'

    elif obj is None:
        message = 'Invalid user.'

    elif user is None:
        message = 'Invalid password.'

    elif user.is_active ==0:
        message = 'unverified user.'
        verified_status = 0

    else:
        token = RefreshToken.for_user(obj)
        refresh = str(token)
        access = str(token.access_token)
        user_type = obj.user_type
        status = 200
        message = 'valid user'
        verified_status = 1

     
    response.data={
        'success' : status,
        #'message' : 'User registered succefuly.',
        'message' : message,
        "refresh": refresh,
        "access": access,
        'user_type' : user_type,
        'verified_status': verified_status
    }

    return response




class AssetList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        asset = Asset.objects.all()
        serializer = AssetSerializer(asset, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  AssetDetail(APIView):

    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Asset.objects.get(pk=pk)
        except Asset.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        asset = self.get_object(pk)
        serializer = AssetSerializer(asset)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        #permission_classes = [AllowAny]
        # import pdb;pdb.set_trace()
        asset = self.get_object(pk)
        serializer = AssetSerializer(asset, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        # import pdb;pdb.set_trace()
        asset = self.get_object(pk)
        #asset = Asset.objects.get(id=pk)
        asset.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class EmployeeList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        employee = Employee.objects.all()
        serializer = EmployeeSerializer(employee, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  EmployeeDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Employee.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        employee = self.get_object(pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_object(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AssetAssignList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        assetassign = AssetAssign.objects.all()
        serializer = AssetAssignSerializer(assetassign, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = AssetAssignSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  AssetAssignDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return AssetAssign.objects.get(pk=pk)
        except Employee.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        assetassign = self.get_object(pk)
        serializer = AssetAssignSerializer(assetassign)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        assetassign = self.get_object(pk)
        serializer = AssetAssignSerializer(assetassign, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        assetassign = self.get_object(pk)
        assetassign.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class DesignationList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        designation = Designation.objects.all()
        serializer = DesignationSerializer(designation, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = DesignationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  DesignationDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Designation.objects.get(pk=pk)
        except Designation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        designation = self.get_object(pk)
        serializer = DesignationSerializer(designation)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        designation = self.get_object(pk)
        serializer = DesignationSerializer(designation, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        designation = self.get_object(pk)
        designation.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#.................................login

class CategoryList(APIView):
    """
    List all snippets, or create a new snippet.
    """
    def get(self, request, format=None):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer =CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class  CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        category = self.get_object(pk)
        serializer = CategorySerializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        category = self.get_object(pk)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



# class TodoListCreateAPIView(ListCreateAPIView):
#     serializer_class = TodoSerializer
# ​
#     def get_queryset(self):
#         return Todo.objects.filter(user=self.request.user)
# ​
#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)
# ​
# ​
# class TodoDetailAPIView(RetrieveUpdateDestroyAPIView):
#     serializer_class = TodoSerializer
#     queryset = Todo.objects.all()
#     permission_classes = (IsAuthenticated, UserIsOwnerTodo)




# class TodoListCreateAPIViewTestCase(APITestCase):
#     url = reverse("todos:list")
# ​
#     def setUp(self):
#         self.username = "john"
#         self.email = "john@snow.com"
#         self.password = "you_know_nothing"
#         self.user = User.objects.create_user(self.username, self.email, self.password)
#         self.token = Token.objects.create(user=self.user)
#         self.api_authentication()
# ​
#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
# ​
#     def test_create_todo(self):
#         response = self.client.post(self.url, {"name": "Clean the room!"})
#         self.assertEqual(201, response.status_code)
# ​
#     def test_user_todos(self):
#         """
#         Test to verify user todos list
#         """
#         Todo.objects.create(user=self.user, name="Clean the car!")
#         response = self.client.get(self.url)
#         self.assertTrue(len(json.loads(response.content)) == Todo.objects.count())
# ​
# ​
# class TodoDetailAPIViewTestCase(APITestCase):
# ​
#     def setUp(self):
#         self.username = "john"
#         self.email = "john@snow.com"
#         self.password = "you_know_nothing"
#         self.user = User.objects.create_user(self.username, self.email, self.password)
#         self.todo = Todo.objects.create(user=self.user, name="Call Mom!")
#         self.url = reverse("todos:detail", kwargs={"pk": self.todo.pk})
#         self.token = Token.objects.create(user=self.user)
#         self.api_authentication()
# ​
#     def api_authentication(self):
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
# ​
#     def test_todo_object_bundle(self):
#         """
#         Test to verify todo object bundle
#         """
#         response = self.client.get(self.url)
#         self.assertEqual(200, response.status_code)
# ​
#         todo_serializer_data = TodoSerializer(instance=self.todo).data
#         response_data = json.loads(response.content)
#         self.assertEqual(todo_serializer_data, response_data)
# ​
#     def test_todo_object_update_authorization(self):
#         """
#             Test to verify that put call with different user token
#         """
#         new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
#         new_token = Token.objects.create(user=new_user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
# ​
#         # HTTP PUT
#         response = self.client.put(self.url, {"name", "Hacked by new user"})
#         self.assertEqual(403, response.status_code)
# ​
#         # HTTP PATCH
#         response = self.client.patch(self.url, {"name", "Hacked by new user"})
#         self.assertEqual(403, response.status_code)
# ​
#     def test_todo_object_update(self):
#         response = self.client.put(self.url, {"name": "Call Dad!"})
#         response_data = json.loads(response.content)
#         todo = Todo.objects.get(id=self.todo.id)
#         self.assertEqual(response_data.get("name"), todo.name)
# ​
#     def test_todo_object_partial_update(self):
#         response = self.client.patch(self.url, {"done": True})
#         response_data = json.loads(response.content)
#         todo = Todo.objects.get(id=self.todo.id)
#         self.assertEqual(response_data.get("done"), todo.done)
# ​
#     def test_todo_object_delete_authorization(self):
#         """
#             Test to verify that put call with different user token
#         """
#         new_user = User.objects.create_user("newuser", "new@user.com", "newpass")
#         new_token = Token.objects.create(user=new_user)
#         self.client.credentials(HTTP_AUTHORIZATION='Token ' + new_token.key)
#         response = self.client.delete(self.url)
#         self.assertEqual(403, response.status_code)
# ​
#     def test_todo_object_delete(self):
#         response = self.client.delete(self.url)
#         self.assertEqual(204, response.status_code)