from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import PackageSerializer,SubscriptionSerializer
from .models import Category,Product,File,Package
from django.utils import timezone
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Gateway,Payment
from subscriptions.models import Package,Subscription
from .serializers import GatewaySerializer 
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
import requests
import uuid
class PackageView(APIView):
    def get(self,request):
        packages = Package.objects.filter(is_enable = True)
        serializer = PackageSerializer(packages,many = True)
        return Response(serializer.data)
class SubscriptionView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self,request):
        subscription = Subscription.objects.filter
        subscription = Subscription.objects.filter(user = request.user,
                                                   expire_time__gt = timezone.now()) # expire time greather than now 
        serializer = SubscriptionSerializer(subscription,many =True)
        return Response(serializer.data)    