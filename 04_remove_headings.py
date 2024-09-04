from test_api.checks import run_test, skip_test, format_err_msg
import re

def remove_mark_down_headings(markdown_heading):
    removed_heading = re.sub(r'^[^A-Za-z]*', '',markdown_heading)
    return removed_heading

@run_test
def test_remove_single_mark_down_headings():
    assert remove_mark_down_headings("# Title") == "Title", \
        format_err_msg("Title", remove_mark_down_headings("# Title"))


@run_test
def test_remove_multiple_mark_down_headings():
    assert remove_mark_down_headings("## Sub Heading") == "Sub Heading", \
        format_err_msg(
            "Sub Heading", remove_mark_down_headings("## Sub Heading"))

    assert remove_mark_down_headings("### level 3") == "level 3", \
        format_err_msg(
            "level 3", remove_mark_down_headings("### level 3"))


if __name__ == '__main__':
    test_remove_single_mark_down_headings()
    test_remove_multiple_mark_down_headings()
