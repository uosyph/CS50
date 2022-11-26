from seasons import get_dob

def main():
    test_dob()


def test_dob():
    assert get_dob('2002-03-20') == ('2002', '03', '20')
    assert get_dob('2002-3-20') == None
    assert get_dob('Mar 20, 2002') == None
    assert get_dob('20302') == None


if __name__ == '__main__':
    main()