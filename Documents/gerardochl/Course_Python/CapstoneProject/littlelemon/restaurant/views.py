from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import booking, menu, user
from .serializers import bookingSerializer, menuSerializer, UserSerializer

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
	
class MenuItemView(ListCreateAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    queryset = menu.objects.all()
    serializer_class = menuSerializer

class BookingViewSet(viewsets.ModelViewSet):
    queryset = booking.objects.all()
    serializer_class = bookingSerializer

class UserViewSet(viewsets.ModelViewSet):
   queryset = user.objects.all()
   serializer_class = UserSerializer
   permission_classes = [permissions.IsAuthenticated] 

#def sayHello(request):
 #return HttpResponse('Hello World')

#def menu(request):
#	menu_data = Menu.objects.all()
#	main_data = {"menu": menu_data}
#	return render(request, 'menu.html', {"menu": main_data})