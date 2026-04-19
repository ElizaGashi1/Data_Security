import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from algorithms.Homophonic_sub_cipher import encrypt, decrypt

def test_roundtrip():
    assert decrypt(encrypt("HELLO")) == "HELLO"

def test_roundtrip_with_space():
    assert decrypt(encrypt("HELLO WORLD")) == "HELLO WORLD"

def test_is_random():
    results = set(encrypt("HELLO") for _ in range(10))
    assert len(results) > 1

def test_invalid_character():
    try:
        encrypt("HELLO!")
        assert False
    except ValueError:
        assert True

def test_invalid_empty():
    try:
        encrypt("")
        assert False
    except ValueError:
        assert True