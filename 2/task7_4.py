class ReverseWords:
    def __init__(self, text):
        self.text = text

    def reverse(self):
        words = self.text.split()
        return ' '.join(reversed(words))

print(ReverseWords(input()).reverse())