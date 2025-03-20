from django.db import models
from django.contrib.auth.models import AbstractUser
 
# Create your models here.
class Usuario(AbstractUser):
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        
    TIPO_FUNCAO = (
        ("1", "Pastor"),
        ("2", "Presbitero"),
        ("3", "Diacono"),
        ("4", "Obreiro"),
        ("5", "Musico"),
        ("6", "Vocal"),
        ("7", "Membro(a)"),
    )
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15, blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    funcao = models.CharField(max_length=25, blank=True, null=True, choices=TIPO_FUNCAO)
    

    def __str__(self):
        return f"{self.username} - {self.nome}"
    

class Evento(models.Model):
    titulo = models.CharField(max_length=200)
    data = models.DateField()
    participantes = models.ManyToManyField(Usuario, through="Escala")

    def __str__(self):
        return f"{self.titulo} - {self.data}"
    
    
class Escala(models.Model):
    FUNCAO_CHOICES= (
        ('1', 'Cantor(a)'),
        ('2', 'Guitarrista'),
        ('3', 'Baterista'),
    )
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="escalas")
    participante = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="participantes", blank=True, null=True)
    funcao = models.CharField(max_length=10, choices=FUNCAO_CHOICES, blank=True, null=True, verbose_name='Função')

    def __str__(self):
        return f"Escala para {self.evento.titulo}"
