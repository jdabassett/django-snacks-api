from rest_framework import serializers

from snacks.models import Snack


class SnackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snack
        fields = ('id', 'owner', 'name', 'description', 'created_at', 'updated_at')
