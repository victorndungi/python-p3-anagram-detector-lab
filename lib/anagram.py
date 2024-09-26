# your code goes here!
class Anagram:
    def __init__(self, word):
        self.sorted_word = ''.join(sorted(word))
    
    def match(self, possible_anagarams):
        return [anagram for anagram in possible_anagarams if ''.join(sorted(anagram)) == self.sorted_word]