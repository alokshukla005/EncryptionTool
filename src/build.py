# Builds ../index.html by inlining OpenPGP.js into index.src.html.
# Run `npm install` in the repo root first.
lib = open('../node_modules/openpgp/dist/openpgp.min.js').read().replace('</script', '<\\/script')
s = open('index.src.html').read().replace('/*OPENPGP*/', lib, 1)
open('../index.html', 'w').write(s)
