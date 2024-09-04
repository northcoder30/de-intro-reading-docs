from test_api.checks import run_test, format_err_msg
from fractions import Fraction

def add_decimals(fractions_to_add):
    floatval = [eval(i) for i in fractions_to_add]
    tot = 0
    for num in range(0,len(floatval)):
        tot += Fraction(floatval[num]).limit_denominator()
    return str(float(tot))       


@run_test
def test_add_decimals():
    assert add_decimals(["0.1", "0.2"]) == "0.3", \
        format_err_msg("0.3", add_decimals(["0.1", "0.2"]))

    assert add_decimals(["0.1", "0.1", "0.1", "0.1"]) == "0.4", \
        format_err_msg("0.4", add_decimals(["0.1", "0.1", "0.1", "0.1"]))


if __name__ == '__main__':
    test_add_decimals()
