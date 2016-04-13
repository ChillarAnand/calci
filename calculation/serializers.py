from swampdragon.serializers.model_serializer import ModelSerializer


class CalculationSerializer(ModelSerializer):
    class Meta:
        model = 'calculation.Calculation'
        publish_fields = ['expression', 'result']
