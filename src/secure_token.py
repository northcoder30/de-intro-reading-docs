import pytest
import secrets


def generate_secure_token(length=32):
    if length < 32:
        length = 32

    chars = []
    token = ''

    num_punctuation_chars = secrets.choice(range(3, length-12))
    length -= num_punctuation_chars

    chars.extend(secrets.choice(punctuation)
                 for _ in range(num_punctuation_chars))

    num_cap_alpha_chars = secrets.choice(range(5, length-7))
    length -= num_cap_alpha_chars

    chars.extend(secrets.choice(ascii_uppercase)
                 for _ in range(num_cap_alpha_chars))

    num_digits = secrets.choice(range(5, length-2))
    length -= num_digits

    chars.extend(secrets.choice(digits) for _ in range(num_digits))

    chars.extend(secrets.choice(ascii_lowercase) for _ in range(length))

    for _ in range(len(chars)):
        char = secrets.choice(chars)
        chars.remove(char)
        token += char

    return token


def test_returns_default_string_length_32():
    assert len(generate_secure_token()) == 32


@pytest.mark.skip()
def test_returns_string_length_provided():
    assert len(generate_secure_token(48)) == 48


@pytest.mark.skip()
def test_returns_string_with_each_of_char_types():
    from re import search
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation

    token = generate_secure_token()
    has_char_types = []

    for char_type in ascii_uppercase, ascii_lowercase, digits, punctuation:
        has_char_types.append(search(fr'[{char_type}]+', token))

    assert all(has_char_types)


@pytest.mark.skip()
def test_returns_string_with_min_3_punctuation_chars():
    import string
    token = generate_secure_token()

    punctuation_chars = [char for char in token if char in string.punctuation]

    assert len(punctuation_chars) >= 3


@pytest.mark.skip()
def test_returns_string_with_min_5_upper_case_chars():
    token = generate_secure_token()

    upper_case_chars = [char for char in token if char.isupper()]

    assert len(upper_case_chars) >= 5


@pytest.mark.skip()
def test_returns_string_with_min_5_numeric_chars():
    token = generate_secure_token()

    numeric_chars = [char for char in token if char.isdigit()]

    assert len(numeric_chars) >= 5


@pytest.mark.skip()
def test_returns_string_with_min_length_32_when_passed_int_less_than_32():
    assert len(generate_secure_token(10)) == 32


@pytest.mark.skip()
def test_tokens_are_unique():
    tokens = set()

    for _ in range(100):
        tokens.add(generate_secure_token())
    assert len(tokens) == 100


@pytest.mark.skip()
def test_tokens_character_types_are_in_mixed_order():
    from re import findall
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation

    char_types = [ascii_lowercase, ascii_uppercase, digits, punctuation]

    for _ in range(100):
        token = generate_secure_token()
        for char_type in char_types:
            char_groups = findall(fr'[{char_type}]+', token)
            assert len(char_groups) > 1
