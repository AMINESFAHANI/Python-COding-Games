# For Python:
#
# Create a function whose return value always passes equality checks.
#
# Examples
# equals() == 0 --> True
#
# equals() == [] --> True
#
# equals() == (lambda: 1) --> True

class Equality:

    def __init__(self,x:object,y:object):
        self.x=x
        self.y=y

    def __eq__(self):
        result= lambda x,y : x==y
        return result(self.x,self.y)

def equal():
    pass
    return True


e= Equality(equal(),0)
e.__eq__()

