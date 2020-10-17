from django.shortcuts import render, HttpResponse

# Create your views here.
base = """
<h1>Mi Web Personal</h1>
<ul>
    <li><a href = "/">Portada</a></li>
    <li><a href ="/about/">Acerca de mi</a></li>
    <li><a href = "/portafolio/">Portafolio</a></li>
    <li><a href ="/contacto/">Contacto</a></li>
</ul>
"""
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")    

def contacto(request):
    return render(request, "core/contact.html")