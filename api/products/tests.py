from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.test import APIClient
from users.models import User
from .models import Category, Product, VariationName, VariationOption


class CategoryViewSetTestCase(TestCase):
    # def setUp(self):
    #     # Create a test object (Category) in the test database
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            email="admin@gmail.com", password="1234"
        )
        self.category = Category.objects.create(name="Test Category", active=True)

        # Generate a JWT access token for the test user
        access_token = AccessToken.for_user(self.user)
        # Set the HTTP_AUTHORIZATION header with the token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    def test_list_categories(self):
        # Perform a GET request to the list endpoint of the CategoryViewSet
        url = reverse("category-list")
        response = self.client.get(url)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Assert that the length of the response data (list of categories) is 1
        self.assertEqual(len(response.data.get("data")), 1)

    def test_retrieve_category(self):
        # Perform a GET request to retrieve a specific category by its primary key
        url = reverse("category-detail", kwargs={"pk": self.category.id})
        response = self.client.get(url)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the name of the retrieved category matches the expected value
        self.assertEqual(response.data.get("data")[0].get("name"), "Test Category")

    def test_create_category(self):
        # Perform a POST request to create a new category
        url = reverse("category-list")
        data = {"name": "New Category", "active": True}
        response = self.client.post(url, data, format="json")
        # Assert that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Assert that the count of Category objects in the test database is 2
        self.assertEqual(Category.objects.count(), 2)

    def test_create_category_conflict(self):
        # Perform a POST request to create a new category
        url = reverse("category-list")
        data = {"name": "Test Category", "active": True}
        response = self.client.post(url, data, format="json")
        # Assert that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("data"), [])

    def test_update_category(self):
        # Perform a PUT request to update an existing category
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        data = {"name": "Updated Category", "active": False}
        response = self.client.put(url, data, format="json")

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the category object from the database to reflect the updated values
        self.category.refresh_from_db()

        # Assert that the name of the updated category matches the expected value
        self.assertEqual(self.category.name, "Updated Category")

        # Assert that the active attribute of the updated category is False
        self.assertFalse(self.category.active)

    def test_delete_category(self):
        # Perform a DELETE request to delete an existing category
        url = reverse("category-detail", kwargs={"pk": self.category.pk})
        response = self.client.delete(url)

        # Assert that the response status code is 204 No Content (successful deletion)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert that the category object has been deleted from the test database
        self.assertFalse(Category.objects.filter(pk=self.category.pk).exists())


