from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from photos.models import  Category, Photo

# Create your tests here.


# category models test
class CategoryTestCase(TestCase):

    def setUp(self):
        
        Category.objects.create(name="Test Category")

    def test_category_name(self):
       
        category = Category.objects.get(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_category_str(self):
        
        category = Category.objects.get(name="Test Category")
        self.assertEqual(str(category), "Test Category")


# image model tests
class ImageTestCase(TestCase):

    def setUp(self):
        
        Photo.objects.create(
            name="Test Image",
            description="Test Description",
            category=Category.objects.create(name="Test Category"),
            image="http://test.com/test.jpg",
            created_at=None
        )

    def test_image_name(self):
       
        photo = Photo.objects.get(name="Test Image")
        self.assertEqual(photo.name, "Test Image")

    def test_image_description(self):
        
        photo = Photo.objects.get(name="Test Image")
        self.assertEqual(photo.description, "Test Description")

    
    def test_image_category(self):
       
        photo = Photo.objects.get(name="Test Image")
        self.assertEqual(photo.category.name, "Test Category")

    def test_image_image(self):
       
        photo = Photo.objects.get(name="Test Image")
        self.assertEqual(photo.image, "http://test.com/test.jpg")


    def test_image_str(self):
        
        photo = Photo.objects.get(name="Test Image")
        self