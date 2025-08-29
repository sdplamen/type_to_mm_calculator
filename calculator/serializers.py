from rest_framework import serializers

class CalculationSerializer(serializers.Serializer):
    conversion_type = serializers.ChoiceField(choices=['mm_to_points', 'points_to_mm'])
    value = serializers.FloatField()