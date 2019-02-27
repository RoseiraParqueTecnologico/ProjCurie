from django.db import models


class Pessoa(models.Model):
    cpf = models.CharField(unique=True, max_length=11, primary_key=True)
    nome = models.CharField(max_length=40)
    endereco = models.TextField(blank=True, null=True)
    dt_nasc = models.DateField(blank=True, null=True)
    email_institucional = models.CharField(max_length=80, blank=True, null=True)
    senha = models.CharField(max_length=16, blank=True, null=True)

    class Meta:
        abstract = False


class Professor(Pessoa):
    rm = models.CharField(max_length=14)
    email_contato = models.CharField(max_length=80, blank=True, null=True)


class Curso(models.Model):
    # codigo = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=50)
    desc = models.TextField(blank=True, null=True)
    link_plano_pedagogico = models.CharField(max_length=100, 
                                             blank=True,
                                             null=True)
    coordenador = models.OneToOneField(Professor,
                                       models.DO_NOTHING,
                                       blank=True,
                                       null=True)


class Disciplina(models.Model):
    cod_disc = models.AutoField(primary_key=True)
    nome_disc = models.CharField(max_length=40)
    desc_disc = models.CharField(max_length=90)
    curso = models.ForeignKey(Curso, models.DO_NOTHING, blank=True, null=True)
    pre_requisitos = models.ManyToManyField('Disciplina')

    


class Aluno(Pessoa):
    ra = models.CharField(max_length=13)


class GradeDeAulas(models.Model):
    cod_grade_aulas = models.IntegerField(primary_key=True)
    periodo = models.CharField(max_length=10)
    formula = models.CharField(max_length=40, blank=True, null=True)
    cod_disc = models.OneToOneField(Disciplina, 
                                    on_delete=models.DO_NOTHING,
                                    blank=True, 
                                    null=True)


class Leciona(models.Model):
    tipo = models.CharField(max_length=15, blank=True, null=True)
    cpf_prof = models.OneToOneField(Professor, 
                                    models.DO_NOTHING)
    cod_grade_aulas = models.OneToOneField(GradeDeAulas,
                                           models.DO_NOTHING)

    class Meta:
        unique_together = (('cpf_prof', 'cod_grade_aulas'),)



class Aula(models.Model):
    data = models.DateField()
    grade_aulas = models.ForeignKey(GradeDeAulas, models.DO_NOTHING)
    descricao = models.TextField()