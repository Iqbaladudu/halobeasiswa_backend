from django.test import TestCase
from .models import Countries
import datetime

# Model test


class CountriesTestCase(TestCase):
    def setUp(self):
        Countries.objects.create(name="Turkiye", date_open='2023-01-01', date_closes='2023-01-01', status='OPEN', description='hdfgjkghsjdkfhdjkgh',
                                 registration_link='https://www.google.com', booklet_link='https://www.google.com', highlight='FALSE')

    def test_countries_models(self):
        turkiye = Countries.objects.get(name='Turkiye')
        self.assertEqual(turkiye.name, 'Turkiye')
        self.assertEqual(turkiye.date_open, datetime.date(2023, 1, 1))
        self.assertEqual(turkiye.date_closes, datetime.date(2023, 1, 1))
