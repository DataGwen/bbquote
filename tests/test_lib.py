from bbquote.lib import get_quote

def test_output_is_tuple():
    assert type(get_quote()) == tuple
    assert len(get_quote()) == 2

def test_output_not_null():
    quote, author = get_quote()
    assert quote != ""
    assert author != ""