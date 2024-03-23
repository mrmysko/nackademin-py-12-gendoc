import pytest
from GenericDocument import GenericDocument
from PartType import PartType


def element_marker(element_id, text):
    return f"{element_id}({text})"


class WithParagraph(GenericDocument):
    def render_paragraph(self, text):
        return element_marker("p", text)


class WithHeading1(WithParagraph):
    def render_heading1(self, text):
        return element_marker("h1", text)


class WithHeading2(WithParagraph):
    def render_heading2(self, text):
        return element_marker("h2", text)


class WithHeading3(WithParagraph):
    def render_heading3(self, text):
        return element_marker("h3", text)


class WithHeading1and2(WithHeading1, WithHeading2):
    pass


class WithHeading2and3(WithHeading2, WithHeading3):
    pass


class WithHeading1and3(WithHeading1, WithHeading3):
    pass


class WithHeadings(WithHeading1, WithHeading2, WithHeading3):
    pass


class WithCodeblock(WithParagraph):
    def render_codeblock(self, text):
        return element_marker("c", text)


class WithAll(WithHeadings, WithCodeblock, WithParagraph):
    def render_codeblock(self, text):
        return element_marker("c", text)


def test_existing_heading1():
    test_doc = WithHeading1()
    test_doc.add_heading1("Bella")
    assert test_doc.render() == "h1(Bella)"


def test_existing_heading2():
    test_doc = WithHeading2()
    test_doc.add_heading2("Max")
    assert test_doc.render() == "h2(Max)"


def test_existing_heading3():
    test_doc = WithHeading3()
    test_doc.add_heading3("Luna")
    assert test_doc.render() == "h3(Luna)"


def test_existing_paragraph():
    test_doc = WithParagraph()
    test_doc.add_paragraph("Charlie")
    assert test_doc.render() == "p(Charlie)"


def test_existing_codeblock():
    test_doc = WithCodeblock()
    test_doc.add_codeblock("Lucy")
    assert test_doc.render() == "c(Lucy)"


def test_existing_heading_1_2():
    test_doc = WithHeading1and2()
    test_doc.add_heading1("Bailey")
    test_doc.add_heading2("Daisy")
    assert test_doc.render() == "h1(Bailey)h2(Daisy)"


def test_existing_heading_1_3():
    test_doc = WithHeading1and3()
    test_doc.add_heading2("Buddy")
    test_doc.add_heading3("Molly")
    assert test_doc.render() == "h1(Buddy)h3(Molly)"


def test_existing_heading_2_3():
    test_doc = WithHeading2and3()
    test_doc.add_heading2("Cooper")
    test_doc.add_heading3("Sadie")
    assert test_doc.render() == "h2(Cooper)h3(Sadie)"


def test_existing_heading_1_2_3():
    test_doc = WithHeadings()
    test_doc.add_heading1("Lola").add_heading2("Rocky").add_heading3("Maggie")
    assert test_doc.render() == "h1(Lola)h2(Rocky)h3(Maggie)"


def test_heading1_fallback_to_paragraph():
    test_doc = WithParagraph()
    test_doc.add_heading1("Bear")
    assert test_doc.render() == "p(Bear)"


def test_heading2_fallback_to_heading1():
    test_doc = WithHeading1()
    test_doc.add_heading2("Duke")
    assert test_doc.render() == "h1(Duke)"


def test_heading2_fallback_to_paragraph():
    test_doc = WithParagraph()
    test_doc.add_heading2("Stella")
    assert test_doc.render() == "p(Stella)"


def test_heading3_fallback_to_heading2():
    test_doc = WithHeading2()
    test_doc.add_heading3("Zoe")
    assert test_doc.render() == "h2(Zoe)"


def test_heading3_fallback_to_heading1():
    test_doc = WithHeading1()
    test_doc.add_heading3("Toby")
    assert test_doc.render() == "h1(Toby)"


def test_heading3_fallback_to_paragraph():
    test_doc = WithParagraph()
    test_doc.add_heading3("Ruby")
    assert test_doc.render() == "p(Ruby)"


def test_codeblock_fallback_to_paragraph():
    test_doc = WithParagraph()
    test_doc.add_codeblock("Oscar")
    assert test_doc.render() == "p(Oscar)"


def test_merge_indices_two_to_first():
    test_doc = WithParagraph()
    test_doc.add_paragraph("Rosie").add_codeblock("Milo").merge_indices(0, 1, sep=",")
    assert test_doc.render() == "p(Rosie,Milo)"


def test_merge_indices_two_to_last():
    test_doc = WithParagraph()
    test_doc.add_paragraph("Ruby").add_codeblock("Jack").merge_indices(1, 0, sep=",")
    assert test_doc.render() == "p(Jack,Ruby)"


def test_merge_indices_three_to_middle_perm1():
    test_doc = WithParagraph()
    test_doc.add_paragraph("Ellie").add_codeblock("Buster").add_codeblock(
        "Chloe"
    ).merge_indices(1, 0, 2, sep=",")
    assert test_doc.render() == "p(Buster,Ellie,Chloe)"


def test_merge_indices_three_to_middle_perm2():
    test_doc = WithParagraph()
    test_doc.add_paragraph("Oliver").add_codeblock("Finn").add_codeblock(
        "Penny"
    ).merge_indices(1, 2, 0, sep=",")
    assert test_doc.render() == "p(Finn,Oliver,Penny)"


def test_merge_indices_error_src_in_dest():
    test_doc = WithParagraph()
    with pytest.raises(ValueError):
        test_doc.add_paragraph("Coco").add_codeblock("Tigger").merge_indices(
            0, 0, sep=","
        )


def test_merge_indices_remove_duplicates_in_src():
    test_doc = WithParagraph()
    test_doc.add_paragraph("Molly").add_codeblock("Felix").merge_indices(
        0, 1, 1, sep=","
    )
    assert test_doc.render() == "p(Molly,Felix)"


def test_merge_consecutive_two_last():
    test_doc = WithCodeblock()
    test_doc.add_paragraph("Sasha").add_codeblock("Louie").add_codeblock(
        "Murphy"
    ).merge_consecutive(PartType.CODEBLOCK, sep=",")
    assert test_doc.render() == "p(Sasha)c(Louie,Murphy)"


def test_merge_consecutive_two_first():
    test_doc = WithAll()
    test_doc.add_heading1("Annie").add_heading1("Harley").add_codeblock(
        "Piper"
    ).merge_consecutive(PartType.HEADING1, sep=",")
    assert test_doc.render() == "h1(Annie,Harley)c(Piper)"
