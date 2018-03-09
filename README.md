# mttech
Desafio Mttech

# Configuração de Banco de dados
  Configure sua conexão com o banco de acordo com o exemplo abaixo:
  Arquivo settings.py
  
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mttech',
            'USER': 'mttech',
            'PASSWORD': '',
            'HOST': 'localhost',
            'PORT': '5432',
        }
    }

# Execução do projeto
  pip install requirements.txt <br/>
  python manage.py migrate <br/>
  python manage.py createsuperuser <br/>
  python manage.py runserver <br/>

# Acesso ao sistema
  http://localhost:8000

# Demonstração
  http://desafio-mttech.t01.com.br <br/>
  
  **Perfil Administrador**<br/>
    Usuário: admin <br/>
    Senha: testemttech <br/>
  
  **Perfil Empresa**<br/>
    Usuário: empresa01 <br/>
    Senha: emp123 <br/>
  
  **Perfil Advogado**<br/>
    Usuário: advogado01 <br/>
    Senha: adv123 <br/>
  
