"""
Variables :-
    Camel Case = camelCase
    Pascal Case = PasalCase
    Snake Case = snake_case
"""
x = 100
print(id(x))
y = x
print(id(y))
y = 500
print(id(y))

"""
    Global variable & Local variable :-
"""
x = 100


def global_variable():
    global x
    x = 20
    print(x)


global_variable()
print(x)

"""
    nonlocal :-
    The nonlocal keyword in Python is used inside a nested or child function to modify a variable in the nearest or 
    parent enclosing function.
        1. To modify a variable in the nearest enclosing scope that is not global.
        2. Place nonlocal before the variable name inside the nested function.
        3. Modifies the variable in the enclosing function.
"""


def outer_function():
    x = 20

    def inner_function():
        nonlocal x
        x = 10
        print(x)

    inner_function()
    print(x)


outer_function()
