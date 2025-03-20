## Comandos

Verficar versão do python instalada:
````
phyton --version
````

Verficar versão do Django:
````
phyton -m django --version
````

Instalar Django:
````
phyton -m pip intall Django
````

Iniciar um novo projeto Django chamado mysite:
````
django-admin startproject mysite
````

Executar meu projeto no servidor de desenvolvimento em localhost:8000:
````
python manage.py runserver
````
Observacao: Atalho para encerrar o servidor no prompt:
````
CTRL+C
````

Iniciar uma nova app chamada core:
````
python manage.py startapp core
````

Defina o modelo da tabela na base de dados do models.py:
````
from django.db import models 
from django.contrib.auth.models import AbstractUser 
    
    class Usuario(AbstractUser): 
        telefone = models.CharField(max_length=15, blank=True, null=True) 
        endereco = models.TextField(blank=True, null=True) 
        
        def __str__(self): return self.first_name or self.username 
````
Observação: Usuario: Representa os participantes de um evento, armazenando informações pessoais.

Explicação: 
• Herdamos AbstractUser, o que nos permite manter os campos padrão (username, email, password etc.). 
• Adicionamos telefone e endereco como campos personalizados. 
• O método __str__ retorna o nome do usuário, tornando a exibição mais amigável. 
````

abra a pasta settings.py e adicione na coluna 31: 
````
AUTH_USER_MODEL ="core.Usuario"
````
adicione tambem o core após 'django.contrib.staticfiles', :
````
'core',
````

Após definir o modelo, precisamos aplicá-lo a base de dados:
````
python manage.py makemigrations
python manage.py migrate
````

Iniciar a Shell do Python:
````
python manage.py shell
````
Observacao: Atalho para sair do shell:
````
exit()
````
Criando um Usuário no Shell:
````
from core.models import Usuario
````
Criar um novo usuário:
````
usuario1 = Usuario.objects.create(nome="joao",
email="joao@email.com")
````
Verificar os dados do usuário criado:
````
print(usuario1)
print(usuario1.nome)
print(usuario1.email)
````
Alterar dados e gravar:
````
usuario1.nome = “jose”
usuario1.save()
````

Apos a class modelo Usuario vamos criar mais dois modelos interligados: 
´´´´
Evento: Representa um evento específico com data e título
Escala: Liga os usuários a um evento específico, registrando sua participação.
````
Vamos esternde-los assim:
````
    class Evento(models.Model): 
        titulo = models.CharField(max_length=200) 
        data = models.DateField() 
    
    def __str__(self): return f"{self.titulo} - {self.data}"
````
Explicação: 

• titulo: Nome do evento (ex: "Culto de Domingo", "Ensaio de Louvor"). 
• data: Data do evento. 
• O método __str__ retorna o título e a data do evento. 
````
class Escala(models.Model): 
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name="escalas", verbose_name="Evento") 
    participantes = models.ManyToManyField(Usuario, related_name="escalas", verbose_name="Participantes", blank=True) 

def __str__(self): return f"Escala para {self.evento.titulo} ({self.evento.data})" 
````
Explicação: 
• evento = models.ForeignKey(Evento, on_delete=models.CASCADE): Relaciona a escala a um único evento.  o on_delete=models.CASCADE: Se o evento for excluído, a escala também será. o related_name="escalas": Permite acessar todas as escalas de um evento com evento.escalas.all(). 
• participantes = models.ManyToManyField(Usuario): Define um relacionamento muitos-para-muitos entre usuários e escalas.  
o related_name="escalas": Permite acessar todas as escalas de um usuário com usuario.escalas.all(). 
• O método __str__ retorna o título do evento associado à escala. 
````



Cria super utilizador para django admin
````
python manage.py createsuperuser
````
 
## Dicionário de conceitos

### Full Stack Web Development
Desenvolvimento de sites e aplicações para a web, envolvendo front-end, back-end e banco de dados.

### ORM (Object-Relational Mapping)
Uma técnica que permite interagir com bancos de dados usando código em vez de SQL puro.

### SQL Injection XSS (Cross-Site Scripting)
Injeção de scripts maliciosos em páginas da web para roubar dados ou manipular usuários.

### Framework
Um conjunto de ferramentas e bibliotecas que facilita o desenvolvimento, fornecendo estrutura e funcionalidades prontas.
Acelera o desenvolvimento, padroniza código, melhora a manutenção e oferece segurança integrada.