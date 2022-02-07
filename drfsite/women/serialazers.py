from rest_framework import serializers
from .models import *


class WomenSerialazer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('title', 'cat_id')
