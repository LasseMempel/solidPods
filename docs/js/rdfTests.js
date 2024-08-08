//import * as $rdf from "rdflib.min.js";
const url = 'https://restaurierungsvokabular.solidweb.org/annotations/annotations.ttl';

async function writeToPod(text, url) {
    let response;
    try {
        response = await fetch(url, {
            method: 'PUT',
            headers: {
                'Content-Type': 'text/turtle'
            },
            body: text
        });
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        let result = await response.text();
        console.log(result);
    } catch (error) {
        console.error(error.message);
    }
}

async function readFromPod(url) {
    let result;
    try {
        result = await fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'text/turtle'
            }
        }
        );
        if (!result.ok) {
            throw new Error(`Response status: ${result.status}`);
        }
        return result.text();
    } catch (error) {
        console.error(error);
    }
}

function initializePod() {
    //
}



// declare namespaces
var AO = $rdf.Namespace("http://www.w3.org/ns/oa#")
var FOAF = $rdf.Namespace("http://xmlns.com/foaf/0.1/")
var DC = $rdf.Namespace("http://purl.org/dc/terms/")
var SK = $rdf.Namespace("http://www.w3.org/2004/02/skos/core#")
var RV = $rdf.Namespace("https://restaurierungsvokabular.solidweb.org/annotations#")
var RDF = $rdf.Namespace("http://www.w3.org/1999/02/22-rdf-syntax-ns#")

// declare entities
var concept = SK('Concept')
var thesaurus = SK('ConceptScheme')
var annotation = AO('Annotation')
var comment = AO("bodyValue")
var target = AO("hasTarget")
var motivation = AO("motivatedBy")
var creator = DC("creator")
var created = DC("created")

// create store
store = $rdf.graph();

//create annotation
anno = $rdf.sym("https://restaurierungsvokabular.solidweb.org/annotations/anno1")

// add annotation to store
store.add(anno, RDF('type'), AO('Annotation'))