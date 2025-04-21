cd ~/hyperdata/transmissions # my local path
./del2.sh
./trans md-to-sparqlstore ~/hyperdata/namespaces/docs/postcraft
./trans postcraft-statics ~/hyperdata/namespaces/docs/postcraft #
./trans sparqlstore-to-html ~/hyperdata/namespaces/docs/postcraft
./trans sparqlstore-to-site-indexes ~/hyperdata/namespaces/docs/postcraft
