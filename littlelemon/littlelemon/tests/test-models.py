from django.test import TestCase
from littlelemon.restaurant.views import MenuItemView

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItemView.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")