def document_it(func):
    def new_function(*args, **kwargs):
        print('Running function:', func.__name__)
        print('Positional arguments:', args)
        print('Keyword arguments:', kwargs)
        result = func(*args, **kwargs)
        print('Result:', result)
        return result
    return new_function



def add_ints(a, b):
   return a + b

cooler_add_ints = document_it(add_ints)
cooler_add_ints(3, 5)


words = ['eeenie', 'meenie', 'miny', 'MO']
for word in words:
 if word.isupper():
   raise UppercaseException(word)