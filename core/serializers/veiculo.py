from core.models import Veiculo
from rest_framework.serializers import ModelSerializer

class VeiculoSerializer(ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '__all__'