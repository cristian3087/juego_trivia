from django.db import models
from usuarios.models import BaseModel, Jugador
# Create your models here.

# class Nivel(BaseModel):
#     nombre = models.CharField(max_length=50, unique=True)
#     aleas = models.IntegerField(default=1)

NIVEL = (
    (1, 'BASICO'),
    (2, 'MEDIO'),
    (3, 'AVANZADO'),
    (4, 'EXPERTO'),
)
class Categoria(BaseModel):
    nombre = models.CharField(max_length=60)
    
    def __str__(self) -> str:
        return f"{self.id}.{self.nombre}"
  


class Pregunta(BaseModel):
    enunciado= models.TextField()
    nivel = models.IntegerField(choices=NIVEL)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self) -> str:
        return f"{self.enunciado}, {self.nivel}, {self.categoria.nombre}"

class Respuesta(BaseModel):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    texto = models.TextField()
    es_correcta = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.pregunta.id}, {self.texto}, {self.es_correcta}"     

class ConfiguracionPartida(BaseModel):
    num_preguntas = models.IntegerField(default=1)
    tiempo_por_nivel = models.IntegerField(default=5)


class Partida(BaseModel):
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)
    score = models.IntegerField()
    configuracion = models.ForeignKey(ConfiguracionPartida, on_delete=models.CASCADE)

class DetallePartida():
    partida = models.ForeignKey(Partida, on_delete=models.CASCADE)
    




