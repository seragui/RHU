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
    opciones = [(True, 'Sí'), (False, 'No'), ]
    regex_validator = RegexValidator(
        regex=r'^\d{8}-\d{1}$', message="Ingrese un número con el formato válido (xxxxxxxx-x).")
    ESTADO_CIVIL_CHOICES = [('soltero', 'Soltero/a'), ('casado', 'Casado/a'),
                            ('divorciado', 'Divorciado/a'), ('viudo', 'Viudo/a'), ]
    tipos_genero = (('M', 'Masculino'), ('F', 'Femenino'),)

    nombres = models.CharField('Nombres', max_length=100, blank=False)
    apellidos = models.CharField('Apellidos', max_length=100, blank=False)
    fecha_nacimiento = models.DateField(
        'Fecha de Nacimiento', auto_now=False, auto_now_add=False, blank=False)
    direccion = models.TextField('Direccion', max_length=400, blank=False)
    telefono = models.CharField("Numero de contacto", max_length=11, validators=[RegexValidator(
        regex=r'^\+?1?\d{9,15}$', message="Ingrese un número de teléfono válido.")])
    sexo = models.CharField("Sexo", max_length=1,
                            choices=tipos_genero, default='M')
    documento_identidad = models.CharField(
        "Documento de Indentidad", max_length=10, validators=[regex_validator], unique=True)
    correo = models.EmailField("Correo", max_length=254)
    estado_civil = models.CharField(
        "Estado Civil", max_length=20, choices=ESTADO_CIVIL_CHOICES, blank=False)
    no_isss = models.CharField("No ISSS", max_length=9, validators=[
                               RegexValidator(regex=r'^\d+$', message="Ingrese solo números.")])
    no_afp = models.CharField("No AFP", max_length=12, validators=[
                              RegexValidator(regex=r'^\d+$', message="Ingrese solo números.")])

    class Meta:
        verbose_name = ("Empleado")
        verbose_name_plural = ("Empleados")

    def __str__(self):
        return str(self.id) + " " + self.nombres + " " + self.apellidos  


class Empleado(Persona):
    contratos = (('Formal', 'Contrato Formal'),
                 ('Servicios', 'Servicios Profesionales'),)

    salario = models.DecimalField(max_digits=8, decimal_places=2)
    fecha_contratacion = models.DateField(
        'Fecha de Contratacion')
    cargo = models.ForeignKey(
        'Cargo', verbose_name='Cargo', on_delete=models.CASCADE, blank=False)
    id_departamento = models.ForeignKey(
        'Departamento', verbose_name='Departamento', on_delete=models.CASCADE, blank=False)
    tipo_contrato = models.CharField(
        "Tipo de Contrato", max_length=10, choices=contratos, default="formal")


class Incapacidad(BaseModel):
    opciones = [(True, 'Sí'), (False, 'No'), ]
    id_empleado = models.ForeignKey(
        'Empleado', verbose_name='Empleados', on_delete=models.CASCADE, blank=False)
    cantidad_dias = models.IntegerField("Cantidad de Dias", blank=False)
    motivo = models.TextField('Motivo', max_length=200, blank=False)
    fecha_inicio = models.DateField('Fecha de Inicio', blank=False)
    fecha_final = models.DateField('Fecha de finalización', blank=False)
    documentacion = models.BooleanField(
        '¿Entrego documentación?', choices=opciones, default=True, blank=False)

    class Meta:
        verbose_name = ("Incapacidad")
        verbose_name_plural = ("Incapacidades")

    def __str__(self):
        return f'{self.id_empleado} {self.cantidad_dias}'
    
class Ausencia(BaseModel):
    opciones = [(True, 'Sí'), (False, 'No'), ]
    id_empleado = models.ForeignKey(
        'Empleado', verbose_name='Empleados', on_delete=models.CASCADE, blank=False)
    cantidad_dias = models.IntegerField("Cantidad de Dias", blank=False)
    fecha_inicio = models.DateField('Fecha de Inicio', blank=False)
    fecha_final = models.DateField('Fecha de finalización', blank=False)

class Prestaciones(BaseModel):
    empleado = models.ForeignKey('Empleado', verbose_name='Empleado', on_delete=models.CASCADE)
    departamento = models.CharField('Departamento', max_length=200, blank=False)
    salario = models.DecimalField(max_digits=8, decimal_places=2, default=None)
    isss_laboral = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    isss_patronal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    afp_laboral = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    afp_patronal = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    impuesto_renta = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    total_descuento = models.DecimalField(max_digits=8, decimal_places=2, default=0)
    sueldo_liquido = models.DecimalField(max_digits=8, decimal_places=2, default=0)


    class Meta:
        verbose_name = "Prestación"
        verbose_name_plural = "Prestaciones"

    def __str__(self):
        return f'{self.empleado} - {self.departamento}'

    
class Retencion(models.Model):
    frecuencia_pago_choices = [
        ('Mensual', 'Mensual'),
        ('Quincenal', 'Quincenal'),
        ('Semanal', 'Semanal')
    ]

    desde = models.DecimalField(max_digits=10, decimal_places=2)
    hasta = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje = models.DecimalField(max_digits=5, decimal_places=2)
    cuota_fija = models.DecimalField(max_digits=10, decimal_places=2)
    frecuencia_pago = models.CharField(max_length=10, choices=frecuencia_pago_choices)

    def __str__(self):
        return f"Retención {self.frecuencia_pago}: {self.desde} - {self.hasta}"


class TablaRetenciones(models.Model):
    retenciones = models.ManyToManyField(Retencion)

    def __str__(self):
        return "Tabla de Retenciones"
    
class Indemnizacion(BaseModel):
    empleado = models.ForeignKey('Empleado', verbose_name='Empleado', on_delete=models.CASCADE)
    departamento = models.ForeignKey('Departamento', verbose_name='Departamento', on_delete=models.CASCADE, default=None)
    fecha_ingreso = models.DateField('Fecha de Ingreso', blank=False)
    fecha_retiro = models.DateField('Fecha de retiro', blank=False)
    salario = models.DecimalField('Salario',max_digits=8, decimal_places=2, default=None)
    años_completos = models.IntegerField("Años completados",default=None, blank=False)
    pago = models.DecimalField('Pago por años', max_digits=8,decimal_places=2, blank=False)

    class Meta:
        verbose_name = "Indemnizacion"
        verbose_name_plural = "Indemnizaciones"

    def __str__(self):
        return f'{self.empleado} - {self.departamento}'
    
    def save(self, *args, **kwargs):
        if self.empleado:
            self.departamento = self.empleado.id_departamento
            self.salario = self.empleado.salario
            self.fecha_ingreso = self.empleado.fecha_contratacion