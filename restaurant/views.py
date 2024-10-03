from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from .models import Menu  # Assuming your menu model is in this app
from .serializers import MenuSerializer
from rest_framework import viewsets
from .models import Booking
from .serializers import BookingSerializer
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Create your views here.
def index(request):
    return render(request, 'index.html', {})



class MenuItemsView(ListCreateAPIView):
    """
    Handles GET and POST requests for the menu items.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer  # Replace with your actual menu serializer

class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
    """
    Handles GET, PUT, and DELETE requests for a single menu item.
    """
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer  # Replace with your actual menu serializer

    # You can override specific methods here if needed, e.g.,
    # def get_object(self):
    #     # ... custom logic to retrieve the object
    #     pass

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAuthenticated]
    