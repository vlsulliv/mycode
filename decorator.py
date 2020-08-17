

 
 # this cimple function is a VERY COMPLICATED, UNTOUCHABLE FUNCTION.
def sub(a,b):
    print(a-b)

 # decorator
def smart_sub(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner

sub= smart_sub(sub)

sub(6,10)
