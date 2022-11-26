from working import convert
import pytest

def main():
    test_time()
    test_time2()
    test_wrong_format()


def test_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_time2():
    assert convert('12:00 AM to 12:00 PM') == '00:00 to 12:00'
    assert convert('12 AM to 12 PM') == '00:00 to 12:00'


def test_wrong_format():
    with pytest.raises(ValueError):
        convert('8:70 AM to 12:70 PM')
    with pytest.raises(ValueError):
        convert('9AM to 8PM')
    with pytest.raises(ValueError):
        convert('09:00 to 17:00')
    with pytest.raises(ValueError):
        convert('9 AM - 8 PM')
    with pytest.raises(ValueError):
        convert('09:00 AM - 17:00')


if __name__ == '__main__':
    main()