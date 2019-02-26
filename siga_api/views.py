from django.shortcuts import render
from .models import Aluno, Curso, Professor, Disciplina, GradeDeAulas, Leciona
from .serializers import ProfessorSerializer, CursoSerializer, AlunoSerializer, DisciplinaSerializer, GradeDeAulasSerializer, LecionaSerializer
from rest_framework import viewsets


class ProfessorViewSet(viewsets.ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AlunoViewSet(viewsets.ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class DisciplinaViewSet(viewsets.ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer


    def get_queryset(self):
        queryset = Disciplina.objects.all()
        curso = self.request.query_params.get('curso', None)
        if curso is not None:
            queryset = queryset.filter(curso=curso)
        return queryset

class GradeDeAulasViewSet(viewsets.ModelViewSet):
    queryset = GradeDeAulas.objects.all()
    serializer_class = GradeDeAulasSerializer

class LecionaViewSet(viewsets.ModelViewSet):
    queryset = Leciona.objects.all()
    serializer_class = LecionaSerializer
