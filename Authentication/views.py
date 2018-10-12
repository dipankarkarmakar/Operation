from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


from .models import Task
# Create your views here.
import datetime

@api_view(['POST'])
def addtask(request):
    try:
        print ("request.data: "), request.data
        # **- used to get all the data from the postman
        addob =Task(**request.data)
        addob.created_date = datetime.datetime.now()
        addob.save()
        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print(e)

        return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET'])
def getalltask(request):

     print ("getting all data")
     data = Task.objects.all().values()

     return Response(data)


@api_view(['PUT'])
def updatetask(request):
    try:
        #request.data is used to get the data from the postman
        mobile_number = request.data['mobile_number']
        #the left sde mobile_no. variable is just to store the value of the variable we put in postman which in this case is mobile_number only , no actual reference with the original model value
        Employee_Id = request.data['id']
        #here 'objects'- is where our model and values are already saved from there we are getting the value of the original left side model from value equivalent to right side variable
        task=Task.objects.get(Employee_Id=Employee_Id)
        #here we updating the mobile no. with above postman variable which in this case is mobile_number only
        task.mobile_number=mobile_number
        task.save()
        return Response("Successfully saved", status=status.HTTP_200_OK)
    except Exception as e:
        print (e)

        return Response("Update Failed", status=status.HTTP_401_UNAUTHORIZED)



@api_view(['DELETE'])
def deltask(request):
    Employee_Id = request.data['id']
    print ("id is", Employee_Id)
    d = Task.objects.filter(id=Employee_Id)
    d.delete()
    return Response("Deleted")


import os

def temp_str(request):
    return render(request, "demo.html", {})