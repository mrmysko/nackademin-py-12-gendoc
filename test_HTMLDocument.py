from HTMLDocument import HTMLDocument
from PartType import PartType


def test_codeblock_limerick():
    doc = HTMLDocument()
    doc.add_codeblock(
        "Limericks I cannot compose,\n With noxious smells in my nose.\n But this one was easy,\n I only felt queasy,\n Because I was sniffing my toes."
    )
    doc.render() == "<pre><code>Limericks I cannot compose,\n With noxious smells in my nose.\n But this one was easy,\n I only felt queasy,\n Because I was sniffing my toes.</code></pre>"


def test_heading1_brother():
    doc = HTMLDocument()
    doc.add_heading1("Brother")
    assert doc.render() == "<h1>Brother</h1>"


def test_heading2_a_tale_of_two_sons():
    doc = HTMLDocument()
    doc.add_heading2("A tale of two sons")
    assert doc.render() == "<h2>A tale of two sons</h2>"


def test_paragraph_lorem_ipsum():
    doc = HTMLDocument()
    doc.add_paragraph("Lorem ipsum dolor sit amet, consectetur adipiscing elit.")
    assert (
        doc.render()
        == "<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>"
    )


def test_merge_consecutive_heading3_fruits():
    doc = HTMLDocument()
    doc.add_heading3("Apple").add_heading3("Banana").add_heading3("Orange")
    doc.merge_consecutive(PartType.HEADING3)
    assert doc.render() == "<h3>Apple<br>Banana<br>Orange</h3>"
