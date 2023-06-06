from django.shortcuts import render, get_object_or_404, HttpResponseRedirect

# Create your views here.
from django.http import HttpResponse
from .models import Question, Choice
from django.views import generic

from django.urls import reverse
from django.utils import timezone
#generic views, vista basadas en clases
class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return 5 questions recientes"""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by("-pub_date")[:5]

#vista para generar los detalles
class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


#vista para generar los resultados
class ResultView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"
# Vistas basadas en funciones 

# Vista principal
# def index(request):
#     # Obtener todas las preguntas más recientes
#     latest_question_list = Question.objects.all()
#     # Renderizar la plantilla index.html con la lista de preguntas
#     return render(request, "polls/index.html", {
#         "latest_question_list": latest_question_list
#     })
#     # return HttpResponse("Pagina principal de premios Platzi App")


#vista detalla de una pregunta
# def detail(request, question_id):
#     # Definir una función llamada 'detail' que toma una solicitud y un 'question_id' como argumentos
#     question = get_object_or_404(Question, pk=question_id)
#     # Obtiene el objeto 'Question' correspondiente al 'question_id' o muestra un error 404 si no se encuentra  
#     return render(request, "polls/detail.html",{
#         "question": question
#     })
#     # Renderiza la plantilla 'polls/detail.html' con el objeto 'question' como contexto y devuelve la respuesta
    
#     # return HttpResponse (f"Estas viendo la pregunta numero: {question_id}")


# #logica vista detalla de resultados
# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "polls/results.html", {
#         "question": question
#     })
    # return HttpResponse (f"Estas viendo los resultados de la pregunta numero: {question_id}")

# funtion views, Vistas basadas en funciones 
# Vista para votar
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)  # Obtiene la pregunta correspondiente al ID o muestra un error 404 si no existe
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])  # Obtiene la opción seleccionada por el usuario en la solicitud POST
    except (KeyError, Choice.DoesNotExist):
        # Si no se seleccionó ninguna opción válida, renderiza la página de detalles nuevamente con un mensaje de error
        return render(request, "polls/detail.html", {
            "question": question,
            "error_message": "Por favor selecciona una respuesta"
        })
    else:
        # Si se seleccionó una opción válida, incrementa el contador de votos para esa opción
        selected_choice.votes += 1
        selected_choice.save()  # Guarda los cambios en la base de datos
        # Redirige al usuario a la página de resultados de la pregunta actual
        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))


    # return HttpResponse (f"Estas votando a la pregunta numero: {question_id}")