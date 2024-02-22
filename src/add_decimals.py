import pytest


def add_decimals(fractions_to_add):
    pass


@pytest.mark.it("Should correctly add decimals without precision errors")
def test_add_decimals():
    assert add_decimals(["0.1", "0.2"]) == "0.3"
    assert add_decimals(["0.1", "0.1", "0.1", "0.1"]) == "0.4"
