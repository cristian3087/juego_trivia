from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BaseModel(models.Model):
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    usuario_creacion = models.ForeignKey(User, related_name="%(class)s_creado_por", on_delete=models.SET_NULL, null=True)
    usuario_modificacion = models.ForeignKey(User, related_name="%(class)s_modificado_por", on_delete=models.SET_NULL, null=True)
    
    class Meta:
        abstract = True

class Jugador(BaseModel):
    email = models.EmailField(unique=True)
    nombres  = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    habilitado =models.BooleanField(default=True)
    
    @property
    def nombres_completos(self):
        "Nombres completos"
        return f"{self.nombres} {self.apellidos}"
    
    def __str__(self) -> str:
        return f'{self.identificacion} {self.nombres} {self.apellidos}'