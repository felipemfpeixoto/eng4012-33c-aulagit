from django.shortcuts import render, redirect
from .models import Title
from .models import Person

# Django views são funções em python que recebem http requests e retornam http response, como documentos HTML.

def home(request): # view da página principal
  titles = Title.objects.all() # pega todos os elementos Title do banco de dados
  people = Person.objects.all() # pega todos os elementos Person do banco de dados
  context = { "titles": titles, "people": people } # associa os nomes usados no HTML às variáveis criadas anteriormente
  return render(request, "home.html", context=context) # retorna o html

def list_titles(request): # view da lista de títulos
  titles = Title.objects.all()
  context = { "titles": titles }
  return render(request, "list_titles.html", context=context) # retorna o html da lista de títulos

def create_title(request): # view para criar um título
  if request.method == "POST":
    Title.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      due_date=request.POST["due-date"],
      done=False
    ) # Pega todas as infs necessárias para um título segundo o models e envia p banco de dados
    return redirect("titles-list") # redireciona para a lista de títulos, com o título criado incluso na lista
  
  return render(request, "titles_form.html")

def list_people(request): # lista de pessoas, funciona igual à lista de títulos
  people = Person.objects.all()
  context = { "people": people }
  return render(request, "list_people.html", context=context)

def create_person(request): # cria pessoa no banco de dados, anàloga à create_title() anterior
  if request.method == "POST":
    Person.objects.create(
      title=request.POST["title"],
      birth_date=request.POST["birth_date"],
      due_date=request.POST["due-date"],
      sex=request.POST["sex"],
    )
    return redirect("people-list")
  
  return render(request, "people_form.html")

def edit_title(request, item_id): # edita título 
    item = Title.objects.get(id=item_id)
    item.due_date = item.due_date.strftime('%Y-%m-%d')

    if request.method == "POST":
        item.title = request.POST["title"]
        item.description = request.POST["description"]
        item.due_date = request.POST["due-date"]
        if "done" not in request.POST:
            item.done = False
        else:
            item.done = True
        item.save() 
        return redirect("titles-list")

    return render(request, "titles_form.html", context={"titles": item})

def remove_title(request, item_id): # Deleta título do banco de dados
    item = Title.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('titles-list')
    else:
        return render(request, 'remove_title.html', {'titles': item})

def edit_person(request, item_id): # edita pessoa no banco de dados 
    item = Person.objects.get(id=item_id)
    if request.method == 'POST':
        item.texto = request.POST['texto']
        item.save()
        return redirect('people-list')
    else:
        return render(request, 'people_form.html', {'people': item})

def remove_person(request, item_id): # Remove pessoa do banco de dados
    item = Person.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('people-list')
    else:
        return render(request, 'remove_person.html', {'people': item})