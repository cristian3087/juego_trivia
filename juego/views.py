from django.shortcuts import render

# Create your views here.
def juego_trivia(request):
    print(request.method)
    print(request.POST)
    return render(request, 'juego/trivia.html', {})