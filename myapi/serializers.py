from rest_framework import serializers
from .models import Person

class PersonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Person
        fields = ('userId','FirstName','LastName','phoneNumber','Email',)
        