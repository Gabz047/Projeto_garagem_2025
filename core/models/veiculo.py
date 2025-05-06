from django.db import models
from .cor import Cor
from .modelo import Modelo
from .acessorio import Acessorio

class Veiculo(models.Model):
    ano = models.IntegerField(null=True, default=0, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2, default=0, null=True, blank=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.PROTECT, related_name='veiculos')
    cor = models.ForeignKey(Cor, on_delete=models.PROTECT, related_name='veiculos')
    acessorio = models.ForeignKey(Acessorio, on_delete=models.PROTECT, related_name='veiculos')

    def __str__(self):
        return f"{self.id} - {self.modelo} - {self.cor} - {self.ano}" 