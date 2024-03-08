# Adaugati toate testele pe care le-ati implementat in framework-ul unit test intr-o suita de teste
# Rulati testele direct din suita de teste. Generati raportul de executie si interpretati-l.


import unittest
from HTMLTestRunner.runner import HTMLTestRunner


from Tema_S11.Tema_S11 import LOGARE


class TestSuite(unittest.TestCase):


   def test_suite(self):
       teste_de_rulat = unittest.TestSuite()
       teste_de_rulat.addTests([
           unittest.defaultTestLoader.loadTestsFromTestCase(LOGARE)
       ])


       runner = HTMLTestRunner(log=True, verbosity=2, output='report', title='Test report', report_name='report',
                               open_in_browser=True, description='HTMLTestreport', tested_by='Serban')
       runner.run(teste_de_rulat)
