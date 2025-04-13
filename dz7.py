class WordLengthIterator:
    def __init__(self, word_list):
        self.word_list = word_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.word_list):
            word = self.word_list[self.index]
            self.index += 1
            return len(word)
        else:
            raise StopIteration

words = ["яблоко", "банан", "апельсин", "виноград"]
word_length_iterator = WordLengthIterator(words)

for length in word_length_iterator:
    print(length)