from escola.models import Estudante, Curso, Matricula
from rest_framework import viewsets, generics
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer 
from escola.throttles import AnonRateThrottleCustom

class EstudanteViewSet(viewsets.ModelViewSet):
    
    queryset = Estudante.objects.all().order_by('id')
    serializer_class = EstudanteSerializer  

class CursoViewSet(viewsets.ModelViewSet):
    
    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    queryset = Matricula.objects.all().order_by('id')   
    serializer_class = MatriculaSerializer
    throttle_classes = [AnonRateThrottleCustom]

class ListaMatriculasEstudanteViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculasCursoViewSet(generics.ListAPIView):

    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    serializer_class = ListaMatriculasCursoSerializer