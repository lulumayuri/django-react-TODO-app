from rest_framework import serializers
from.models import Todo1
 
 class TodoSerializer(serializers.ModelSerializers):
    class Meta:
        model