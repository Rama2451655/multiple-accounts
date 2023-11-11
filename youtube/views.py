from django.shortcuts import render

# Create your views here.
def youtube(request):
  return render(request,'youtube.html')