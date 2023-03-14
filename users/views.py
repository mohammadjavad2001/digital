from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.core.cache import cache
from .models import User,Device
import uuid

import random
class RegisterView(APIView):
    #shomare mide ma behesh code midm ba sms ya email captcha midim 
    
    def post(self,request):
        phone_number = request.data.get('phone_number')
        if not phone_number:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        try:
            user = User.objects.get(phone_number=phone_number)
            return Response({'detail':'User already registered'},
                            status=status.HTTP_400_BAD_REQUEST)
        except User.DoesNotExist:
            user = User.objects.create_user(phone_number=phone_number)    
       
        #nemishode ba paieini chon mehtod ma ro ke zadim baraye creatuuser dar models ejra nemikone 
        #user,created = User.objects.get_or_create(phone_number = phone_number)
        #agar vojood nadasht besazesh 
        #agar bood bedesh be mean 
        #if not created:
         #   return Response({'detail':'User already registered'},
          #                  status=status.HTTP_400_BAD_REQUEST)
        device =Device.objects.create(user = user)
        code = random.randint(10000,99999)
        #send message this code we call a url witch from sms service provider so we can't instead return a Response
        #we can save cdoe  to cache and set to this code is valid from now until 2 minutes
        #https://docs.djangoproject.com/en/4.1/topics/cache/
        cache.set(str(phone_number),code,2*60) 

        return Response({'code':code})
    

class GetTokenView(APIView):
    def post(self,request):
        phone_number = request.data.get('phone_number')
        code = request.data.get('code')

        cache_code = cache.get(str(phone_number))
        if code != cache_code:
            return Response(status=status.HTTP_204_NO_CONTENT)
        token = str(uuid.uuid4())
        return Response({'token': token})
    
     

    #shomare mobile va code ro mide ma behesh token midim 
    # har api ke az smate client sedd zade besshe oon token baray ma ersal mishe
    #  