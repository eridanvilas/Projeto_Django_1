from datetime import datetime
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpRequest
from django.views.generic import ListView,CreateView, DeleteView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .forms import ClienteForm, ProdutoForm, CestaForm
from .models import Cliente,Produto,Cesta
from django.forms import modelformset_factory

@login_required(login_url='/login')
def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Pagina Inicial',
            'year':datetime.now().year,
        }
 )

@login_required(login_url='/login')
def lista_cliente(request):
    clientes = Cliente.objects.all()
    search = request.GET.get('search')
    if search:
        clientes = objects.filter(nome__icontains=search)
    contexto = {'clientes': clientes}
    return render(request, "app/cliente.html", contexto)

@login_required(login_url='/login')
def cliente_form(request, cpf=0):
    if request.method == "GET":
        if cpf==0:
            form = ClienteForm()
        else:
            cliente = Cliente.objects.get(pk=cpf)
            form = ClienteForm(instance=cliente)
        return render(request,"app/criarcliente.html",{'form':form})
    else:
        if cpf == 0:
            form = ClienteForm(request.POST)
        else:
            cliente = Cliente.objects.get(pk=cpf)
            form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
        return redirect('/cliente')

@login_required(login_url='/login')
def cliente_update(request, cpf):
    cliente = get_object_or_404(Cliente, pk=cpf)
    form = ClienteForm(instance=cliente)

    if(request.method =='POST'):
        form = ClienteForm(request.POST, instance=cliente)

        if form.is_valid():
            cliente.save()
            return redirect('/cliente')
        else:
            return render(request, 'app/criarcliente.html', {'form': form, 'cliente': cliente})
    else:
        return render(request, 'app/criarcliente.html', {'form': form, 'cliente': cliente})

@login_required(login_url='/login')
def cliente_delete(request, cpf):
    cliente = get_object_or_404(Cliente, pk=cpf)
    cliente.delete()
    return redirect('/cliente')

@login_required(login_url='/login')
def lista_produto(request):
    produtos = Produto.objects.all()
    search = request.GET.get('search')
    if search:
        produtos=produtos.filter(nome__icontains=search)
    contexto = {'produtos': produtos}
    return render(request, "app/produto.html", contexto)

@login_required(login_url='/login')
def produto_form(request, codigo_barras=0):
    if request.method == "GET":
        if codigo_barras==0:
            form = ProdutoForm()
        else:
            produto = Produto.objects.get(pk=codigo_barras)
            form = ProdutoForm(instance=produto)
        return render(request,"app/criarproduto.html",{'form':form})
    else:
        if codigo_barras == 0:
            form = ProdutoForm(request.POST)
        else:
            produto = Produto.objects.get(pk=codigo_barras)
            form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
        return redirect('/produto')

@login_required(login_url='/login')
def produto_update(request, codigo_barras):
    produto = get_object_or_404(Produto, pk=codigo_barras)
    form = ProdutoForm(instance=produto)

    if(request.method =='POST'):
        form = ProdutoForm(request.POST, instance=produto)

        if form.is_valid():
            produto.save()
            return redirect('/produto')
        else:
            return render(request, 'app/criarproduto.html', {'form': form, 'produto': produto})
    else:
        return render(request, 'app/criarproduto.html', {'form': form, 'produto': produto})


@login_required(login_url='/login')
def produto_delete(request, codigo_barras):
    produto = get_object_or_404(Produto, pk=codigo_barras)
    produto.delete()
    return redirect('/produto')

@login_required(login_url='/login')
def cesta_form(request):
    if request.method == "GET":
        form = CestaForm()
        return render(request,"app/criarcesta.html",{'form':form})
    else:
        form = CestaForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/cesta')

@login_required(login_url='/login')
def lista_cesta(request):
    cestas = Cesta.objects.all()
    contexto = {'cestas': cestas
               }
    return render(request, "app/cestas.html", contexto)
