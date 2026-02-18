from django.contrib import admin
from django.urls import path, include
from escola.views import EstudanteViewSet, CursoViewSet, MatriculaViewSet, ListaMatriculasEstudanteViewSet, ListaMatriculasCursoViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'estudantes', EstudanteViewSet, basename='estudantes')
router.register(r'cursos', CursoViewSet, basename='cursos')
router.register(r'matriculas', MatriculaViewSet, basename='matriculas')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('estudantes/<int:pk>/matriculas/', ListaMatriculasEstudanteViewSet.as_view(), name='estudante-matriculas'),
    path('cursos/<int:pk>/matriculas/', ListaMatriculasCursoViewSet.as_view(), name='curso-matriculas'),
]
