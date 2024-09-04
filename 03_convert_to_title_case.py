from test_api.checks import run_test, skip_test, format_err_msg
import string

def convert_to_title_case(sentence):
    cap = string.capwords(sentence, sep = None)
    return cap
    # return re.sub(r"[A-Za-z]+('[A-Za-z] +)?", lambda word: word.group(0).capitalize(),sentence)


@run_test
def test_convert_single_word_to_title_case():
    assert convert_to_title_case("hi") == "Hi", \
        format_err_msg("Hi", convert_to_title_case("hi"))


@run_test
def test_convert_multi_word_to_title_case():
    assert convert_to_title_case("hello world") == "Hello World", \
        format_err_msg("Hello World", convert_to_title_case("hello world"))

    assert convert_to_title_case("Goodbye world") == "Goodbye World", \
        format_err_msg("Goodbye World", convert_to_title_case("Goodbye world"))

    assert convert_to_title_case("Well ain't this awkward") == \
        "Well Ain't This Awkward", \
        format_err_msg("Well Ain't This Awkward",
                       convert_to_title_case("Well ain't this awkward"))


@run_test
def test_convert_complex_sentence_to_title_case():
    assert convert_to_title_case(
        "not just apostrophes, could be something-else") \
        == "Not Just Apostrophes, Could Be Something-else", \
        format_err_msg(
            "Not Just Apostrophes, Could Be Something-else",
            convert_to_title_case(
                "not just apostrophes, could be something-else"))


if __name__ == '__main__':
    test_convert_single_word_to_title_case()
    test_convert_multi_word_to_title_case()
    test_convert_complex_sentence_to_title_case()
