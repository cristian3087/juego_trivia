from django.shortcuts import render
from django.core.paginator import Paginator
from juego.models import Pregunta

# Create your views here.
def juego_trivia(request):
    data = {}
    quiz_data = Pregunta.objects.all().order_by('?')[:10]
    page = 1  
    paginador = Paginator(quiz_data,1)
    preguntas = paginador.get_page(page)
    if request.method == 'POST':
      print('POST:', request.POST)
      page = request.POST.get('page')
      paginador = Paginator(quiz_data,1)
      preguntas = paginador.get_page(page)
      data['preguntas'] = preguntas 
      data['total'] = paginador.num_pages
      return render(request, 'juego/trivia.html', data)

    
    data['preguntas'] = preguntas 
    data['total'] = paginador.num_pages
    return render(request, 'juego/trivia.html', data)