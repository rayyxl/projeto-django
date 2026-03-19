from django.shortcuts import render, redirect
from .models import Pessoa
from .forms import PessoaForm

def home(request):
    print("Acessou a home")
    return render(request, 'home.html')

def listar_pessoas(request):
    pessoas = Pessoa.objects.all()
    return render(request, 'listar_pessoas.html', {'pessoas': pessoas})

def criar_pessoa(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        
        if form.is_valid():
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm()
        
    return render(request, 'criar_pessoa.html', {'form': form})


def atualizar_pessoa(request, id):
    pessoa = Pessoa.objects.get(pk=id)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():     
            form.save()
            return redirect('listar_pessoas')
    else:
        form = PessoaForm(instance=pessoa)
        
    return render(request, 'criar_pessoa.html', {'form': form})

def deletar_pessoa(request, id):
    pessoa = Pessoa.objects.get(pk=id)
    if request.method == "POST":
        pessoa.delete()
        return redirect('listar_pessoas')
    return render(request, 'confirmar_delete.html', {'pessoa': pessoa})