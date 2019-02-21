from django.urls import  path
from django.views.generic import TemplateView

urlpatterns = [
    path('cadastrar', TemplateView.as_view(template_name='siga/cadastrar_aluno.html')),

]
