from django.shortcuts import render
from apps.main.models import Setting, Gallary
# Create your views here.

def index(request):
    setting = Setting.objects.latest("id")
    gallary = Gallary.objects.all()
    return render(request, 'index.html', locals())

