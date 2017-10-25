from .models import Ciudad
from .models import EstadoCivil
from .models import NivelEducacion
from .models import Requerimiento
from .models import Provincia
from .models import Usuario
from .models import Etnia
from .models import Contenido
from .models import Evidencia
from .models import Genero
from .models import TipoRequerimiento

from .serializers import CiudadSerializer
from .serializers import EstadoCivilSerializer
from .serializers import NivelEducacionSerializer
from .serializers import RequerimientoSerializer
from .serializers import ProvinciaSerializer
from .serializers import UsuarioSerializer
from .serializers import EtniaSerializer
from .serializers import ContenidoSerializer
from .serializers import EvidenciaSerializer
from .serializers import GeneroSerializer
from .serializers import TipoRequerimientoSerializer

from rest_framework import generics

from rest_framework.response import Response
from rest_framework.reverse import reverse

from rest_framework import permissions

from django.core.mail import send_mail

# Create your views here.
class CiudadList(generics.ListAPIView):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer
    name = 'ciudad-list'
    filter_fields = ('provincia',)
    search_fields = ('nombre',)
    ordering_fields = ('nombre',)


class EstadoCivilList(generics.ListAPIView):
    queryset = EstadoCivil.objects.all()
    serializer_class = EstadoCivilSerializer
    name = 'estado-civil-list'


class NivelEducacionList(generics.ListAPIView):
    queryset = NivelEducacion.objects.all()
    serializer_class = NivelEducacionSerializer
    name = 'nivel-educacion-list'


class RequerimientoList(generics.ListCreateAPIView):
    queryset = Requerimiento.objects.all()
    serializer_class = RequerimientoSerializer
    name = 'requerimiento-list'
    permission_classes = (permissions.IsAuthenticated,)
    '''
    def perform_create(self, serializer):
        try:
            descripcion = self.request.data['descripcion']
            tipo = self.request.data['tiporequerimiento']
            if tipo == '1':
                accion = 'Denuncia'
            elif tipo =='2':
                accion = 'Petición'
        except KeyError:
            descripcion = ''
            accion = 'Petición'
        instance = serializer.save()
        send_mail( 'Confirmaciòn Envio De Formulario','<h1>Envio Exitoso</h1> <p> Sr(a)' +
                   instance.nombres_apellidos_denunciante + ' su ' + accion + ' ha sido enviada correctamente </p> <h3>' +
                   accion + ': ' + descripcion + '</h3>', 'prueba.envio.formulario@gmail.com', [instance.correo_denunciante],
                   fail_silently = False, html_message = '<h1> Envio Exitoso </h1> <p> Sr(a) ' +
                instance.nombres_apellidos_denunciante + ' su ' + accion + ' ha sido enviada correctamente </p><h3>'+
                accion + ': ' + descripcion + '</h3>')
'''
class ProvinciaList(generics.ListAPIView):
    queryset = Provincia.objects.all()
    serializer_class = ProvinciaSerializer
    name = 'provincia-list'
class UsuarioList(generics.ListCreateAPIView):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer
    name = 'usuario-list'
class EtniaList(generics.ListCreateAPIView):
    queryset = Etnia.objects.all()
    serializer_class = EtniaSerializer
    name = 'etnia-list'
class ContenidoList(generics.ListCreateAPIView):
    queryset = Contenido.objects.all()
    serializer_class = ContenidoSerializer
    name = 'Contenido-list'
class Evidencia(generics.ListCreateAPIView):
    queryset = Evidencia.objects.all()
    serializer_class = EvidenciaSerializer
    name = 'evidencia-list'

class GeneroList(generics.ListCreateAPIView):
    queryset = Genero.objects.all()
    serializer_class = GeneroSerializer
    name = 'genero-list'

class TipoRequerimientoList(generics.ListCreateAPIView):
    queryset = TipoRequerimiento.objects.all()
    serializer_class = TipoRequerimientoSerializer
    name = 'tiporequerimiento-list'

#class Descarga
'''
class FileUploadView(views.APIView):
    parser_classes = (FileUploadParser,)
    def put(self, request, filename, format=None):
        file_obj = request.data['file']
        return Response(status=204)
'''

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'tiporequerimiento': reverse(TipoRequerimientoList.name, request=request),
            'provincias': reverse(ProvinciaList.name, request=request),
            'ciudades': reverse(CiudadList.name, request=request),
            'estados-civiles': reverse(EstadoCivilList.name, request=request),
            'niveles-educacion': reverse(NivelEducacionList.name, request=request),
            'genero': reverse(GeneroList.name,request=request),
            'etnias': reverse(EtniaList.name, request=request),
			'contenidos': reverse(ContenidoList.name, request=request),
			'usuarios': reverse(UsuarioList.name, request=request),
            'requerimiento': reverse(RequerimientoList.name, request=request),
			'evidencias': reverse(Evidencia.name, request=request),
            })