import requests
from rdflib import Graph, Literal, BNode, Namespace, URIRef
from rdflib.namespace import SKOS, RDF, DC, DCTERMS, RDFS

OA = Namespace("http://www.w3.org/ns/oa#")
creator = DCTERMS.creator
created = DCTERMS.created
target = OA.hasTarget
# get the ttl file from the solid pod
ttlText = requests.get('https://restaurierungsvokabular.solidweb.org/annotations/annotations.ttl').text
# load ttlTest into a graph
g = Graph()
g.parse(data=ttlText, format='ttl')
# load all annotations from the graph into list
annotations = []
# find all subjects in the graph which are of type oa:Annotation
for s, p, o in g.triples((None, RDF.type, OA.Annotation)):
    annotations.append(s)
for annotation in annotations:
    # get the target of the annotation
    annotationTarget = list(g.objects(annotation, target))
    # get the creator of the annotation
    annotationCreator = list(g.objects(annotation, creator))
    # get the created date of the annotation
    annotationCreated = list(g.objects(annotation, created))
    print(f"Annotation: {annotation}")
    print(f"Target: {annotationTarget}")
    print(f"Creator: {annotationCreator}")
    print(f"Created: {annotationCreated}")
    if len(annotationTarget) > 1 or len(annotationCreator) > 1 or len(annotationCreated) > 1:
        print("Multiple entries found in annotation")
    print("\n")