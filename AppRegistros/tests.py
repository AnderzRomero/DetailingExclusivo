from django.test import TestCase

from AppRegistros.forms import ClientesFormulario


class ClientesFormularioTestCase(TestCase):
    def setUp(self):
        ClientesFormulario.objects.create(nombre='Anderson', apellidos='Romero')
        ClientesFormulario.objects.create(nombre='Manfred', apellidos='Rico')

    def test_animals_can_speak(self):
        p1 = ClientesFormulario.objects.get(apellidos='Romero')
        p2 = ClientesFormulario.objects.get(apellidos='Rico')
        self.assertEqual(p1.nombre, 'Anderson')
        self.assertEqual(p2.nombre, 'Manfred')
