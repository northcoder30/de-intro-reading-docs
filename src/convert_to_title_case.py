def convert_to_title_case(sentence):
    pass


def test_convert_to_title_case():
    assert convert_to_title_case("hi") == "Hi"
    assert convert_to_title_case("hello world") == "Hello World"
    assert convert_to_title_case("Goodbye world") == "Goodbye World"
    assert (
        convert_to_title_case("Well ain't this awkward")
        == "Well Ain't This Awkward"
    )
    assert (
        convert_to_title_case("not just apostrophes, could be something-else")
        == "Not Just Apostrophes, Could Be Something-else"
    )
