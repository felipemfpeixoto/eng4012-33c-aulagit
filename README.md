# eng4012-33c-aulagit
secrets:
 - key = 'SECRET_KEY'
 - value = <código copiado>

 - Criar o primeiro projeto Django;
  - Setar a SECRET_KEY:
   - shell:
    - python
    - import secrets
    - secrets.token_urlsafe(32) (copiar o código retornado)
   - Secrets:
    - key = 'SECRET_KEY'
    - value = <codigoCopiado> 
 - Lembrar de configurar a SECRET_KEY no replit;
 - Criar o app através do comando python3 manage.py startapp <nomedoapp> no Shell;
 - Criar a primeira view que chame o HTML da pasta templates;
 - Criar a pasta templates e adicionar o link dela no settings.py;
 - Dentro da pasta templates botar o arquivo HTML da Atividade Individual 01;

Roda o código:
 - python3 manage.py run server
