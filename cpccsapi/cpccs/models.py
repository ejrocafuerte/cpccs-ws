from django.db import models

def make_dir(instance, filename):
    return 'uploads/denuncia/{0}/{1}'.format(instance.denuncia,filename)

# Create your models here.
class Sector(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    control = models.CharField(max_length=5)
    mensaje = models.CharField(max_length=255)

    class Meta:
        db_table = 'sector'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class EstadoCivil(models.Model):
    nombre = models.CharField(max_length=255)
    #id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'estadocivil'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class Institucion(models.Model):
    url = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    competencia = models.CharField(max_length=255)
    representante = models.CharField(max_length=255)
    #id = models.IntegerField(primary_key=True)
    publica=models.BooleanField(default=True)
    sector = models.ForeignKey(
        Sector,
        db_column='sectorid',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'institucion'
        ordering = ('id',)

    def __str__(self):
        return self.nombre

class Nacionalidad(models.Model):
    nombre = models.CharField(max_length=255)
    #id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'nacionalidad'
        ordering = ('id',)

    def __str__(self):
        return self.nombre

class NivelEducacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    #id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'niveleducacion'
        ordering = ('id',)

    def __str__(self):
        return self.nombre

class Ocupacion(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    #id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'ocupacion'
        ordering = ('id',)

    def __str__(self):
        return self.nombre

class PreDenuncia(models.Model):
    tipodenuncia = models.CharField(max_length=1)
    generodenunciante = models.CharField(max_length=255)
    descripcioninvestigacion = models.CharField(max_length=255)
    generodenunciado = models.CharField(max_length=255)
    funcionariopublico = models.CharField(max_length=255, blank=True, default='')
    #id = models.IntegerField(primary_key=True)
    niveleducaciondenunciante = models.ForeignKey(
        NivelEducacion,
        db_column='niveleducaciondenuncianteid',
        on_delete=models.CASCADE)
    ocupaciondenunciante = models.ForeignKey(
        Ocupacion,
        db_column='ocupaciondenuncianteid',
        on_delete=models.CASCADE)
    nacionalidaddenunciante = models.ForeignKey(
        Nacionalidad,
        db_column='nacionalidaddenuncianteid',
        on_delete=models.CASCADE)
    estadocivildenunciante = models.ForeignKey(
        EstadoCivil,
        db_column='estadocivildenuncianteid',
        on_delete=models.CASCADE)
    institucionimplicada = models.ForeignKey(
        Institucion,
        db_column='institucionimplicadaid',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'predenuncia'
        ordering = ('id',)

    def __str__(self):
        return self.id
class Region(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=255)
    #id = models.IntegerField(primary_key=True)

    class Meta:
        db_table = 'region'
        ordering = ('id',)

    def __str__(self):
        return self.nombre

class Provincia(models.Model):
    nombre = models.CharField(max_length=255)
    #id = models.IntegerField(primary_key=True)
    region = models.ForeignKey(
        Region,
        db_column='regionid',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'provincia'
        ordering = ('id',)

    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    nombre = models.CharField(max_length=255)
    #id = models.IntegerField(primary_key=True)
    provincia = models.ForeignKey(
        Provincia,
        db_column='provinciaid',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'ciudad'
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class Reclamo(models.Model):
    nombresapellidosdenunciante = models.CharField(max_length=255)
    tipoidentificacion = models.CharField(max_length=255)
    numidenti = models.CharField(max_length=255)
    direccion = models.CharField(max_length=255, blank=True, default='')
    email = models.CharField(max_length=255)
    nombresapellidosdenunciado = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255, blank=True, default='')
    cargo = models.CharField(max_length=255, blank=True, default='')
    comparecer = models.BooleanField(default=False)
    documentores = models.BooleanField(default=False)
    identidadreservada = models.BooleanField(default=False)
    resideextrangero = models.BooleanField(default=False)
    #id = models.IntegerField(primary_key=True)
    ciudaddeldenunciante = models.ForeignKey(
        Ciudad,
        db_column='ciudaddeldenuncianteid',
        related_name='ciudaddeldenunciante',
        on_delete=models.CASCADE)
    ciudaddeldenunciado = models.ForeignKey(
        Ciudad,
        db_column='ciudaddeldenunciadoid',
        related_name='ciudaddenunciado')
    institucionimplicada = models.ForeignKey(
        Institucion,
        db_column='insttitucionimplicadaid',
        on_delete=models.CASCADE)
    provinciadenunciante = models.ForeignKey(
        Provincia,
        db_column='provinciadenuncianteid',
        related_name='provinciadenunciante',
        on_delete=models.CASCADE)
    provinciadenunciado = models.ForeignKey(
        Provincia,
        db_column='provinciadenunciadoid',
        related_name='provinciadenunciado',
        on_delete=models.CASCADE)

    class Meta:
        db_table = 'reclamo'
        ordering = ('id',)

    def __str__(self):
        return self.nombresapellidosdenunciante

class Usuario(models.Model):
    nome = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    telefone = models.CharField(max_length=12)

    class Meta:
        db_table = 'usuario'
        ordering = ('nome',)

    def __str__(self):
        return self.nome

class InstitucionCiudad(models.Model):
    institucion=models.ForeignKey(
        Institucion,
        db_column='institucionid',
        related_name='instituciondedenuncia',
        on_delete=models.CASCADE)
    ciudad=models.ForeignKey(
        Ciudad,
        db_column='ciudadid',
        related_name='ciudaddeinstitucion',
        on_delete=models.CASCADE)
    sw=models.BooleanField(default=True)
    class Meta:
        db_table='institucionciudad'

class Pais(models.Model):
    nombre=models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table='pais'
        ordering = ('nombre',)

class Etnia(models.Model):
    nombre=models.CharField(max_length=255)
    def __str__(self):
        return self.nombre
    class Meta:
        db_table='etnia'
        ordering = ('nombre',)

class Contenido(models.Model):
    descripcion=models.CharField(max_length=255)
    contenido=models.CharField(max_length=255)
    url_video=models.CharField(max_length=255)
    def __str__(self):
        return self.descripcion
    class Meta:
        db_table='contenido'

class Evidencia(models.Model):
    denuncia=models.CharField(max_length=255)
    fecha=models.DateField(auto_now=True)
    archivo=models.FileField(upload_to=make_dir)
    class Meta:
        db_table='evidencia'
