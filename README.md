# eng4012-33c-aulagit
Setar a SECRET_KEY:

shell:
 - python
 - import secrets
 - secrets.token_urlsafe(32)
 (copiar o código retornado)

secrets:
 - key = 'SECRET_KEY'
 - value = <código copiado>

Criando o app:

shell: 
 - exit()
 - python manage.py startapp <nomedoapp>

CRIAR A VIEW QUE CHAME O HTML:

Roda o código:
 - python3 manage.py run server
