import urllib
u="""http://xmlarmyknife.org/api/rdf/sparql/query?default-graph-uri=http%3A%2F%2Fxmlns.com%2Ffoaf%2F0.1%2Findex.rdf&query=PREFIX+rdf%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F1999%2F02%2F22-rdf-syntax-ns%23%3E%0D%0APREFIX+rdfs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2000%2F01%2Frdf-schema%23%3E%0D%0APREFIX+vs%3A+%3Chttp%3A%2F%2Fwww.w3.org%2F2003%2F06%2Fsw-vocab-status%2Fns%23%3E%0D%0ASELECT+DISTINCT+%3Fstatus+%3Fx+%3Flabel%0D%0AWHERE+%7B%0D%0A%7B%0D%0A++%3Fx+a+rdf%3AProperty+.%0D%0A++%3Fx+rdfs%3Alabel+%3Flabel+.%0D%0A++%3Fx+vs%3Aterm_status+%3Fstatus+.%0D%0A%7D+UNION+%7B%0D%0A++%3Fx+a+rdfs%3AClass+.%0D%0A++%3Fx+rdfs%3Alabel+%3Flabel+.%0D%0A++%3Fx+vs%3Aterm_status+%3Fstatus+.%0D%0A%7D%0D%0A%7D%0D%0AORDER+BY+%3Fstatus&format=html"""
print urllib.unquote(u)
