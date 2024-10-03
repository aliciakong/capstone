from django.test import TestCase
from restaurant.models import Menu
from restaurant.views import MenuItemsView
from restaurant.serializers import MenuSerializer
from decimal import Decimal

class MenuViewTest(TestCase):
    def setUp(self):
        """
        Create a few test menu objects for testing.
        """
        self.menu1 = Menu.objects.create(Title = 'Burger', Price = 12.50, Inventory = 5)
        self.menu2 = Menu.objects.create(Title = 'Salad', Price = 12.50, Inventory = 10)
    
    def test_getall(self):
        """
        Test retrieving all Menu objects and verifying their serialized data.
        """
        # Simulate a GET request to the MenuItemsView
        response = self.client.get('/menu/')

        # Check for successful response status code (e.g., 200 OK)
        self.assertEqual(response.status_code,200)

        # Get the serialized data from the response
        serialized_data = response.data
        self.assertEqual(len(serialized_data),2)

        # Loop through the serialized data and compare with test objects
        for i,item in enumerate(serialized_data):
            # Assuming your MenuSerializer serializes all fields
            self.assertEqual(item['Title'],self.menu1.Title if i ==0 else self.menu2.Title)
            
            self.assertEqual(Decimal(item['Price']), self.menu1.Price if i == 0 else self.menu2.Price)
            self.assertEqual(Decimal(item['Inventory']), self.menu1.Inventory if i == 0 else self.menu2.Inventory)