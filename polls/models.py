from django.db import models
import datetime
from django.utils import timezone

# Crear modelos de la aplicación polls

# Modelo para representar una pregunta
class Question(models.Model):
    question_text = models.CharField(max_length=200)  # texto de la pregunta
    pub_date = models.DateTimeField('date published')  # fecha de publicación

    def __str__(self):
        return self.question_text

    # Comprueba si la pregunta fue publicada recientemente (dentro de las últimas 24 horas)
    def was_published_recently(self):
        return timezone.now() >= self.pub_date >= timezone.now() - datetime.timedelta(days=1)

# Modelo para representar una opción de respuesta a una pregunta
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # clave foránea hacia una pregunta
    choice_text = models.CharField(max_length=200)  # texto de la opción
    votes = models.IntegerField(default=0)  # votos

    def __str__(self):
        return self.choice_text
