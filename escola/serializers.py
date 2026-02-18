from rest_framework import serializers
"""
Serializer para listar as matrículas de um curso.
Este serializer é utilizado para serializar dados de matrícula, exibindo
o nome do estudante matriculado em um curso específico. Fornece uma visão
simplificada das informações de matrícula focando na identificação do
estudante.
Attributes:
    estudante (ReadOnlyField): Campo somente leitura que retorna o nome
        do estudante associado à matrícula através do relacionamento
        'estudante.nome'.
Meta:
    model (Matricula): Define que o serializer trabalha com o modelo Matricula.
    fields (list): Lista de campos a serem incluídos na serialização.
        - 'estudante_nome': O nome do estudante da matrícula.
Note:
    Há uma inconsistência: o atributo `estudante` está mapeado para
    'estudante.nome', mas o campo em `fields` referencia 'estudante_nome'.
    Considere alinhar os nomes para evitar erros de serialização.
"""
from escola.models import Estudante, Curso, Matricula

class EstudanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Estudante
        fields = ['id', 'nome', 'email', 'cpf', 'data_nascimento', 'celular']

class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Matricula
        exclude = []

class ListaMatriculasEstudanteSerializer(serializers.ModelSerializer):
    # curso = serializers.CharField(source='curso.descricao')
    # periodo = serializers.CharField(source='get_periodo_display')
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()
    
#Listar as matriculas de um curso, mostrando o nome do estudante e o período da matrícula
class ListaMatriculasCursoSerializer(serializers.ModelSerializer):
    estudante_nome = serializers.ReadOnlyField(source='estudante.nome')

    class Meta:
        model = Matricula
        fields = ['estudante_nome']