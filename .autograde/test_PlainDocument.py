from PartType import PartType
from PlainDocument import PlainDocument


def test_render_small_heading1():
    doc = PlainDocument()
    doc.add_heading1("Heading 1")
    expected = "Heading 1\n\n"
    assert doc.render() == expected


def test_render_small_heading2():
    doc = PlainDocument()
    doc.add_heading2("Heading 2")
    expected = "Heading 2\n\n"
    assert doc.render() == expected


def test_render_small_heading3():
    doc = PlainDocument()
    doc.add_heading3("Heading 3")
    expected = "Heading 3\n\n"
    assert doc.render() == expected


def test_render_small_paragraph():
    doc = PlainDocument()
    doc.add_paragraph("Text")
    expected = "Text\n\n"
    assert doc.render() == expected


def test_render_small_codeblock():
    doc = PlainDocument()
    doc.add_codeblock("x = 1")
    expected = "x = 1\n\n"
    assert doc.render() == expected


def test_render_amp_heading1():
    doc = PlainDocument()
    doc.add_heading1("Test & in heading 1")
    expected = "Test & in heading 1\n\n"
    assert doc.render() == expected


def test_render_amp_heading2():
    doc = PlainDocument()
    doc.add_heading2("Test & in heading 2")
    expected = "Test & in heading 2\n\n"
    assert doc.render() == expected


def test_render_amp_heading3():
    doc = PlainDocument()
    doc.add_heading3("Test & in heading 3")
    expected = "Test & in heading 3\n\n"
    assert doc.render() == expected


def test_render_amp_paragraph():
    doc = PlainDocument()
    doc.add_paragraph("Test & in paragraph")
    expected = "Test & in paragraph\n\n"
    assert doc.render() == expected


def test_render_amp_codeblock():
    doc = PlainDocument()
    doc.add_codeblock("foo(&window) {..}")
    expected = "foo(&window) {..}\n\n"
    assert doc.render() == expected


def test_render_newline_heading1():
    doc = PlainDocument()
    doc.add_heading1("Test \n in heading 1")
    expected = "Test \n in heading 1\n\n"
    assert doc.render() == expected


def test_render_newline_heading2():
    doc = PlainDocument()
    doc.add_heading2("Test \n in heading 2")
    expected = "Test \n in heading 2\n\n"
    assert doc.render() == expected


def test_render_newline_heading3():
    doc = PlainDocument()
    doc.add_heading3("Test \n in heading 3")
    expected = "Test \n in heading 3\n\n"
    assert doc.render() == expected


def test_render_newline_paragraph():
    doc = PlainDocument()
    doc.add_paragraph("Test \n in paragraph")
    expected = "Test \n in paragraph\n\n"
    assert doc.render() == expected


def test_render_newline_untouched_in_codeblock():
    doc = PlainDocument()
    doc.add_codeblock("def bar(txt):\n    print(txt.upper())")
    expected = "def bar(txt):\n    print(txt.upper())\n\n"
    assert doc.render() == expected


def test_heading1_empty():
    doc = PlainDocument()
    doc.add_heading1("")
    expected = "\n\n"
    assert doc.render() == expected


def test_kebabtårta():
    doc = PlainDocument()
    doc.add_heading1("Kebabtårta")
    expected = "Kebabtårta\n\n"
    assert doc.render() == expected


def test_poem_flows():
    doc = PlainDocument()
    doc.add_heading1(
        "In a world where code flows like a fountain,\nPython reigns, a versatile mountain."
    )
    expected = "In a world where code flows like a fountain,\nPython reigns, a versatile mountain.\n\n"
    assert doc.render() == expected


def test_strong_liquor():
    doc = PlainDocument()
    doc.add_heading1("<strong>liquor</strong>")
    expected = "<strong>liquor</strong>\n\n"
    assert doc.render() == expected


def test_codeblock():
    doc = PlainDocument()
    doc.add_codeblock(
        "<marquee>\n  <blink>\n    <h1>WELCOME TO MY WEBSITE</h1>\n    1990's called, they want their marquee back.\n  </blink>\n</marquee>"
    )
    expected = "<marquee>\n  <blink>\n    <h1>WELCOME TO MY WEBSITE</h1>\n    1990's called, they want their marquee back.\n  </blink>\n</marquee>\n\n"
    assert doc.render() == expected


def test_example_poem_logic():
    doc = PlainDocument()
    doc.add_heading1("Whispers of Logic").add_paragraph(
        "Silent bytes in flow,\nPython shapes the unseen path,\nWisdom in each row."
    )

    expected = "Whispers of Logic\n\nSilent bytes in flow,\nPython shapes the unseen path,\nWisdom in each row.\n\n"

    assert doc.render() == expected


def test_example_manipulation():
    doc = PlainDocument()
    doc.add_heading1("Elegance in Code").add_paragraph(
        "Moonlight through the loops,"
    ).add_paragraph("Silent whispers, Python speaks,").add_paragraph(
        "Nature's algorithms leap."
    ).merge_consecutive(
        PartType.PARAGRAPH
    )

    expected = "Elegance in Code\n\nMoonlight through the loops,\nSilent whispers, Python speaks,\nNature's algorithms leap.\n\n"

    assert doc.render() == expected
