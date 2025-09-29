from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def dashboard(request):
   #return HttpResponse("Welcome to your dashboard!")
    return render(request,'mainApp/dashboard.html')