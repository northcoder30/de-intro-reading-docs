from test_api.checks import (
    run_test, skip_test, format_err_msg, NORMAL_RED, DEFAULT)
import secrets
import string

def generate_secure_token(length=32):
    token_length = length
    if token_length < 32:
        token_length = 32

    token = ''
    # Want to first add the characters we need then add the remaning chars
    token += ''.join(secrets.choice(string.ascii_uppercase) for i in range(5))
    token += secrets.choice(string.ascii_lowercase)
    token += ''.join(secrets.choice(string.digits) for i in range(5))
    token += ''.join(secrets.choice(string.punctuation) for i in range(3))
    
    alphabet = string.ascii_lowercase + string.ascii_uppercase + string.digits # exclude punctuation since we already have 3
    token += ''.join(secrets.choice(alphabet) for i in range(token_length-len(token)))

    # shuffle them so they are randomly distrubuted
    token_list = list(token)
    secrets.SystemRandom().shuffle(token_list)
    
    return ''.join(token_list)

@run_test
def test_returns_default_string_length_32():
    assert len(generate_secure_token()) == 32, \
        format_err_msg(32, len(generate_secure_token()))


@run_test
def test_returns_string_length_provided():
    assert len(generate_secure_token(48)) == 48, \
        format_err_msg(48, len(generate_secure_token(48)))


@run_test
def test_returns_string_with_each_of_char_types():
    from re import search
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation

    token = generate_secure_token()
    has_char_types = []

    for char_type in ascii_uppercase, ascii_lowercase, digits, punctuation:
        has_char_types.append(search(fr'[{char_type}]+', token))

    assert all(has_char_types), (f"{NORMAL_RED}Secure token should contain "
                                 "uppercase characters, lowercase characters, "
                                 f"digits and punctuation characters{DEFAULT}")


@run_test
def test_returns_string_with_min_3_punctuation_chars():
    import string
    token = generate_secure_token()

    punctuation_chars = [char for char in token if char in string.punctuation]

    assert len(punctuation_chars) >= 3, (f"{NORMAL_RED}Secure token should "
                                         "contain at least 3 punctuation"
                                         f"characters{DEFAULT}")


@run_test
def test_returns_string_with_min_5_upper_case_chars():
    token = generate_secure_token()

    upper_case_chars = [char for char in token if char.isupper()]

    assert len(upper_case_chars) >= 5, (f"{NORMAL_RED}Secure token should "
                                        "contain at least 5 uppercase"
                                        f"characters{DEFAULT}")


@run_test
def test_returns_string_with_min_5_numeric_chars():
    token = generate_secure_token()

    numeric_chars = [char for char in token if char.isdigit()]

    assert len(numeric_chars) >= 5, (f"{NORMAL_RED}Secure token should "
                                     f"contain at least 5 digits{DEFAULT}")


@run_test
def test_returns_string_with_min_length_32_when_passed_int_less_than_32():
    assert len(generate_secure_token(10)) == 32, \
        format_err_msg(32, len(generate_secure_token(10)))


@run_test
def test_tokens_are_unique():
    tokens = set()

    for _ in range(100):
        tokens.add(generate_secure_token())
    assert len(tokens) == 100, (f"{NORMAL_RED}Secure tokens should be"
                                f"unique{DEFAULT}")


@run_test
def test_tokens_character_types_are_in_mixed_order():
    from re import findall
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation

    char_types = [ascii_lowercase, ascii_uppercase, digits, punctuation]

    for _ in range(100):
        token = generate_secure_token()
        for char_type in char_types:
            char_groups = findall(fr'[{char_type}]+', token)
            assert len(char_groups) > 1, (f"{NORMAL_RED}Secure token "
                                          "characters should be in a mixed "
                                          f"order{DEFAULT}")


if __name__ == '__main__':
    test_returns_default_string_length_32()
    test_returns_string_length_provided()
    test_returns_string_with_each_of_char_types()
    test_returns_string_with_min_3_punctuation_chars()
    test_returns_string_with_min_5_upper_case_chars()
    test_returns_string_with_min_5_numeric_chars()
    test_returns_string_with_min_length_32_when_passed_int_less_than_32()
    test_tokens_are_unique()
    test_tokens_character_types_are_in_mixed_order()
