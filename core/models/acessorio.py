from django.db import models

class Acessorio(models.Model):
    descricao = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return f"{self.id} - {self.descricao}" 