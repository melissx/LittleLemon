from unittest import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu1 = Menu.objects.create(name='Menu 1', description='Description 1')
        self.menu2 = Menu.objects.create(name='Menu 2', description='Description 2')

    def test_getall(self):
        response = self.client.get('/api/menus/')
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)