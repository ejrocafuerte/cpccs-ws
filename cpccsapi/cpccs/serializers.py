from rest_framework import serializers
from cpccs.models import Ciudad
from cpccs.models import EstadoCivil
from cpccs.models import NivelEducacion
from cpccs.models import Requerimiento
from cpccs.models import Provincia
from cpccs.models import Usuario
from cpccs.models import Etnia
from cpccs.models import Contenido
from cpccs.models import Evidencia
import cpccs.views

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

class RequerimientoSerializer(serializers.ModelSerializer):
    tipo = serializers.CharField(source='tipodenuncia')
    genero_denunciante = serializers.CharField(source='generodenunciante')
    descripcion_investigacion = serializers.CharField(source='descripcioninvestigacion')
    genero_denunciado = serializers.CharField(source='generodenunciado')
    funcionario_publico = serializers.CharField(source='funcionariopublico', allow_blank=True)
    estado_civil_denunciante = serializers.PrimaryKeyRelatedField(source='estadocivildenunciante', queryset=EstadoCivil.objects.all())

    class Meta:
        model = Requerimiento
        fields = (
            'tipo',
            'genero_denunciante',
            'descripcion_investigacion',
			'genero_denunciado',
            'funcionario_publico',
            'id',
			'nivel_educacion_denunciante',
			'estado_civil_denunciante',
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

class EvidenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evidencia
        fields = (
            'id',
            'denuncia',
            'archivo',
            )
