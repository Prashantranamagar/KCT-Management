from sms.models import Cordinator
from rest_framework import serializers

class CordSerializer(serializers.ModelSerializer):
	class Meta:
		model = Cordinator
		fields = '__all__'