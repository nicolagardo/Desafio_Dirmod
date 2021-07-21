from teclado import mensaje_valido
from teclado import listar_mensaje
import pytest

def test_mensaje_valido():
     assert mensaje_valido() == 'hola'

def test_listar_mensaje():
    assert listar_mensaje("hola") == ['h', 'o', 'l', 'a']