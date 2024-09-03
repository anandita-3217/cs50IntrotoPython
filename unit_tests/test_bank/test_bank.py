
from bank import value

def test_value():
    
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO there") == 0
    assert value("hi") == 20
    assert value("Hey") == 20
    assert value("howdy") == 20
    assert value("Good morning") == 100
    assert value("What's up") == 100
    assert value("Greetings") == 100

