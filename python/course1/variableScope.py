# the are 4 scopes
# local
# enclosing
# global
# built in
# LEGB

#Built In scope (def)
def outer():
    #enclosed scope
    b = 2
    def inner():
        #local scope
        c = 3
# global scope is generally discouraged in apps

#global 
myGlobal = 10

def fn1():
    enclosedV = 8


    def fn2():
        localV = 5
        print(f'access to global {myGlobal}')
        print(f'Access to local {enclosedV}')
    
    fn2()

fn1()

# the inner function has access to the outside 
