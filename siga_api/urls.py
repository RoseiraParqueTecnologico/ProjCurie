from django.urls import path, include

from rest_framework import routers


from siga_api.views import ProfessorViewSet, CursoViewSet, AlunoViewSet, DisciplinaViewSet, GradeDeAulasViewSet, LecionaViewSet, AtividadeViewSet,Horarios_AulasViewSet,AulaViewSet

router = routers.DefaultRouter()
router.register('professor', ProfessorViewSet)
router.register('curso', CursoViewSet)
router.register('aluno', AlunoViewSet)
router.register('disciplina', DisciplinaViewSet)
router.register('grade-aulas', GradeDeAulasViewSet)
router.register('leciona', LecionaViewSet)
router.register('aula', AulaViewSet)
router.register('Atividade', AtividadeViewSet)
router.register('Horario_aulas', Horarios_AulasViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
