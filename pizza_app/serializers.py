from rest_framework import serializers
from django.contrib.auth  import authenticate
from rest_framework import exceptions
from pizza_app.models import Pizza
from django.http import HttpResponse

class ModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Pizza
        fields=(
            'id',
            'pizza_type',
            'pizza_size',
            'toppings'
        )  
        
class PostSerialzer(serializers.ModelSerializer):
        def save(self):
            try:
                pizza=Pizza(
                    pizza_size=self.validated_data['pizza_size'],
                    pizza_type=self.validated_data['pizza_type'],
                    toppings=self.validated_data['toppings'],
                    )
                pizza_size=self.validated_data['pizza_size']
                pizza_type=self.validated_data['pizza_type']
                toppings=self.validated_data['toppings']
                pizza.save()
                return pizza
            except KeyError as ke:
                print('Key must be', ke)   
            
        class Meta:
            model=Pizza
            fields='__all__'  
