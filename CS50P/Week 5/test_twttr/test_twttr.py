from twttr import shorten

def main():
    test_shorten_str()
    test_shorten_int()
    test_shorten_punc()


def test_shorten_str():
    assert shorten('twitter') == 'twttr'
    assert shorten('yOuSeF') == 'ySF'
    assert shorten('CS50P') == 'CS50P'


def test_shorten_int():
    assert shorten('123') == '123'
    assert shorten('404') == '404'


def test_shorten_punc():
    assert shorten('!@^*@$#') == '!@^*@$#'
    assert shorten('._.}>.??_<,.') == '._.}>.??_<,.'


if __name__ == '__main__':
    main()