from string import punctuation as ponct
from string import whitespace as ws

def text_analyzer(text):
    """Counts and prints the number of uppercases,
    lowercases, ponctuation marks and whitespaces."""
    up = lo = pc = sp = 0
    if type(text) is not str or text == '':
        print("What is the text to analyse?")
    else:
        for ltr in text:
            if ltr.isupper():
                up += 1
            elif ltr.islower():
                lo += 1
            elif ltr in ws:
                sp += 1
            elif ltr in ponct:
                pc += 1
        print("The text contains {} characters:".format(len(text)))
        print("-", up, "upper letters")
        print("-", lo, "lower letters")
        print("-", pc, "punctuation marks")
        print("-", sp, "spaces")

if __name__ == "__main__":
    text_analyzer('')
    text_analyzer(4)
    text_analyzer("""Python 2.0, released 2000, introduced features like List comprehensions and a garbage collection system capable of collecting reference cycles.""")
    text_analyzer("Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.")