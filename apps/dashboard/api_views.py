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
# from rest_framework_jwt.views import ObtainJSONWebToken
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

