from collections import defaultdict
class Trie:
	# takes a list of strings, words
	def __init__(self, words=[]):
		def _trie():
			return defaultdict(_trie)
		T = _trie()
		# put a stop condition for the empty Trie
		T[None]
		self.T = T

		# i have a couple ideas for a potentially more efficient first loading method
		for word in words:
			self.insert(word)

	# insert a word into the Trie
	def insert(self, word):
		T = self.T
		for c in word:
			T = T[c]
		T[None]

	# TODO: consider word is empty or none, though it never should be
	# TODO: consider when there are no words in the Trie
	# search for a match in the Trie, if not found, return a similar word
	def search(self, word):
		T = self.T
		i = 0
		nearest = ""
		found = True
		# use next(iter(dict)) to get a key out of the dict when there's no match
		#while(
		for c in word:
			if c in T:
				T = T[c]
				nearest += c
			else:
				found = False
				break
		while(None not in T):
			found = False
			c = str(next(iter(T)))
			T = T[c]
			nearest += c
		return (nearest, found)
				
			
	# TODO: make a helpful representation of Trie
	def __repr__(self):
		return self.T

	def __str__(self):
		return str(self.T)
# tests
if __name__ == '__main__':
	T = Trie(['bat', 'cat', 'car'])
	print("Searched for: car", T.search('car'))
	print("Searched for: bar", T.search('bar'))
	S = Trie()
	print("Searched for: car", S.search('car'))
