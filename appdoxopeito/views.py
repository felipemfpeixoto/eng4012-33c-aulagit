from django.shortcuts import render, redirect
from .models import Title
from .models import Person

def home(request):
  titles = Title.objects.all()
  people = Person.objects.all()
  context = { "titles": titles, "people": people }
  return render(request, "home.html", context=context)

def list_titles(request):
  titles = Title.objects.all()
  context = { "titles": titles }
  return render(request, "list_titles.html", context=context)

def create_title(request):
  if request.method == "POST":
    Title.objects.create(
      title=request.POST["title"],
      description=request.POST["description"],
      due_date=request.POST["due-date"],
      done=False
    )
    return redirect("titles-list")
  
  return render(request, "titles_form.html")

def list_people(request):
  people = Person.objects.all()
  context = { "people": people }
  return render(request, "list_people.html", context=context)

def create_person(request):
  if request.method == "POST":
    Person.objects.create(
      title=request.POST["title"],
      birth_date=request.POST["birth_date"],
      due_date=request.POST["due-date"],
      sex=request.POST["sex"],
    )
    return redirect("people-list")
  
  return render(request, "people_form.html")

def edit_title(request, item_id):
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

def remove_title(request, item_id):
    item = Title.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('titles-list')
    else:
        return render(request, 'remove_title.html', {'titles': item})

def edit_person(request, item_id):
    item = Person.objects.get(id=item_id)
    if request.method == 'POST':
        item.texto = request.POST['texto']
        item.save()
        return redirect('people-list')
    else:
        return render(request, 'people_form.html', {'people': item})

def remove_person(request, item_id):
    item = Person.objects.get(id=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('people-list')
    else:
        return render(request, 'remove_person.html', {'people': item})