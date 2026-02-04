from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required # This is "Logic Building" — it blocks anyone not logged in
def index(request):
    return render(request, 'dashboard/index.html')