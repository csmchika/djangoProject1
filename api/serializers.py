from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Activity


class UserSerializer(serializers.ModelSerializer):
    activity = serializers.StringRelatedField(many=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'activity']


class ActivitySerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    calories = serializers.SerializerMethodField('get_calories')

    def get_calories(self, obj):
        d = {
            'Бег': 3,
            'Ходьба': 4,
            'Велосипед': 5
        }
        if obj.type in d:
            return obj.distance * d[obj.type]


    class Meta:
        model = Activity
        fields = ['id', 'started', 'finished', 'type', 'distance', 'calories', 'owner']
