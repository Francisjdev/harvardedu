from twttr import shorten

def test_shorten():
    assert shorten("CaSA")=="cs"
    assert shorten("Javier")=="jvr"
    assert shorten("madrE")=="mdr"