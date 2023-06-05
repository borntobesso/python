class Evaluator:
    def zip_evaluate(coefs, words):
        if not all(isinstance(coef, (float, int)) for coef in coefs):
            return -1
        elif len(coefs) != len(words):
            return -1
        return sum([len(word) * coef for word, coef in zip(words, coefs)])
    
    def enumerate_evaluate(coefs, words):
        if not all(isinstance(coef, (float, int)) for coef in coefs):
            return -1
        elif len(coefs) != len(words):
            return -1
        return sum(len(word) * coef for i, word in enumerate(words) for i, coef in enumerate(coefs))