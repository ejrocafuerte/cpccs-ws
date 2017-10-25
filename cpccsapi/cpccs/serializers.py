from rest_framework import serializers
from .models import Ciudad
from .models import EstadoCivil
from .models import NivelEducacion
from .models import TipoRequerimiento
from .models import Requerimiento
from .models import Provincia
from .models import Usuario
from .models import Etnia
from .models import Contenido
from .models import Evidencia
from .models import Genero


class EvidenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evidencia
        fields = (
            'id',
            'denuncia',
            'archivo',
            )
class TipoRequerimientoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoRequerimiento
        fields = (
            'id',
            'nombre',
        )

class GeneroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genero
        fields = (
            'id',
            'nombre',
        )

class CiudadSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ciudad
        fields = (
            'nombre',
            'id',
            'provincia'
			)

class EstadoCivilSerializer(serializers.ModelSerializer):

    class Meta:
        model = EstadoCivil
        fields = (
            'nombre',
            'id'
			)
class NivelEducacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = NivelEducacion
        fields = (
            'nombre',
            'descripcion',
            'id'
			)
class ProvinciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Provincia
        fields = (
            'nombre',
            'id'
			)

class UsuarioSerializer(serializers.ModelSerializer):
    nombre = serializers.CharField(source='nome')
    telefono = serializers.CharField(source='telefone')

    class Meta:
        model = Usuario
        fields = (
            'id',
			'nombre',
            'email',
            'telefono'
			)

class EtniaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Etnia
        fields = (
            'id',
            'nombre',
            )

class ContenidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contenido
        fields = (
            'id',
            'descripcion',
            'contenido',
            'url_video',
            )
class RequerimientoSerializer(serializers.ModelSerializer):
    tipodenuncia = serializers.PrimaryKeyRelatedField(queryset=TipoRequerimiento.objects.all(),allow_null=True)
    niveleducaciondenunciante = serializers.PrimaryKeyRelatedField(queryset=NivelEducacion.objects.all(),many=False)

    class Meta:
        model = Requerimiento
        fields = (
            'fechaIngreso',
            'tipodenuncia',
            'identidad_reservada',
            'nombres_apellidos_denunciante',
            'edad_denunciante',
            'correo_denunciante',
            'telefono_denunciante',
            'celular_denunciante',
            'direccion_denunciante',
            'provincia_denunciante',
            'ciudad_denunciante',
            'genero_denunciante',
            'estado_civil_denunciante',
            'etnia_denunciante',
            'niveleducaciondenunciante',
            'institucion_denunciante',
            'cargo_denunciante',
            'tipo_identificacion',
            'identificacion_id',
            'pais',
            'descripcion',
            'nombres_apellidos_denunciado',
            'genero_denunciado',
            'institucion_denunciado',
            'cargo_denunciado',
            'provincia_denunciado',
            'ciudad_denunciado',
            'parroquia_denunciado',
        )
    #fecha_de_ingreso = serializers.PrimaryKeyRelatedField(source='fechaingreso')
    #tipo_requerimiento = serializers.PrimaryKeyRelatedField(source='tiporequerimientoid',queryset=TipoRequerimiento.objects.all(), many=False)
    '''
    tipo_requerimiento = TipoRequerimientoSerializer(queryset=TipoRequerimiento.objects.all())
    nombres_apellidos_denunciante = serializers.CharField()
    edad_denunciante = serializers.CharField()
    correo_denunciante = serializers.EmailField()
    telefono_denunciante = serializers.CharField()
    celular_denunciante = serializers.CharField()
    direccion_denunciante = serializers.CharField()
    provincia_denunciante = serializers.PrimaryKeyRelatedField(source='provinciadenunciante', queryset=Provincia.objects.all())
    ciudad_denunciante = serializers.PrimaryKeyRelatedField(source='ciudaddenunciante', queryset=Ciudad.objects.all())
    genero_denunciante = serializers.PrimaryKeyRelatedField(source='generodenunciante', queryset= Genero.objects.all())
    estado_civil_denunciante = serializers.PrimaryKeyRelatedField(source='estadocivildenunciante', queryset=EstadoCivil.objects.all())
    etnia_denunciante = serializers.PrimaryKeyRelatedField(source='etniadenunciante',queryset=Etnia.objects.all())
    nivel_educacion_denunciante = serializers.PrimaryKeyRelatedField(source='educaciondenuncianteciante', queryset=NivelEducacion.objects.all())
    institucion_denunciante = serializers.CharField()
    cargo_denunciante = serializers.CharField()
    tipo_identificacion = serializers.CharField()
    identificacion_id = serializers.CharField()
    pais= serializers.CharField()

    descripcion_investigacion = serializers.CharField(source='descripcion')
    nombres_apellidos_denunciado = serializers.CharField()
    genero_denunciado = serializers.PrimaryKeyRelatedField(source='generodenunciado', queryset=Genero.objects.all())
    institucion_denunciado = serializers.CharField()
    cargo_denunciado = serializers.CharField()
    provincia_denunciado = serializers.PrimaryKeyRelatedField(source='provinciadenunciado',                                                               queryset=Provincia.objects.all())
    ciudad_denunciado = serializers.PrimaryKeyRelatedField(source='ciudaddenunciado', queryset=Ciudad.objects.all())
    parroquia_denunciado = serializers.CharField()

'''



