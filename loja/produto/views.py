from django.shortcuts import render
from django.views.generic.list import ListView
from django.views import View
from django.http import HttpResponse
from produto.models import Produto 

class ListaProdutos(ListView):
    model = Produto
    template_name = 'produto/lista.html'    
    context_object_name = 'produtos'

class DetalheProduto(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Detalhe produto')

class AdicionarCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Adicionar carrinho')

class RemoverCarrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Remover carrinho')

class Carrinho(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Carrinho')

class Finalizar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('Finalizar')

