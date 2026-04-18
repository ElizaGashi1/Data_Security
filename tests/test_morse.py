from algorithms.MorseCode.morse import encode, decode

def test_encode_basic():
    assert encode("HELLO")==".... . .-.. .-.. ---"
    assert encode("SOS")=="... --- ..."

def test_encode_with_numbers():
    assert encode("ABC 123") == ".- -... -.-. / .---- ..--- ...--"


def test_decode_basic():
    assert decode(".... . .-.. .-.. ---") == "HELLO"
    assert decode("... --- ...") == "SOS"


def test_decode_with_numbers():
    assert decode(".- -... -.-. / .---- ..--- ...--") == "ABC 123"


def test_invalid_encode():
    try:
        encode("HELLO@")
        assert False  
    except ValueError:
        assert True


def test_invalid_decode():
    try:
        decode("... --- ... ---.-")  
        assert False
    except ValueError:
        assert True
