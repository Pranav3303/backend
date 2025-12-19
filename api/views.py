from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
# All Data
@api_view(['GET'])
def info(request):
    df = TV.objects.all()
    serializers = TVSerializer(df,many=True)

    return Response(serializers.data)


# Create Data
@api_view(['POST'])
def tv_reg(request):
    serializers = TVSerializer(data = request.data)
    if serializers.is_valid():
        serializers.save()
    
    return Response(serializers.data)


# Show One Data
@api_view(['GET'])
def indiv(request, pk):
    df = TV.objects.get(id=pk)
    serializers = TVSerializer(df,many=False)

    return Response(serializers.data)


# To update data
@api_view(['POST'])
def update(request,pk):
    df = TV.objects.get(id=pk)
    serializers = TVSerializer(intance=df,data= request.data)
    if serializers.is_valid():
        serializers.save()

    return Response(serializers.data)


# To delete data
@api_view(['DELETE'])
def delete(request,pk):
    df = TV.objects.get(id=pk)
    df.delete()

    return Response("This Record has been successfully deleted")



def tv_list(request):
    tvs = TV.objects.all().values()
    return JsonResponse(list(tvs), safe=False)