class ProductViewSetTestCase(TestCase):
    # def setUp(self):
    #     # Create a test object (Category) in the test database
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            email="admin@gmail.com", password="1234"
        )
        self.category = Category.objects.create(name="Test Category", active=True)
        self.product = Product.objects.create(
            name="Test Product", active=True, category=self.category
        )

        # Generate a JWT access token for the test user
        access_token = AccessToken.for_user(self.user)
        # Set the HTTP_AUTHORIZATION header with the token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    def test_list_categories(self):
        url = reverse("product-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data.get("data")), 1)

    def test_retrieve_product(self):
        url = reverse("product-detail", kwargs={"pk": self.product.id})
        response = self.client.get(url)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the name of the retrieved product matches the expected value
        self.assertEqual(response.data.get("data")[0].get("name"), "Test Product")

    def test_create_product(self):
        # Perform a POST request to create a new product
        url = reverse("product-list")
        data = {"name": "New Product", "active": True, "product": self.product.pk}
        response = self.client.post(url, data, format="json")
        # Assert that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that the count of product objects in the test database is 2
        self.assertEqual(Product.objects.count(), 2)

    def test_create_product_conflict(self):
        # Perform a POST request to create a new product
        url = reverse("product-list")
        data = {"name": "Test Product", "active": True, "category": self.category.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("data"), [])

    def test_update_product(self):
        # Perform a PUT request to update an existing product
        url = reverse("product-detail", kwargs={"pk": self.product.pk})
        data = {
            "name": "Updated Product",
            "active": False,
        }  # Correct field names and values
        response = self.client.put(url, data, format="json")

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the product object from the database to reflect the updated values
        self.product.refresh_from_db()

        # Assert that the name of the updated product matches the expected value
        self.assertEqual(self.product.name, "Updated Product")

        # Assert that the active attribute of the updated product is False
        self.assertFalse(self.product.active)

    def test_delete_product(self):
        # Perform a DELETE request to delete an existing product
        url = reverse("product-detail", kwargs={"pk": self.product.pk})
        response = self.client.delete(url)

        # Assert that the response status code is 204 No Content (successful deletion)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert that the product object has been deleted from the test database
        self.assertFalse(Product.objects.filter(pk=self.product.pk).exists())


class VariationNameViewSetTestCase(TestCase):
    # def setUp(self):
    #     # Create a test object (Category) in the test database
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            email="admin@gmail.com", password="1234"
        )
        self.category = Category.objects.create(name="Test Category", active=True)
        self.variation_name = VariationName.objects.create(
            name="Test VariationName", category=self.category
        )

        # Generate a JWT access token for the test user
        access_token = AccessToken.for_user(self.user)
        # Set the HTTP_AUTHORIZATION header with the token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    def test_list_categories(self):
        url = reverse("variation_name-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data.get("data")), 1)

    def test_retrieve_variationName(self):
        url = reverse("variation_name-detail", kwargs={"pk": self.variation_name.id})
        response = self.client.get(url)
        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the name of the retrieved VariationName matches the expected value
        self.assertEqual(response.data.get("data")[0].get("name"), "Test VariationName")

    def test_create_variation_name(self):
        # Perform a POST request to create a new VariationName
        url = reverse("variation_name-list")
        data = {"name": "New VariationName", "category": self.category.id}
        response = self.client.post(url, data, format="json")
        # Assert that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that the count of VariationName objects in the test database is 2
        self.assertEqual(VariationName.objects.count(), 2)

    def test_create_variationName_conflict(self):
        # Perform a POST request to create a new VariationName
        url = reverse("variation_name-list")
        data = {"name": "Test VariationName", "category": self.category.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("data"), [])

    def test_update_variation_name(self):
        # Perform a PUT request to update an existing VariationName
        url = reverse("variation_name-detail", kwargs={"pk": self.variation_name.id})
        data = {
            "name": "Updated VariationName",
            "category": self.category.id,
        }  # Correct field names and values
        response = self.client.put(url, data, format="json")
        # Assert that the response status code is  200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the VariationName object from the database to reflect the updated values
        self.variation_name.refresh_from_db()

        # Assert that the name of the updated VariationName matches the expected value
        self.assertEqual(self.variation_name.name, "Updated VariationName")

    def test_delete_variation_name(self):
        # Perform a DELETE request to delete an existing VariationName
        url = reverse("variation_name-detail", kwargs={"pk": self.variation_name.id})
        response = self.client.delete(url)

        # Assert that the response status code is 204 No Content (successful deletion)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert that the VariationName object has been deleted from the test database
        self.assertFalse(
            VariationName.objects.filter(pk=self.variation_name.pk).exists()
        )


class VariationOptionViewSetTestCase(TestCase):
    # def setUp(self):
    #     # Create a test object (Category) in the test database
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_superuser(
            email="admin@gmail.com", password="1234"
        )
        self.category = Category.objects.create(name="Test Category", active=True)
        self.variation_name = VariationName.objects.create(
            name="Test VariationName", category=self.category
        )
        self.variation_option = VariationOption.objects.create(
            value="Test Variation Option", variation_name=self.variation_name
        )

        # Generate a JWT access token for the test user
        access_token = AccessToken.for_user(self.user)
        # Set the HTTP_AUTHORIZATION header with the token
        self.client.credentials(HTTP_AUTHORIZATION=f"Bearer {access_token}")

    def test_list_variation_option(self):
        url = reverse("variation_option-list")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(len(response.data.get("data")), 1)

    def test_retrieve_variation_option(self):
        url = reverse("variation_option-detail", kwargs={"pk": self.variation_option.id})
        response = self.client.get(url)

        # Assert that the response status code is 200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assert that the name of the retrieved variation_option matches the expected value
        self.assertEqual(response.data.get("data")[0].get("value"), "Test Variation Option")

    def test_create_variation_name(self):
        # Perform a POST request to create a new variation_option
        url = reverse("variation_option-list")
        data = {"value": "New Variation Option", "variation_name": self.variation_name.id}
        response = self.client.post(url, data, format="json")
        # Assert that the response status code is 201 Created
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Assert that the count of variation_option objects in the test database is 2
        self.assertEqual(VariationOption.objects.count(), 2)

    def test_create_variation_option_conflict(self):
        # Perform a POST request to create a new variation_option
        url = reverse("variation_option-list")
        data = {"value": "Test Variation Option", "variation_name": self.variation_name.id}
        response = self.client.post(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(response.data.get("data"), [])

    def test_update_variation_option(self):
        # Perform a PUT request to update an existing variation_option
        url = reverse("variation_option-detail", kwargs={"pk": self.variation_option.id})
        data = {
            "value": "Updated Variation Option",    
            "variation_name": self.variation_name.id,
        }  # Correct field names and values
        response = self.client.put(url, data, format="json")
        # Assert that the response status code is  200 OK
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Refresh the variation_option object from the database to reflect the updated values
        self.variation_option.refresh_from_db()

        # Assert that the name of the updated variation_option matches the expected value
        self.assertEqual(self.variation_option.value, "Updated Variation Option")

    def test_delete_variation_name(self):
        # Perform a DELETE request to delete an existing variation_option
        url = reverse("variation_option-detail", kwargs={"pk": self.variation_option.id})
        response = self.client.delete(url)

        # Assert that the response status code is 204 No Content (successful deletion)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        # Assert that the variation_option object has been deleted from the test database
        self.assertFalse(
            VariationOption.objects.filter(pk=self.variation_name.pk).exists()
        )
