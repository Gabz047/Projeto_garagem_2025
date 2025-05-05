from garagem.models import Cor
from rest_framework.serializers import ModelSerializer

class CorSerializer(ModelSerializer):
    class Meta:
        model = Cor
        fields = '__all__'