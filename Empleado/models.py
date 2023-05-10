from django.db import models
from django.core.validators import RegexValidator
from django.forms import TextInput
from base.models import BaseModel

# Create your models here.

class Cargo(BaseModel):

    nombre_cargo = models.CharField(
        'Nombre de Cargo', max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = ("Cargo")
        verbose_name_plural = ("Cargos")

    def __str__(self):
        return self.nombre_cargo

class Departamento(BaseModel):

    nombre_departamento = models.CharField(
        'Nombre de Departamento', max_length=50, blank=False, unique=True)

    class Meta:
        verbose_name = ('Departamento')
        verbose_name_plural = ('Departamentos')

    def __str__(self):
        return self.nombre_departamento

class Persona(BaseModel):
    opciones = [(True, 'Sí'),(False, 'No'),]
    regex_validator = RegexValidator(regex=r'^\d{8}-\d{1}$',message="Ingrese un número con el formato válido (xxxxxxxx-x).")
    ESTADO_CIVIL_CHOICES = [('soltero', 'Soltero/a'),('casado', 'Casado/a'),('divorciado', 'Divorciado/a'),('viudo', 'Viudo/a'),]

    nombres = models.CharField('Nombres', max_length=100, blank=False )
    apellidos = models.CharField('Apellidos', max_length=100, blank=False )
    fecha_nacimiento = models.DateField('Fecha de Nacimiento', auto_now=False, auto_now_add=False, blank=False )
    direccion = models.TextField('Direccion', max_length=400, blank=False )
    telefono = models.CharField("Numero de contacto",max_length=11, validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$',message="Ingrese un número de teléfono válido.")])
    documento_identidad = models.CharField('Documento de Identidad',max_length=9, blank=False , unique=True)
    flag_discapacidad = models.BooleanField('Posee una discapacidad?',choices=opciones, default=False,blank=False)
    documento_identidad = models.CharField("Documento de Indentidad",max_length=10,validators=[regex_validator])
    correo = models.EmailField("Correo",max_length=254)
    estado_civil = models.CharField("Estado Civil",max_length=20, choices=ESTADO_CIVIL_CHOICES,blank=False)
    no_isss = models.CharField("No ISSS",max_length=9,validators=[RegexValidator(regex=r'^\d+$',message="Ingrese solo números.")])
    no_afp = models.CharField("No AFP",max_length=12,validators=[RegexValidator(regex=r'^\d+$',message="Ingrese solo números.")])

    class Meta:
        verbose_name = ("Empleado")
        verbose_name_plural = ("Empleados")

    def __str__(self):
        return self.nombres

class Empleado(Persona):
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_contratacion = models.DateField(
        'Fecha de Contratacion')
    cargo = models.ForeignKey(
        'Cargo', verbose_name='Cargo', on_delete=models.CASCADE, blank=False )
    id_departamento = models.ForeignKey(
        'Departamento', verbose_name='Departamento', on_delete=models.CASCADE, blank=False )

class Incapacidad(BaseModel):
    id_empleado = models.ForeignKey(
        'Empleado', verbose_name='Empleados', on_delete=models.CASCADE, blank=False )
    
