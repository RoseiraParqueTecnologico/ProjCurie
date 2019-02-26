from django.urls import path, include

from rest_framework import routers


from siga_api.views import ProfessorViewSet, CursoViewSet, AlunoViewSet, DisciplinaViewSet, GradeDeAulasViewSet, LecionaViewSet

router = routers.DefaultRouter()
router.register('professor', ProfessorViewSet)
router.register('curso', CursoViewSet)
router.register('aluno', AlunoViewSet)
router.register('disciplina', DisciplinaViewSet)
router.register('grade-aulas', GradeDeAulasViewSet)
router.register('leciona', LecionaViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
