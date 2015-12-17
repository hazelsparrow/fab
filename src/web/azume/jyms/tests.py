from django.test import TestCase
from .models import Jym

class JymsTests(TestCase):

    def test_add_jym_adds_one_jym(self):
        response = self.client.post("/jyms/add", {"lat": 25, "lng": 10})
        jyms = Jym.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(jyms.count(), 1)
        self.assertEqual(jyms[0].lat, 25)
        self.assertEqual(jyms[0].lng, 10)

