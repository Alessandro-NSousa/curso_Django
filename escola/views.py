from escola.models import Estudante, Curso, Matricula
from rest_framework import viewsets, generics
from escola.serializers import EstudanteSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasEstudanteSerializer, ListaMatriculasCursoSerializer 
from escola.throttles import AnonRateThrottleCustom

class EstudanteViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de estudantes.

    Campos de ordenação:
    - nome: permite ordenar os resultados por nome.

    Campos de pesquisa:
    - nome: permite pesquisar os resultados por nome.
    - cpf: permite pesquisar os resultados por CPF.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE

    Classe de Serializer:
    - EstudanteSerializer: usado para serialização e desserialização de dados.
    - Se a versão da API for 'v2', usa EstudanteSerializerV2.
    """
    
    queryset = Estudante.objects.all().order_by('id')
    serializer_class = EstudanteSerializer  

class CursoViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de cursos.

    Métodos HTTP Permitidos:
    - GET, POST, PUT, PATCH, DELETE
    """

    queryset = Curso.objects.all().order_by('id')
    serializer_class = CursoSerializer

class MatriculaViewSet(viewsets.ModelViewSet):
    """
    Descrição da ViewSet:
    - Endpoint para CRUD de matrículas.

    Métodos HTTP Permitidos:
    - GET, POST

    Throttle Classes:
    - MatriculaAnonRateThrottle: limite de taxa para usuários anônimos.
    - UserRateThrottle: limite de taxa para usuários autenticados.
    """

    queryset = Matricula.objects.all().order_by('id')   
    serializer_class = MatriculaSerializer
    throttle_classes = [AnonRateThrottleCustom]

class ListaMatriculasEstudanteViewSet(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Estudante
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):
        queryset = Matricula.objects.filter(estudante_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasEstudanteSerializer

class ListaMatriculasCursoViewSet(generics.ListAPIView):
    """
    Descrição da View:
    - Lista Matriculas por id de Curso
    Parâmetros:
    - pk (int): O identificador primário do objeto. Deve ser um número inteiro.
    """

    def get_queryset(self):
        
        queryset = Matricula.objects.filter(curso_id=self.kwargs['pk']).order_by('id')
        return queryset
    
    serializer_class = ListaMatriculasCursoSerializer