from django.shortcuts import render
from django.core.paginator import Paginator

# Create your views here.
def juego_trivia(request):
    data = {}
    quiz_data = [
                {
                    "image_link": "https://st3.idealista.com/news/archivos/styles/amp_1200x675_16_9/public/2023-10/images/francia_en_otono.jpg",
                    "question": "¿Cuál es la capital de Francia?",
                    "answers": ["París", "Londres", "Berlín", "Madrid"]
                },
                {
                    "image_link": "https://cdn.pixabay.com/photo/2017/09/01/00/16/png-2702697_1280.png",
                    "question": "¿Qué planeta es conocido como el Planeta Rojo?",
                    "answers": ["Tierra", "Marte", "Júpiter", "Saturno"]
                },
                {
                    "image_link": "https://cdn.pixabay.com/photo/2017/09/01/00/16/png-2702697_1280.png",
                    "question": "¿Quién escribió 'Matar a un ruiseñor'?",
                    "answers": ["Harper Lee", "Jane Austen", "Mark Twain", "Ernest Hemingway"]
                },
                {
                    "image_link": "https://example.com/image4.jpg",
                    "question": "¿Cuál es el océano más grande de la Tierra?",
                    "answers": ["Océano Atlántico", "Océano Índico", "Océano Ártico", "Océano Pacífico"]
                }
            ]
    page = request.GET.get('page')
    paginador = Paginator(quiz_data,1)
    preguntas = paginador.get_page(page)
    data['preguntas'] = preguntas 
    data['total'] = paginador.num_pages
    return render(request, 'juego/trivia.html', data)

