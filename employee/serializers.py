from rest_framework import serializers
from .models import employees

class emp_serializers(serializers.ModelSerializer):
    class Meta:
        model = employees
        fields = '__all__'
