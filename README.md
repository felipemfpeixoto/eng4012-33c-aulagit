# eng4012-33c-aulagit
SECRET_KEY:
 - python
 - import secrets
 - secrets.token_urlsafe(32)

Criar app:
 - python manage.py startapp <nomedoapp>
 
Registrando os modelos no banco de dados:
 - python manage.py makemigrations <nomedoapp>
 - python manage.py migrate
 
Roda o código:
 - python3 manage.py run server
