import pytest


def remove_mark_down_headings(markdown_heading):
    pass


@pytest.mark.it("Should remove single # markdown heading")
def test_remove_mark_down_headings():
    assert remove_mark_down_headings("# Title") == "Title"


@pytest.mark.skip()
@pytest.mark.it("Should remove multiple # markdown headings")
def test_remove_multiple_mark_down_headings():
    assert remove_mark_down_headings("## Sub Heading") == "Sub Heading"
    assert remove_mark_down_headings("### level 3") == "level 3"
