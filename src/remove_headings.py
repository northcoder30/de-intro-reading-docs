import pytest


def remove_mark_down_headings(markdown_heading):
    pass


def test_remove_single_mark_down_headings():
    assert remove_mark_down_headings("# Title") == "Title"


@pytest.mark.skip()
def test_remove_multiple_mark_down_headings():
    assert remove_mark_down_headings("## Sub Heading") == "Sub Heading"
    assert remove_mark_down_headings("### level 3") == "level 3"
