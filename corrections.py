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
from trie import Trie
from collections import defaultdict
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
				# relating (phrase, index) to associated word in table D
				D[word].append((p, i))
				# loading word into trie T
				C = T.insert(word)
		self.trie = T
		self.context = D

	# returns list of corrections made, as well as the corrected string
	def corrections(self, text):
		context = self.context
		corrected_string = ""
		corrections = []
		T = self.trie
		i = 0
		j = 0
		m = len(text)
		while(i < m):
			word = text[i]
			# the Trie does not currently prejudicially search for a nearest word, but rather takes the first close match
			# but this could be augmented to have a similarity heuristic done at every step to better search for the closest
			# match in the Trie (choosing characters by least dissimilar at each step--reducing state-space to polynomial O(26*n)
			# rather than the exponential space of the full tree O(26^n), but not necessarily returning the best possible result
			# in the whole tree).
			cword,found = T.search(word)
			if cword in context and words_close_enough(word,cword):
				# choosing first in list arbitrarily at present--searching the full list presents more complexity, with
				# potentially more correctness, similarly to searching more through the Trie
				phrase, index = context[cword][0]
				# add the phrase preceeding the correction
				for k in range(index):
					addition = phrase[k]
					corrected_string += addition
					corrections.append(f'+ {addition}')
				# add the correction
				corrected_string += cword
				# move to the next word and check for replacements in the rest of the text
				i+=1
				k = index+1
				n = len(phrase)
				while k < n and i < m:
					cword = phrase[k]
					word = text[i]
					if words_close_enough(word,cword):
						corrected_string += cword
						corrections.append(f'{word} -> {cword}')
						i+=1
					else:
						corrected_string += cword 
						corrections.append(f'+ {cword}')
					k+=1
				# for when the phrase runs past the end of the text
				while k < n:
					addition = phrase[k]
					corrected_string += addition
					corrections.append(f'+ {addition}')
					k+=1
			else:
				i+=1
				corrected_string += word

def words_close_enough(left,right):
	return True

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
