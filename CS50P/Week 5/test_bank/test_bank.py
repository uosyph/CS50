from bank import value

def main():
    test_value_0()
    test_value_20()
    test_value_100()


def test_value_0():
    assert value('hello cs50') == 0
    assert value('Hello') == 0
    assert value('HeLlO CS50') == 0


def test_value_20():
    assert value('hey') == 20
    assert value('HI') == 20


def test_value_100():
    assert value('what\'s up') == 100
    assert value('good mornin\'') == 100
    assert value('12498431') == 100
    assert value('!%$&<>.,":') == 100


if __name__ == '__main__':
    main()