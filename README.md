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
  
  Usuário: admin
  Senha: testemttech
