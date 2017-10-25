from django.db import models
from django.conf import settings


def make_dir(instance, filename):
    return settings.DENUNCIA_ROOT + '/{0}/{1}'.format(instance.denuncia, filename)

class Etnia(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'etnia'
        ordering = ('nombre',)

# Create your models here.
class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=255)

    # id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'estadocivil'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class Genero(models.Model):
    nombre = models.CharField(max_length=25)

    class Meta:
        db_table = 'genero'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class NivelEducacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)

    # id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'niveleducacion'
        ordering = ('id',)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    nombre = models.CharField(max_length=255)

    class Meta:
        db_table = 'provincia'
        ordering = ('id',)

    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=255)
    provincia = models.ForeignKey(
        Provincia,
        db_column='provinciaid',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'ciudad'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class TipoRequerimiento(models.Model):
    nombre = models.CharField(max_length=10)

    class Meta:
        db_table = 'tiporequerimiento'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class Requerimiento(models.Model):
    fechaIngreso = models.DateField(auto_now_add=True)
    ###0 para denuncia 1 para pedido
    tipodenuncia = models.ForeignKey(
        TipoRequerimiento,
        db_column='tipo_requerimiento_id',
        related_name='tiporequerimientoid',
    )
    identidad_reservada = models.BooleanField(default=0)
    #DATOS DEL DENUNCIANTE - PETICIONARIO
    nombres_apellidos_denunciante = models.CharField(max_length=255)
    edad_denunciante = models.CharField(max_length=2)
    correo_denunciante = models.CharField(max_length=100)
    telefono_denunciante = models.CharField(max_length=13)
    celular_denunciante = models.CharField(max_length=13)
    direccion_denunciante = models.CharField(max_length=100)
    ciudad_denunciante = models.ForeignKey(
        Ciudad,
        db_column='ciudaddenuncianteid',
        related_name='ciudaddenunciante',
    )
    provincia_denunciante = models.ForeignKey(
        Provincia,
        db_column='provinciadenuncianteid',
        related_name='provinciadenunciante',
    )
    genero_denunciante = models.ForeignKey(
        Genero,
        db_column='generodenuncianteid',
        related_name='generodenunciante',
    )
    estado_civil_denunciante = models.ForeignKey(
        EstadoCivil,
        db_column='estadocivildenuncianteid',
        related_name='estadocivildenunciante',
    )
    etnia_denunciante = models.ForeignKey(
        Etnia,
        db_column='etniadenuncianteid',
        related_name='etniadenunciante',
    )
    niveleducaciondenunciante = models.ForeignKey(
        NivelEducacion,
        db_column='niveleducaciondenuncianteid',
        related_name="educaciondenunciante",
    )
    institucion_denunciante = models.CharField(max_length=60)
    cargo_denunciante = models.CharField(max_length=100)
    tipo_identificacion = models.CharField(max_length=10)
    identificacion_id = models.CharField(max_length=10)
    pais = models.CharField(max_length=30)
    ###Descripcion de denuncia y evidencia
    descripcion = models.CharField(max_length=255)

    ####DATOS DEl DENUNCIADO
    nombres_apellidos_denunciado = models.CharField(max_length=255)
    genero_denunciado = models.ForeignKey(
        Genero,
        db_column='generodenunciadoid',
        related_name='generodenunciado',
    )
    institucion_denunciado = models.CharField(max_length=60)
    cargo_denunciado = models.CharField(max_length=100)
    ciudad_denunciado = models.ForeignKey(
        Ciudad,
        db_column='ciudaddenunciadoid',
        related_name='ciudaddenunciado',
    )
    provincia_denunciado = models.ForeignKey(
        Provincia,
        db_column='provinciadenunciadoid',
        related_name='provinciadenunciado',
    )
    parroquia_denunciado = models.CharField(max_length=30)

    class Meta:
        db_table = 'requerimiento'
        ordering = ('id',)

    def __str__(self):
        return self.id

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=12)

    class Meta:
        db_table = 'usuario'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class Contenido(models.Model):
    descripcion = models.CharField(max_length=255)
    contenido = models.CharField(max_length=255)
    url_video = models.CharField(max_length=255)

    def __str__(self):
        return self.descripcion

    class Meta:
        db_table = 'contenido'


class Evidencia(models.Model):
    denuncia = models.CharField(max_length=255)
    fecha = models.DateField(auto_now=True)
    archivo = models.FileField(upload_to=make_dir)

    class Meta:
        db_table = 'evidencia'