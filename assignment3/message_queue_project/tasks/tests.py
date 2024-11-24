from django.test import TestCase
from .models import DataUpload
from django.urls import reverse

class DataUploadTestCase(TestCase):

    def setUp(self):
       
        self.upload = DataUpload.objects.create(file='test1.csv', status='Processing')

    def test_upload_status(self):
      
        response = self.client.get(reverse('check_upload_status', args=[self.upload.id]))
        self.assertEqual(response.status_code, 200)
        self.assertIn('status', response.json())
        self.assertEqual(response.json()['status'], 'Processing')
