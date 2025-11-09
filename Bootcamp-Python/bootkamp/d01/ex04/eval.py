class Evaluator():
    """Evaluator class"""

    def zip_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        result = 0
        for a, b in zip(coefs, words):
            result += a * len(b)
        return result

    def enumerate_evaluate(coefs, words):
        if len(coefs) != len(words):
            return -1
        result = 0
        for i, w in enumerate(words):
            result += coefs[i] * len(w)
        return result

if __name__ == '__main__':
    words = ["Le", "Lorem", "Ipsum", "est", "simple"]
    coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
    print(Evaluator.zip_evaluate(coefs, words))
    print(Evaluator.enumerate_evaluate(coefs, words))

    words = ["Le", "Lorem", "Ipsum", "n'", "est", "pas", "simple"]
    coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
    print(Evaluator.enumerate_evaluate(coefs, words))