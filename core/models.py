from django.db import models


class Base(models.Model):
    created_at = models.DateTimeField('Criado em', auto_now=True, auto_now_add=False)
    updated_at = models.DateTimeField('Atualizado em', auto_now=False, auto_now_add=True)
    active = models.BooleanField('Ativo?', default=True)


class Users(Base):
    GENDER_CHOICES = (
        ('M', 'Masculino'),
        ('F', 'Feminino'),
    )

    name = models.CharField('Nome', max_length=255, blank=False)
    sexo = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField('Idade', blank=False)
    hobby = models.TextField('Hobby', max_length=255, blank=False)
    birthdate = models.DateField('Data de nascimento', blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'
