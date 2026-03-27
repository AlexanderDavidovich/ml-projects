class Roman: 
    def __init__(self, roman):
        self.roman = roman

    def translate(self):
        values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
        }
        total = 0
        for i in range(len(self.roman)):
            if i + 1 < len(self.roman) and values[self.roman[i]] < values[self.roman[i + 1]]:
                total -= values[self.roman[i]]
            else:
                total += values[self.roman[i]]
        return total

n = Roman(input('введите римское число: '))
print(n.translate())

# MCMXXI