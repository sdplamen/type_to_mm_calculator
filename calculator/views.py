from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema, OpenApiParameter
from calculator.serializers import CalculationSerializer


# Create your views here.
def mm_to_points(mm):
    points_per_mm = 72 / 25.4
    return mm * points_per_mm

def points_to_mm(points):
    inches = points / 72.0
    return inches * 25.4

def index(request):
    result = None
    if request.method == 'POST':
        conversion_type = request.POST.get('conversion_type')
        try:
            value = float(request.POST.get('value', 0))
            if conversion_type == 'mm_to_points' :
                result_value = mm_to_points(value)
                result = f'{value} mm is approximately {result_value:.2f} points'
            elif conversion_type == 'points_to_mm' :
                result_value = points_to_mm(value)
                result = f'{value} points is approximately {result_value:.2f} mm'
        except ValueError:
            result = 'Please enter a valid number'

    return render(request, 'index.html', {'result': result})


class ConversionAPIView(APIView) :
    @extend_schema(
        request=CalculationSerializer,
        responses={200: CalculationSerializer},
        description='Convert between millimeters and points',
        parameters=[
            OpenApiParameter(
                name='conversion_type',
                type=str,
                enum=['mm_to_points', 'points_to_mm'],
                description='Type of conversion',
                required=True
            )
        ]
    )
    def post(self, request) :
        serializer = CalculationSerializer(data=request.data)
        if serializer.is_valid() :
            conversion_type = serializer.validated_data['conversion_type']
            value = serializer.validated_data['value']

            if conversion_type == 'mm_to_points' :
                result = mm_to_points(value)
                result_text = f'{value} mm is approximately {result:.2f} points'
            elif conversion_type == 'points_to_mm':
                result = points_to_mm(value)
                result_text = f'{value} points is approximately {result:.2f} mm'
            else :
                return Response({"error": 'Invalid conversion type'}, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'result' :result_text,
                'value' :round(result, 2)
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)