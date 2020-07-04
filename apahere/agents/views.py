from django.shortcuts import render

# Create your views here.
def agents_page(request):
    return render(request, 'agents.html')