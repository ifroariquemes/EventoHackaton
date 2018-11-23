from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def event_view(request):
    titulo = 'Eventos'
    return render(request, 'event_view.html', {'titulo' : titulo})

def event(request):
    titulo = 'Eventos'
    return render(request, 'event.html', {'titulo' : titulo})

def accreditation(request):
    titulo = 'Eventos'
    return render(request, 'accreditation.html', {'titulo': titulo})

def user(request):
    titulo = 'Usuários'
    return render(request, 'user.html', {'titulo': titulo})

def user_edit(request):
    titulo = 'Usuários'
    return render(request, 'user_edit.html', {'titulo': titulo})

def organization_edit(request):
    titulo = 'Organizações'
    return render(request, 'organization_edit.html', {'titulo': titulo})

def frequency(request):
    titulo = 'Eventos'
    return render(request, 'frequency.html', {'titulo': titulo})

def event_edit(request):
    titulo = 'Eventos'
    return render(request, 'event_edit.html', {'titulo': titulo})

def organizations(request):
    titulo = 'Organizações'
    return render(request, 'organizations.html', {'titulo': titulo})

def activity(request):
    titulo = 'Organizações'
    return render(request, 'organizations.html', {'titulo': titulo})