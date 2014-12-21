# -*- coding: utf-8 -*-

from franz.openrdf.sail.allegrographserver import AllegroGraphServer
from franz.openrdf.repository.repository import Repository
from franz.miniclient import repository
from franz.openrdf.query.query import QueryLanguage
from franz.openrdf.model import URI
from franz.openrdf.vocabulary.rdf import RDF
from franz.openrdf.vocabulary.rdfs import RDFS
from franz.openrdf.vocabulary.owl import OWL
from franz.openrdf.vocabulary.xmlschema import XMLSchema
from franz.openrdf.query.dataset import Dataset
from franz.openrdf.rio.rdfformat import RDFFormat
from franz.openrdf.rio.rdfwriter import  NTriplesWriter
from franz.openrdf.rio.rdfxmlwriter import RDFXMLWriter

import os, urllib, datetime, time, sys

CURRENT_DIRECTORY = os.getcwd() 

AG_HOST = os.environ.get('AGRAPH_HOST', 'localhost')
AG_PORT = int(os.environ.get('AGRAPH_PORT', '10035'))
AG_CATALOG = os.environ.get('AGRAPH_CATALOG', 'python-catalog')
# AG_CATALOG = ''
AG_REPOSITORY = 'FreelaTI'
AG_USER = 'marvin'
AG_PASSWORD = 'teste'
# AG_USER = 'anonymous'
# AG_PASSWORD = ''
# Updated July 23, 2010 AG 4.1 BDC

class Ontologia(object):

	def getConexao(self, accessMode=Repository.RENEW):
		server = AllegroGraphServer(AG_HOST, AG_PORT, AG_USER, AG_PASSWORD)
		catalog = server.openCatalog()
		myRepository = catalog.getRepository(AG_REPOSITORY, accessMode)
		myRepository.initialize()
		conn = myRepository.getConnection()
		return conn

	def listaCatalogs(self):
	    """
	    Can we connect to AG?
	    """
	    print "Starting example example0()."
	    print "Current working directory is '%s'" % (os.getcwd())
	    server = AllegroGraphServer(AG_HOST, AG_PORT, AG_USER, AG_PASSWORD)
	    print "Available catalogs", server.listCatalogs()
	    return True

	def abreRespositorio(self, accessMode=Repository.RENEW):
	    """
	    Tests getting the repository up.  Is called by the other examples to do the startup.
	    """
	    print "Starting example1()."
	    print "Default working directory is '%s'" % (CURRENT_DIRECTORY)
	    server = AllegroGraphServer(AG_HOST, AG_PORT, AG_USER, AG_PASSWORD)
	    print "Available catalogs", server.listCatalogs()
	##    catalog = server.openCatalog(AG_CATALOG)  ## named catalog
	    catalog = server.openCatalog()             ## default rootCatalog
	    print "Available repositories in catalog '%s':  %s" % (catalog.getName(), catalog.listRepositories())    
	    myRepository = catalog.getRepository(AG_REPOSITORY, accessMode)
	    myRepository.initialize()
	    conn = myRepository.getConnection()
	    print "Repository %s is up!  It contains %i statements." % (
	                myRepository.getDatabaseName(), conn.size())
	    indices = conn.listValidIndices()
	    print "All valid triple indices: %s" % (indices)
	    indices = conn.listIndices()
	    print "Current triple indices: %s" % (indices)
	    print "Removing graph indices..."
	    conn.dropIndex("gospi")
	    conn.dropIndex("gposi")
	    conn.dropIndex("gspoi")
	    indices = conn.listIndices()
	    print "Current triple indices: %s" % (indices)
	    print "Adding one graph index back in..."
	    conn.addIndex("gspoi")
	    indices = conn.listIndices()
	    print "Current triple indices: %s" % (indices)
	    return conn

	# def executaConsulta(self):    
	#     conn = self.abreRespositorio()
	#     print "Starting example3()."
	#     print "Default working directory is '%s'" % (CURRENT_DIRECTORY)
	#     print "SPARQL query for all triples in repository."
	#     try:
	#         queryString = "SELECT ?s ?p ?o  WHERE {?s ?p ?o .}"
	#         tupleQuery = conn.prepareTupleQuery(QueryLanguage.SPARQL, queryString)
	#         result = tupleQuery.evaluate();
	#         try:
	#             for bindingSet in result:
	#                 s = bindingSet.getValue("s")
	#                 p = bindingSet.getValue("p")
	#                 o = bindingSet.getValue("o")              
	#                 print "%s %s %s" % (s, p, o)
	#         finally:
	#             result.close();
	#     finally:
	#         conn.close();
	#         myRepository = conn.repository
	#         myRepository.shutDown()

	def executaConsulta(self):
	    conn = self.abreRespositorio()
	    print "Starting example4()."
	    print "Default working directory is '%s'" % (CURRENT_DIRECTORY)
	    alice = conn.createURI("http://www.semanticweb.org/spengler/ontologies/2014/10/untitled-ontology-16#Alberto")
	    print "Searching for Alice using getStatements():"
	    statements = conn.getStatements(alice, None, None, False)
	    print "Statements: %s" % (statements) 
	    # statements.enableDuplicateFilter() ## there are no duplicates, but this exercises the code that checks
	    for s in statements:
	        print s
	    statements.close()
	    conn.close();
	    myRepository = conn.repository
	    myRepository.shutDown()
	    return True