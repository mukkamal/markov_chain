import urllib2
from markov_python.cc_markov import MarkovChain

#response=urllib2.urlopen("http://www.gutenberg.org/files/135/135-0.txt")
#html=response.read()
mc=MarkovChain()
strings=mc.generate_text()
sad=0
print strings
for word in strings:
	if word=='sad':
		sad=sad+1
print sad		
