# Aqui temos a importação, semelhante ao import algumaCoisa from 'lib';

from django.conf import settings
from django.db import models
from django.utils import timezone

# Essa linha define o nosso model (um objeto)
# class -> é uma palavra-chave especial que indica que estamos definindo um objeto;
# Post -> é o nome do nosso modelo. Nós podemos dar um nome diferente (mas precisamos evitar caracteres especiais e espaços em branco). Sempre inicie o nome de uma classe com uma letra em maiúsculo.
# models.Model -> O post é um modelo de Django, sendo assim, ele sabe que deve ser salvo no banco de dados;

class Post(models.Model):
    
    # models.ForeignKey -> um link para outro modelo;
    # models.CharField -> é assim que definimos um texto com um número limitado de caracteres;
    # models.TextField -> um campo para texto sem limite fixo
    # models.DateTimeField -> data e hora;

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    create_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def publish(self):
        self.published_date = timezone.now()
        self.save()
        
    def __str__(self):
        return self.title