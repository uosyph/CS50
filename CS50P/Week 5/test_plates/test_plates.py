from plates import is_valid

def main():
    test_isvalid_min_max_chars()
    test_isvalid_start_with_two_letters()
    test_isvalid_middle_numbers()
    test_isvalid_middle_zero()
    test_isvalid_punc()


def test_isvalid_min_max_chars():
    assert is_valid('AA') == True
    assert is_valid('ABCDEF') == True
    assert is_valid('A') == False
    assert is_valid('ABCDEFGH') == False


def test_isvalid_start_with_two_letters():
    assert is_valid('AA') == True
    assert is_valid('A1') == False
    assert is_valid('1A') == False
    assert is_valid('11') == False


def test_isvalid_middle_numbers():
    assert is_valid('AAA111') == True
    assert is_valid('AAA11A') == False


def test_isvalid_middle_zero():
    assert is_valid('CS50') == True
    assert is_valid('CS05') == False


def test_isvalid_punc():
    assert is_valid('PI3.14') == False
    assert is_valid('PI3!14') == False
    assert is_valid('PI 14') == False


if __name__ == '__main__':
    main()