from garagem.models import Acessorio
from rest_framework.serializers import ModelSerializer

class AcessorioSerializer(ModelSerializer):
    class Meta:
        model = Acessorio
        fields = '__all__'