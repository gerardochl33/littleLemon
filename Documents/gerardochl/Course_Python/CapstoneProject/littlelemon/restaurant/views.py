from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import booking
from .serializers import bookingSerializer


# Create your views here.
def index(request):
 return render(request, 'index.html', {})

class bookingView(APIView):
	def get(self, request):
		items = booking.objects.all()
		serializer = bookingSerializer(item, many= True)
		return Response(serializer.data) # Return JSON

def post(self, request):
	serializer = menuSerializer(data=request.data)
	
	if serializer.is_valid():
		serializer.save()
		return Response({"status": "success", "data": serializer.data})
	
    
#def sayHello(request):
 #return HttpResponse('Hello World')

#def menu(request):
#	menu_data = Menu.objects.all()
#	main_data = {"menu": menu_data}
#	return render(request, 'menu.html', {"menu": main_data})