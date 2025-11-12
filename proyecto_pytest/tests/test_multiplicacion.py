import pytest 

def multiplicar(a,b):
    """Funcion que multiplica dos numeros"""
    return a*b

def test_multiplicacion():
    assert multiplicar(1,2)==2
    assert multiplicar(-1,1)==-1
    assert multiplicar(0,55)==0

def test_multiplicacion_fail():
    assert multiplicar(5,5)==500
