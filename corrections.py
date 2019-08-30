'''
The basic premise of `corrections` will be to take in the user's given context C, and compare
each given piece of text T against it to find which words will or won't be corrected. If a
word W is determined to be a near-enough match to a word X within the context phrase P as to
be corrected, then it will be.

Further metrics will be explored to determine and discover similaritiy in the search Trie.
'''
from jaro import jaro
from trie import Trie
from collections import defaultdict
class Corrector:
	def __init__(self, context): 
		# each phrase in the context, split into  word-by-word lists
		P = [p.split() for p in context]
		# trie to build a nearest match for word, presuming it's not in table D
		T = Trie()
		# relational hashtable associating words to phrases
		D = defaultdict(list)

		# process in each phrase in the context
		for p in P:
			# associate each word in the phrase to the rest, and its index in the phrase
			for i in range(len(p)):
				word = p[i]
				# relating (phrase, index) to associated word in table D
				D[word].append((p, i))
				# loading word into trie T
				C = T.insert(word)
		self.trie = T
		self.context = D

	# returns the corrected text, along with a list of corrections
	def corrections(self, text):
		text = text.split()
		context = self.context
		corrections = []
		T = self.trie
		m = len(text)
		for i in range(m):
			word = text[i]
			# TODO:
			# the Trie does not currently prejudicially search for a nearest word, but rather takes the first close match
			# but this could be augmented to have a similarity heuristic done at every step to better search for the closest
			# match in the Trie (choosing characters by least dissimilar at each step--reducing state-space to polynomial O(26*n)
			# rather than the exponential space of the full tree O(26^n), but not necessarily returning the best possible result
			# in the whole tree).
			# 
			# i've considered penalizing context word candidates which are of different magnitude than the correction candidate
			# in some manner

			cword,_ = T.search(word) 
			if cword in context and words_close_enough(word,cword) and word != cword:
				text[i] = cword
				text_left = cword
				corrections.append(f'({word} -> {cword}) @{i}')
		return " ".join(text), corrections

# threshold of 0.75 chosen fairly arbitrarily as to fit the test data, not sure on optimal number currently
def words_close_enough(left,right,threshold=0.75):
	s = jaro(left,right)
	return s > threshold

# tests
if __name__ == '__main__':
	test_context = ["John Wayne", "Tom Hanks", "Tom Cruise", "John Hamm",  "William", "Clint Eastwood", "Thomas Watson", "yesterday"]
	test_inputs = [
		# passing input:
		# worth noting tom and tomorrow more jaro-similarity than tim and tom, wonder what better metrics could get a better match?
		"tomorrow I have a meeting with Tim Hanks Tom Crus and Eastwood",
		"Michael likes movies with Jon Way and Client East",
		"Jonn invited me Jon Ham and Jon Wane over for a lunch",

		# failing input:
		"i got a call yetserday from Tomas Watsin"
	]

	C = Corrector(test_context)
	for text in test_inputs:
		corrected_string, corrections = C.corrections(text)
		print(f'\'{text}\'\n\tbecame\n\'{corrected_string}\'\n\twith\n corrections: {corrections}\n')

	
