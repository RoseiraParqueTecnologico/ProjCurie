from rest_framework import serializers

from .models import Aluno, Curso, Pessoa, Professor, Disciplina, GradeDeAulas, Leciona, Atividade,Horarios_Aulas, Disciplina_Cursadas


class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {'senha': {'write_only': True}}
        model = Pessoa
        fields = ('cpf', 'nome', 'endereco', 'dt_nasc', 'email_institucional', 'senha')


class AlunoSerializer(PessoaSerializer):
    class Meta:
        extra_kwargs = {'senha': {'write_only': True}}
        model = Aluno
        fields = ('cpf', 'nome', 'endereco', 'dt_nasc', 'email_institucional', 
                  'ra')


class ProfessorSerializer(PessoaSerializer):
    class Meta:
        extra_kwargs = {'senha': {'write_only': True}}
        model = Professor
        fields = ('cpf', 'nome', 'endereco', 'dt_nasc', 'email_institucional', 
                  'rm', 'email_contato', 'senha')



class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        read_only_fields = ['codigo', ]
        fields =  '__all__'


class DisciplinaSerializer(serializers.ModelSerializer):
    pre_requisitos = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Disciplina.objects.all(),
        required=False
    )
    class Meta:
        extra_kwargs = {
            'pre_requisitos': {'required': False},
        }
        model = Disciplina
        read_only_fields = ['cod_disc', ]
        fields = ('cod_disc', 'nome_disc', 'desc_disc', 'curso', 'pre_requisitos')


class GradeDeAulasSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'cod_grade_aulas': {'required': False}
        }
        model = GradeDeAulas
        read_only_fields = ['cod_grade_aulas']
        fields = '__all__'


class LecionaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Leciona
        fields = '__all__'

class AtividadeSerializer(serializers.ModelSerializer):
    class Meta:
        read_only_fields = ['cod_ativ']
        model = Atividade
        fields = '__all__'

class Horarios_AulasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Horarios_Aulas
        fields = '__all__'

class Disciplina_CursadasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Disciplina_Cursadas
        fields = '__all__'