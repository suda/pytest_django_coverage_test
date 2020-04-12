from django.test import TestCase, Client
from django.urls import reverse

class TestViews(TestCase):
    def test_landing(self):
        client = Client()
        response = client.get(reverse("landing"))
        self.assertTemplateUsed(response, "render_something/index.html")