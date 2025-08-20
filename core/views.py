from django.shortcuts import render
from django.contrib import messages

from .forms import ContatoForm

def index(request):
    return render(request, 'index.html')


def contato(request):
    form = ContatoForm(request.POST or None)

    print(request.POST) 

    if str(request.method) == 'POST':
        if form.is_valid():
            nome = form.cleaned_data.get('nome')
            email = form.cleaned_data.get('email')
            assunto = form.cleaned_data.get('assunto')
            mensagem = form.cleaned_data.get('mensagem')

            print("Mensagem enviada!")
            print(f'Nome: {nome}')
            print(f'Email: {email}')
            print(f'Assunto: {assunto}')
            print(f'Mensagem: {mensagem}')

            messages.success(request, 'Mensagem enviada com sucesso!')
            form = ContatoForm()
        else:
            messages.error(request, 'Erro ao enviar mensagem.') 

    context = {
        'form': form
    }

    return render(request, 'contato.html', context=context)


def produto(request):
    return render(request, 'produto.html')
