from rest_framework import serializers
from .models import Native, Cohort




class CohortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cohort
        fields = "__all__"

    

class NativeSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Native
        fields = "__all__"


        # fields = ('id', 'emai', 'first_name', 'last_name')



