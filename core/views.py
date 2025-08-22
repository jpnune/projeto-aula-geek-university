from django.shortcuts import render, redirect
from django.contrib import messages

from .forms import ContatoForm, ProdutoModelsForm
from .models import Produto


def index(request):
    context = {
        'produtos': Produto.objects.all()
    }

    return render(request, 'index.html', context)


def contato(request):
    form = ContatoForm(request.POST or None)

    print(request.POST) 

    if str(request.method) == 'POST':
        if form.is_valid():
            form.send_mail()
            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar mensagem.') 

    context = {
        'form': form
    }

    return render(request, 'contato.html', context=context)


def produto(request):

    if str(request.user) != 'AnonymousUser':
        if str(request.method) == 'POST':
            form = ProdutoModelsForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                messages.success(request, 'Produto cadastrado com sucesso!')
                form = ProdutoModelsForm()
            else:
                messages.error(request, 'Erro ao cadastrar produto.')
        else:
            form = ProdutoModelsForm()
        context = {
            'form': form
        }
    else:
        return redirect('index')
    return render(request, 'produto.html', context=context)
