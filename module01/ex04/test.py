from eval import Evaluator

words = ["Le", "Lorem", "Ipsum", "est", "simple"]
coefs = [1.0, 2.0, 1.0, 4.0, 0.5]
print(Evaluator.zip_evaluate(coefs, words))

# Error test : words and coefs not same length
words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = [0.0, -1.0, 1.0, -12.0, 0.0, 42.42]
print(Evaluator.enumerate_evaluate(coefs, words))


# Error test : coefs not float or int
words = ["Le", "Lorem", "Ipsum", "n’", "est", "pas", "simple"]
coefs = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(Evaluator.enumerate_evaluate(coefs, words))