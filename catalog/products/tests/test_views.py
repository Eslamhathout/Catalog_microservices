from rest_framework.test import APITestCase
from model_bakery import baker
from products.models import Product
from rest_framework import status


class TestProductViewSet(APITestCase):

    def setUp(self) -> None:
        self.url = f"/api/product"

        #Create testing 3 products
        self.product_1 = baker.make(Product, name='Pepsi', cost=50, price=4)
        self.product_2 = baker.make(Product, name='Miranda', cost=50, price=4)
        self.product_3 = baker.make(Product, name='Cola', cost=50, price=4)

    def test_list_products(self):
        number_of_current_products = Product.objects.count()
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), number_of_current_products)
        
    def test_update_products(self):
        new_product_name = "Fayrouz"
        body =     {
            "name": new_product_name, 
            "cost": 50,
            "price": 4
        }
        url = f"{self.url}/{str(self.product_3.id)}"
        response = self.client.put(url, data=body) 
        self.product_3.refresh_from_db()

        self.assertEqual(response.status_code, status.HTTP_202_ACCEPTED)
        self.assertEqual(self.product_3.name, new_product_name)
    
    def test_delete_products(self):
        url = f"{self.url}/{str(self.product_3.id)}"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

         
