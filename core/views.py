from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from .models import UserData
from .serializers import UserDataSerializer

PAGE_SIZE = 20
class UserDataList(APIView):
    def get(self, request):
        user_data = UserData.objects.all()

        paginator = PageNumberPagination()
        paginator.page_size = PAGE_SIZE
        result_page = paginator.paginate_queryset(user_data, request)
        
        serializer = UserDataSerializer(result_page, many=True)
        
        return paginator.get_paginated_response(serializer.data)


class UserDataDetail(APIView):
    def get(self, request, pk):
        try:
            user_data = UserData.objects.get(pk=pk)
        except UserData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserDataSerializer(user_data)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            user_data = UserData.objects.get(pk=pk)
        except UserData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserDataSerializer(user_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            user_data = UserData.objects.get(pk=pk)
        except UserData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        user_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
