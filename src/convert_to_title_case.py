import pytest


def convert_to_title_case(sentence):
    pass


def test_convert_single_word_to_title_case():
    assert convert_to_title_case("hi") == "Hi"


@pytest.mark.skip()
def test_convert_multi_word_to_title_case():
    assert convert_to_title_case("hello world") == "Hello World"
    assert convert_to_title_case("Goodbye world") == "Goodbye World"
    assert (
        convert_to_title_case("Well ain't this awkward")
        == "Well Ain't This Awkward"
    )


@pytest.mark.skip()
def test_convert_complex_sentence_to_title_case():
    assert (
        convert_to_title_case("not just apostrophes, could be something-else")
        == "Not Just Apostrophes, Could Be Something-else"
    )
