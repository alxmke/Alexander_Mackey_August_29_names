'''
The basic premise of `corrections` will be to take in the user's given context C, and compare
each given piece of text T against it to find which words will or won't be corrected. If a
word W is determined to be a near-enough match to a word X within the context phrase P as to
be corrected, it will correct W to X, and add the words left of X within P to the corrected
string S. It will then search the rest of the text for the remaining words on the right side,
moving forward a word in the phrase each time there is a miss, and moving forward a word in
the text AND the phrase each time there's a hit, correcting the text word to the phrase word in S.

For example, if in C, we have P = "President John F Kennedy", and T = "Jon Kenedy and friends",
`corrections` aims to find Jon associated to P via John, and make C = "President John", and then
it wouldn't find 'F', as the next word is 'Kenedy', and so it would move forward in P to 'Kennedy',
and then find 'Kennedy' close enough to 'Kenedy' (and so replace it), and with no other context
should then place 'and' and 'friends' making C = "President John F Kennedy and friends", with
corrections [(+ President),(Jon -> John),(+ F),(Kenedy -> Kennedy)].
'''
from jaro import jaro
from collections import defaultdict
class Trie:
	def __init__(self, words=None):
		def _trie():
			return defaultdict(_trie)
		self.T = _trie()

	# insert a word into the Trie
	def insert(self, word):
		T = self.T
		for c in word:
			T = T[c]
		T[None]

	# TODO: consider word is empty or none, though it never should be
	# TODO: consider when there are no words in the Trie
	# search for the nearest match in the Trie
	def search(self, word):
		#T = self.T
		#i = 0
		
		# use next(iter(dict)) to get a key out of the dict when there's no match
		#while(
		pass

	# TODO: make a helpful representation of Trie
	def __repr__(self):
		return self.T

	def __str__(self):
		return str(self.T)
		

class Corrector:
	def __init__(self, context): 
		# each phrase in the context, split into  word-by-word lists
		P = [p.split() for p in context]
		# trie to build a nearest match for word, presuming it's not in table D
		T = Trie()
		# relational hashtable associating words to phrases, a list will be searched in case of a conflict
		D = defaultdict(list)

		# process in each phrase in the context
		for p in P:
			# associate each word in the phrase to the rest, and its index in the phrase
			for i in range(len(p)):
				word = p[i]
				# (word, phrase, index) tuples in table D
				D[word].append((p, i))
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

	# returns list of corrections made, as well as the corrected string
	def corrections(self, text):
		context = self.context
		corrected_string = ""
		corrections = []
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
