import pytest
from fuel import convert, gauge

def main():
    test_correct_input()
    test_str_input()
    test_zero_input()


def test_correct_input():
    assert convert('1/4') == 25 and gauge(25) == '25%'
    assert convert('1/100') == 1 and gauge(1) == 'E'
    assert convert('99/100') == 99 and gauge(99) == 'F'


def test_str_input():
    with pytest.raises(ValueError):
        convert('test/str')


def test_zero_input():
    with pytest.raises(ZeroDivisionError):
        convert('1/0')


if __name__ == '__main__':
    main()