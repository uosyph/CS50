from um import count
import pytest

def main():
    test_um()
    test_um_with_words()
    test_um_with_punc()
    test_um_with_words_and_punc()

def test_um():
    assert count('um') == 1
    assert count('UM') == 1
    assert count('uM') == 1
    assert count('Um') == 1


def test_um_with_words():
    assert count('yumy') == 0
    assert count('album') == 0
    assert count('umm') == 0
    assert count('uumm') == 0


def test_um_with_punc():
    assert count('...um...') == 1
    assert count('!?.,UM,.?!') == 1
    assert count(',.,!!?um?!!,.,') == 1


def test_um_with_words_and_punc():
    assert count('Um, thanks for the album.') == 1
    assert count('Um, thanks, um...') == 2


if __name__ == '__main__':
    main()