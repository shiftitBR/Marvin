# -*- coding: utf-8 -*-

from django.test                    import TestCase
from marvin.ontologia.models 		import Ontologia

class Test(TestCase):
    
    def setUp(self):
        pass
    
    
    def tearDown(self):
        pass
    
    def testListaCatalogs(self):
    	print '##### Inicio testListaCatalogs #####'
        iRetorno= Ontologia().listaCatalogs()
        self.assertEquals(iRetorno, True)
        print '##### Fim testListaCatalogs #####'

    def testeAbreRepositorio(self):
    	print '##### Inicio testeAbreRepositorio #####'
        iRetorno= Ontologia().abreRespositorio()
        self.assertEquals(iRetorno != None, True)
        print '##### Fim testeAbreRepositorio #####'

    def testeExecutaConsulta(self):
    	print '##### Inicio testeExecutaConsulta #####'
        iRetorno= Ontologia().executaConsulta()
        self.assertEquals(iRetorno, True)
        print '##### Fim testeExecutaConsulta #####'
        
        