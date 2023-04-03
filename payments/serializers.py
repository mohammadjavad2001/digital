from rest_framework import serializers

from .models import Gateway,Payment

class GatewaySerializer(serializers.ModelSerializer):
    class Meta:
        model = Gateway
        fields = ('id','title','description','avatar','is_enable','created_time','update_time')
class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ('user','package','gateway','price','status','device-uuid','token','phone_number','consumed_code','created_time','updated_time')
