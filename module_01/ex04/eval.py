from multiprocessing.sharedctypes import Value


class Evaluator:
    @staticmethod
    def zip_evaluate(coefs,words):
        try:
            assert isinstance(coefs,list)
            assert isinstance(words,list)
            assert len(coefs)==len(words)
        except Exception:
            return -1
        else:
            try:
                return sum([x*len(y) for (x,y)in zip(coefs,words)])
            except Exception:
                return -1

    @staticmethod
    def enumerate_evaluate(coefs,words):
        try:
            assert isinstance(coefs,list)
            assert isinstance(words,list)
            assert len(coefs)==len(words)
        except Exception:
            return -1
        else:
            try:
                return sum([coefs[x]*len(y) for (x,y)in enumerate(words)])
            except Exception:
                return -1

test=Evaluator
words=["Le","Lorem","Ipsum","est","simple"]
coefs=[1.0,2.0,1.0,4.0,0.5]
Evaluator.enumerate_evaluate(coefs,words)
Evaluator.zip_evaluate(coefs,words)