from jaro import jaro
from collections import defaultdict
class Trie:
	def __init__(self, words=None):
		def _trie():
			return defaultdict(_trie)
		self.T = _trie()

	def insert(self, word):
		T = self.T
		for c in word:
			T = T[c]
		T[None]

	# TODO: consider word is empty or none, though it never should be
	# TODO: consider when there are no words in the Trie
	def search(self, word):
		#T = self.T
		#i = 0
		
		# use next(iter(dict)) to get a key out of the dict when there's no match
		#while(
		pass

class Corrector:
	def __init__(self, context): 
		# each phrase in the context, split into  word-by-word lists
		P = [p.split() for p in context]
		# trie to build a nearest match for word, presuming it's not in table D
		T = Trie()
		# relational hashtable associating words
		D = dict()

		# process in each phrase in the context
		for p in P:
			# associate each word in the phrase to the rest, and its index in the phrase
			for i in range(len(p)):
				word = p[i]
				# (word, phrase, index) tuples in table D
				D[word] = (p, i)
				# loading word into trie T
				C = T.insert(word)
				
				
		'''
		for k in D:
			s, l, r = D[k]
			print(k, s, l, r)
			n = len(s)
			print("  before:")
			for i in range(l):
				print("   " + s[i])
			print("  after:")
			for i in range(r, n):
				print("   " + s[i])
		
		# null string returns []
		if len("".split()):
			print("TEST")
		'''
		self.trie = T
		self.context = D

	def corrections(self, text):
		context = self.context
		for k in context:
			print(k)
		print(self.trie)



# tests
if __name__ == '__main__':
	test_inputs = [
		"tomorrow I have a meeting with Tim Hanks Tom Crus and Eastwood",
		"Michael likes movies with Jon Way and Client East",
		"Jonn invited me Jon Ham and Jon Wane, over for a lunch",
	]

	test_context = ["John Wayne", "Tom Hanks", "William"]
	C = Corrector(test_context)
	for text in test_inputs:
		C.corrections(text)
