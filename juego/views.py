from django.shortcuts import render

# Create your views here.
def juego_trivia(request):
    return render(request, 'juego/trivia.html', {})