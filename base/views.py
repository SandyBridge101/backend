from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.utils import timezone


# Create your views here.
from rest_framework import generics, permissions
from .models import *
from .serializers import *


class UserModelCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    http_method_names = ['post']

class UserModelListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    http_method_names = ['get']

class UserModelUpdateView(generics.UpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    http_method_names = ['put']

class UserModelDeleteView(generics.DestroyAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    http_method_names = ['delete']

class RideModelCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerializer
    http_method_names = ['post']

class RideModelListView(generics.ListAPIView):
    queryset = RideModel.objects.all()
    serializer_class = RideModelSerializer
    http_method_names = ['get']

class RideModelUpdateView(generics.UpdateAPIView):
    queryset = RideModel.objects.all()
    serializer_class = RideModelSerializer
    http_method_names = ['put']

class RideModelDeleteView(generics.DestroyAPIView):
    queryset = RideModel.objects.all()
    serializer_class = RideModelSerializer
    http_method_names = ['delete']


def login(request,password):
    users=UserModel.objects.all()
    isAuth=False

    for user in users:
        print(user.firstname,user.password,password)
        if user.password==password:
            isAuth=True
    
    print(isAuth)
    data={
        'is_auth':isAuth
    }
    return JsonResponse(data)

def getUser(request,phone):
    users=UserModel.objects.all()
    id=-1
    fname=''
    lname=''
    uname=''
    pword=''

    for user in users:
        print(user.firstname)
        if user.phonenumber==phone:
            id=user.pk
            break

    data={
        'user_id':id,
        'firstname':fname,
        'lastname':lname,
        'username':uname,
        'password':pword
    }
    return JsonResponse(data)


def createRide(request,start,destination,user):# collects user number, start and destination and creates a RideModel
    ride=RideModel(start=start,destination=destination,user=user)
    ride.save()

    data={
        'id':ride.pk
    }
    return JsonResponse(data)

def cancelRide(request,id):#assign ride as cancelled
    ride=RideModel.objects.get(id=id)
    ride.is_cancelled=1
    ride.save()
    data={
        'status':'cancelled'
    }
    return JsonResponse(data)

def getRider(request,ride_id):#gets a rider who is ready and sends assignment message
    users=UserModel.objects.all()
    ride=RideModel.objects.get(id=ride_id)
    rider=None

    for user in users:
        print(user.firstname)
        if user.is_rider==1 and user.is_ready==0:
            rider=user

    
    rider.ride=ride_id
    ride.rider=rider.phonenumber

    rider.save()
    ride.save()

    data={
        'firstname': rider.firstname,
        'lastname': rider.lastname,
        'username': rider.username,
        'phonenumber': rider.phonenumber,
        'ride':rider.ride,
    }

    return JsonResponse(data)

def riderArrived(request,ride_id): # collects input from rider and sends output to user
    ride=RideModel.objects.get(id=ride_id)

    data={
        'user':ride.user
    }
    return JsonResponse()

def startRide(request,ride_id): # collects input from rider to initiate ride
    ride=RideModel.objects.get(id=ride_id)
    ride.start_time=timezone.now()
    ride.save()
    data={
        'status':'start'
    }
    return JsonResponse(data)

def endRide(request,ride_id): # collects input from rider to end ride and sends cost to rider and summary to user
    ride=RideModel.objects.get(id=ride_id)
    ride.end_time=timezone.now()
    ride.save()
    
    duration=ride.end_time-ride.start_time
    cost=round(duration.seconds*0.05,2)
    data={
        'cost':cost,
        'duration':duration.seconds
    }
    return JsonResponse(data)

def rateRide(request,ride_id,rating,feed_back):
    ride=RideModel.objects.get(id=ride_id)
    ride.ratings=rating
    ride.feedback=feed_back
    ride.save()
    data={
        'status':'rated'
    }
    return JsonResponse(data)


def rideHistory(request,user):
    rides=RideModel.objects.all()
    history=[]

    for ride in rides:
        if ride.user==user:
            data={
                'start':ride.start,
                'destination':ride.destination,
                'start_time':ride.start_time,
                'end_time':ride.end_time,
                'feedback':ride.feedback,
                'ratings':ride.ratings,
                'rider_id':ride.rider
            }
            history.append(data)
    
    response_data={
        'history':history
    }
    return JsonResponse(response_data)
