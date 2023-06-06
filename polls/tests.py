import datetime
from django.test import TestCase
from django.utils import timezone
from .models import Question

# # Create your tests here.
# class QuestionModelTests(TestCase):
#     def test_was_published_recently_with_future_questions(self):
#         """Comprueba si 'was_published_recently' devuelve False para preguntas futuras."""
        
#         # Obtén la fecha y hora actual y agrega 30 días para obtener una fecha futura
#         time = timezone.now() + datetime.timedelta(days=30)
        
#         # Crea una nueva pregunta con el texto y la fecha futura
#         future_question = Question(question_text="¿Quien es el mejor CD de platzi?", pub_date=time)
        
#         # Comprueba si el método 'was_published_recently' devuelve False para preguntas futuras
#         self.assertIs(future_question.was_published_recently(), False)

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_questions(self):
        """Comprueba si 'was_published_recently' devuelve False para preguntas futuras."""

        # Obtiene la fecha y hora actual
        current_time = timezone.now()

        # Crea una nueva pregunta con la fecha actual
        current_question = Question(question_text="¿Quien es el mejor CD de platzi?", pub_date=current_time)
        
        # Comprueba si el método 'was_published_recently' devuelve True para preguntas creadas en el presente
        self.assertIs(current_question.was_published_recently(), True)

        # Obtiene la fecha y hora de hace 2 días
        past_time = current_time - datetime.timedelta(days=2)

        # Crea una nueva pregunta con la fecha pasada
        past_question = Question(question_text="¿Quien es el mejor CD de platzi?", pub_date=past_time)

        # Comprueba si el método 'was_published_recently' devuelve False para preguntas creadas en el pasado
        self.assertIs(past_question.was_published_recently(), False)

        # Obtiene la fecha y hora dentro de 2 días en el futuro
        future_time = current_time + datetime.timedelta(days=2)

        # Crea una nueva pregunta con la fecha futura
        future_question = Question(question_text="¿Quien es el mejor CD de platzi?", pub_date=future_time)

        # Comprueba si el método 'was_published_recently' devuelve False para preguntas creadas en el futuro
        self.assertIs(future_question.was_published_recently(), False)
