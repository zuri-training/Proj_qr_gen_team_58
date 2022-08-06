from django.test import TestCase, Client
from django.urls import reverse

from .models import Contacts

# from django.views import reverse
# Create your tests here.


class MyTests(TestCase):
    def test_contact_page_view(self):
        contact_page_view = reverse("contact_page")
       
        # Test form renders well
        response = self.client.get(contact_page_view)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "contact_page.html")

        # Test form submission
        response = self.client.post(contact_page_view, data = {"name":"UserName", "email":"user@email.com", "message":"Random message"})
       
        # Test Form was submitted properly
        self.assertEqual(response.status_code, 200)

        # Test new model/instance saved in the database
        contact_obj = Contacts.objects.last()
        self.assertEqual(contact_obj.name, "UserName")
        self.assertEqual(contact_obj.email, "user@email.com")
        self.assertEqual(contact_obj.message, "Random message")