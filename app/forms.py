from app.models import UsuarioModel, TarefaModel
from django.forms import ModelForm

class UsuarioModelForm(ModelForm):
    class Meta:
        model = UsuarioModel
        fields = ['nome', 'email', 'senha']
        
    def clean_nome(self):
        nome = self.cleaned_data['nome']
        return nome.upper()

class TarefaModelForm(ModelForm):
    class Meta:
        model = TarefaModel
        fields = ['titulo', 'descricao', 'data_conclusao']


    def clean_titulo(self):
            nome = self.cleaned_data['titulo']
            return nome.upper()
        