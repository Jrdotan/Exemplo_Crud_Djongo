

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import posts
# Create your views here.
 
# função de inserção CRUD
def add_post(request):
    tit = request.POST.get("titulo")
    descript = request.POST.get("descricao")
    post = posts(titulo=tit,descricao=descript)
    post.save()
    return HttpResponse("inserido")

# função de leitura no CRUD
def read_post(request):
    postou = posts.objects.all()
    responde = []
    for post in postou:
        responde.append({"titulo":post.titulo, "descrição":post.descricao})
    return JsonResponse(responde, safe=False )


#função de atualização no CRUD
def update_post(request):
    id = request.POST.get("id")
    titulo = request.POST.get("titulo")
    descricao = request.POST.get("descricao")
    postou = posts.objects.get(id=id)
    postou.titulo = titulo
    postou.descricao = descricao
    postou.save()
    return HttpResponse("Atualizado")

#função de deletar no CRUD

def delete_post(request):
    id = request.POST.get("id")
    postou = posts.objects.get(id=id)
    postou.delete()
    return HttpResponse("Deletado")

def home(request):
    postou = posts.objects.all() # capturar todos os posts
    return render(request, 'index.html', {"posts": postou})  # Renderiza o template HTML