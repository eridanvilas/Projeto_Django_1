from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.utils.translation import ugettext_lazy as _
from .models import Cliente, Produto, Cesta

class BootstrapAuthenticationForm(AuthenticationForm):
    username = forms.CharField(max_length=254,
                               widget=forms.TextInput({
                                   'class': 'form-control',
                                   'placeholder': 'Usuario'}))
    password = forms.CharField(label=_("Password"),
                               widget=forms.PasswordInput({
                                   'class': 'form-control',
                                   'placeholder':'Senha'}))

class ClienteForm (forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'telefone', 'email', 'estado', 'cidade', 'cep','numero']
        widgets = {
            'cpf': forms.TextInput(attrs={'class':'form-control','placeholder': 'CPF'}),
            'nome': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nome'}),
            'telefone': forms.TextInput(attrs={'class':'form-control','placeholder': 'Telefone'}),
            'email': forms.TextInput(attrs={'class':'form-control','placeholder': 'Email'}),
            'estado': forms.TextInput(attrs={'class':'form-control','placeholder': 'Estado'}),
            'cidade': forms.TextInput(attrs={'class':'form-control','placeholder': 'Cidade'}),
            'cep': forms.TextInput(attrs={'class':'form-control','placeholder': 'CEP'}),
            'numero': forms.TextInput(attrs={'class':'form-control','placeholder': 'Numero'}),
            }
      

class ProdutoForm (forms.ModelForm):
    class Meta:
        model = Produto
        fields =['codigo_barras', 'nome', 'descricao', 'preco', 'quantidade']
        widgets ={
            'codigo_barras': forms.TextInput(attrs={'class':'form-control','placeholder': 'Codigo De Barras'}),
            'nome': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nome'}),
            'descricao': forms.TextInput(attrs={'class':'form-control','placeholder': 'Descrição'}),
            'preco': forms.TextInput(attrs={'class':'form-control','placeholder': 'Preço'}),
            'quantidade': forms.TextInput(attrs={'class':'form-control','placeholder': 'Quantidade'}),
            }

class CestaForm (forms.ModelForm):
    class Meta:
        model = Cesta
        fields = '__all__'
        widgets ={
            'id': forms.TextInput(attrs={'class':'form-control','placeholder': 'ID'}),
            'nome': forms.TextInput(attrs={'class':'form-control','placeholder': 'Nome'}),
            'quantidade': forms.TextInput(attrs={'class':'form-control','placeholder': 'Quantidade'}),
            'preco': forms.TextInput(attrs={'class':'form-control','placeholder': 'Preço'}),
            'produtos': forms.CheckboxSelectMultiple(attrs={}),
            }


    
    
    
