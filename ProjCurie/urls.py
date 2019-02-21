from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

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
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    path('alunos/', include('siga.urls')),
    path('', TemplateView.as_view(template_name='siga/index.html'))
    # path('', include('rest_framework.urls')),
]
