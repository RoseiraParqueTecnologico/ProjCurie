from django.urls import  path
from django.views.generic import TemplateView

urlpatterns = [
    path('alunos/cadastrar', 
         TemplateView.as_view(template_name='siga/cadastrar_aluno.html'),
         name='cadastrar_aluno'),
    path('cursos/cadastrar', 
         TemplateView.as_view(template_name='siga/cadastrar_curso.html'),
         name='cadastrar_curso'),
    path('coordenadores/cadastrar',
         TemplateView.as_view(template_name='siga/cadastrarcoordenador_.html'),
         name='cadastrar_coordenador'),
    path('disciplinas/cadastrar',
         TemplateView.as_view(template_name='siga/cadastrar_disciplina.html'),
         name='cadastrar_disciplina'),
    path('grade/cadastrar',
         TemplateView.as_view(template_name='siga/cadastrar_grade.html'),
         name='cadastrar_grade'),
    path('pre-requisitos/cadastrar',
         TemplateView.as_view(template_name='siga/cadastrar_pre_requisitos.html'),
         name='cadastrar_pre_requisitos'),
    path('professores/cadastrar',
         TemplateView.as_view(template_name='siga/cadastrar_professor.html'),
         name='cadastrar_professor'),
]
