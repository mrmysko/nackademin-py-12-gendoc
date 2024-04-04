from PlainDocument import PlainDocument
from PartType import PartType


def test_codeblock_limerick():
    doc = PlainDocument()
    doc.add_codeblock(
        "Limericks I cannot compose,\n With noxious smells in my nose.\n But this one was easy,\n I only felt queasy,\n Because I was sniffing my toes."
    )
    doc.render() == "Limericks I cannot compose,\n With noxious smells in my nose.\n But this one was easy,\n I only felt queasy,\n Because I was sniffing my toes.\n\n"


def test_heading1_brother():
    doc = PlainDocument()
    doc.add_heading1("Brother")
    assert doc.render() == "Brother\n\n"


def test_heading2_a_tale_of_two_sons():
    doc = PlainDocument()
    doc.add_heading2("A tale of two sons")
    assert doc.render() == "A tale of two sons\n\n"


def test_paragraph_lorem_ipsum():
    doc = PlainDocument()
    doc.add_paragraph("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    assert (
        doc.render() == "Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n\n"
    )


def test_merge_consecutive_heading3_fruits():
    doc = PlainDocument()
    doc.add_heading3("Apple").add_heading3("Banana").add_heading3("Orange")
    doc.merge_consecutive(PartType.HEADING3)
    assert doc.render() == "Apple\nBanana\nOrange\n\n"
