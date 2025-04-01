# Corpuscle

```prompt
Please create an OWL ontology to capture the following:
A corpuscle is a resource in an RDF graph used to refer to an information entity (an object in a corpus). This will typically be sourced from something like an academic paper. The original will be referenced by a doi identifier, a URL (such as an arxiv page). This will use standard document reference terms from Dublin Core etc. This will have additional simple metadata such as rdfs:label.
A corpuscle will have a set of properties that either refer directly to literals where they are short, as in dc:description or rdfs:label or a very concise summary. The corpuscle will also refer to other representations of the entity, such as an embedding vector (this will likely contain a reference to the model used to create the embedding and the numbers together with their encoding - possibly a csv literal string). Summaries of various levels of details will be referenced, as will various products of analyses such as keyword lists, the identifiers of papers mentioned in references and so on.  
Render the ontology as an artifact in RDF Turtle. Additional provide an instance example based on the attached paper (feel free to mock the details rather than trying to do any comprehensive extraction, it's getting an idea of the model that counts here).
```
