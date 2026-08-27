from django.test import TestCase

from recruitmentapp.apps.core.models import Competence


class CompetenceTest(TestCase):
    def setUp(self):
        self.competence = Competence.objects.create(name='mining')
        self.competence.set_current_language('sv')
        self.competence.name = 'gruvarbete'
        self.competence.save()

    def test_translation(self):
        competence = Competence.objects.first()
        self.assertEqual(competence.name, 'mining')
        competence.set_current_language('sv')
        self.assertEqual(competence.name, 'gruvarbete')

    def test_translation_fallback(self):
        competence = Competence.objects.first()
        competence.set_current_language('fi')
        self.assertEqual(competence.name, 'mining')
