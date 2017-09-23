from django.conf.urls import url
from cpccs import views

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^ciudades/$',
        views.CiudadList.as_view(),
        name=views.CiudadList.name),
    url(r'^estados-civiles/$',
        views.EstadoCivilList.as_view(),
        name=views.EstadoCivilList.name),
    url(r'^niveles-educacion/$',
        views.NivelEducacionList.as_view(),
        name=views.NivelEducacionList.name),
    url(r'^requerimiento/$',
        views.RequerimientoList.as_view(),
        name=views.RequerimientoList.name),
    url(r'^provincias/$',
        views.ProvinciaList.as_view(),
        name=views.ProvinciaList.name),
    url(r'^usuarios/$',
        views.UsuarioList.as_view(),
        name=views.UsuarioList.name),
    url(r'^etnias/$',
        views.EtniaList.as_view(),
        name=views.EtniaList.name),
    url(r'^contenidos/$',
        views.ContenidoList.as_view(),
        name=views.ContenidoList.name),
    url(r'^evidencias/$',
        views.Evidencia.as_view(),
        name=views.Evidencia.name),
    url(r'^$',
        views.ApiRoot.as_view(),
        name=views.ApiRoot.name)
]+static(settings.DENUNCIA_URL,document_root=settings.DENUNCIA_ROOT)
#url(r'^evidencias/uploads/([0-9]+)/([0-9]+)/([0-9]+)/(?P<filename>[^/]+)$', FileUploadView.as_view()),