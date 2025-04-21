# About namespaces/docs/postcraft

Material that was previously at `https://hyperdata.it/xmlns/` migrated to `https://hyperdata.it/ns/` (redirecting for cool URIs)

Exceptions : mcp, a2a

On server, first check `hyperdata/sites/danny.ayers.name`, if not exist, use `sites/hyperdata-static`

```sh
cd ~/hyperdata/transmissions # my local path
./del2.sh
./trans md-to-sparqlstore ~/hyperdata/namespaces/docs/postcraft
./trans postcraft-statics ~/hyperdata/namespaces/docs/postcraft #
./trans sparqlstore-to-html ~/hyperdata/namespaces/docs/postcraft
./trans sparqlstore-to-site-indexes ~/hyperdata/namespaces/docs/postcraft
```

## Default Postcraft Structure

- about.md
- app.ttl
- content
  - media
  - raw
  - static
- knowledge
  - prompts
  - references
- layout
  - base
  - logos
- public
- system
  - sparql-templates

---

```sh
cd ~/sites/strandz.it/postcraft
tree -L 2 --filesfirst
```

#:todo purl.org/ibis redirect to hyperdata.it/ns/