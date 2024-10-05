from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
 return HttpResponse('Hello World')

def menu(request):
	menu_data = Menu.objects.all()
	main_data = {"menu": menu_data}
	return render(request, 'menu.html', {"menu": main_data})