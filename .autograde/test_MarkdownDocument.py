from MarkdownDocument import MarkdownDocument


def test_render_small_heading1():
    doc = MarkdownDocument()
    doc.add_heading1("Heading 1")
    expected = "# Heading 1\n\n"
    assert doc.render() == expected


def test_render_small_heading2():
    doc = MarkdownDocument()
    doc.add_heading2("Heading 2")
    expected = "## Heading 2\n\n"
    assert doc.render() == expected


def test_render_small_heading3():
    doc = MarkdownDocument()
    doc.add_heading3("Heading 3")
    expected = "### Heading 3\n\n"
    assert doc.render() == expected


def test_render_small_paragraph():
    doc = MarkdownDocument()
    doc.add_paragraph("Text")
    expected = "Text\n\n"
    assert doc.render() == expected


def test_render_small_codeblock():
    doc = MarkdownDocument()
    doc.add_codeblock("x = 1")
    expected = "```\nx = 1\n```\n\n"
    assert doc.render() == expected


def test_render_backtick_heading1():
    doc = MarkdownDocument()
    doc.add_heading1("Test ` in heading 1")
    expected = "# Test \\` in heading 1\n\n"
    assert doc.render() == expected


def test_render_backtick_heading2():
    doc = MarkdownDocument()
    doc.add_heading2("Test ` in heading 2")
    expected = "## Test \\` in heading 2\n\n"
    assert doc.render() == expected


def test_render_backtick_heading3():
    doc = MarkdownDocument()
    doc.add_heading3("Test ` in heading 3")
    expected = "### Test \\` in heading 3\n\n"
    assert doc.render() == expected


def test_render_backtick_paragraph():
    doc = MarkdownDocument()
    doc.add_paragraph("Test ` in paragraph")
    expected = "Test \\` in paragraph\n\n"
    assert doc.render() == expected


def test_render_backtick_codeblock():
    doc = MarkdownDocument()
    doc.add_codeblock("greet(`${name}san`)")
    expected = "```\ngreet(\\`${name}san\\`)\n```\n\n"
    assert doc.render() == expected


def test_render_newline_heading1():
    doc = MarkdownDocument()
    doc.add_heading1("Test \n in heading 1")
    expected = "# Test   in heading 1\n\n"
    assert doc.render() == expected


def test_render_newline_heading2():
    doc = MarkdownDocument()
    doc.add_heading2("Test \n in heading 2")
    expected = "## Test   in heading 2\n\n"
    assert doc.render() == expected


def test_render_newline_heading3():
    doc = MarkdownDocument()
    doc.add_heading3("Test \n in heading 3")
    expected = "### Test   in heading 3\n\n"
    assert doc.render() == expected


def test_render_newline_untouched_in_paragraph():
    doc = MarkdownDocument()
    doc.add_paragraph("Test \n in paragraph")
    expected = "Test \n in paragraph\n\n"
    assert doc.render() == expected


def test_render_newline_untouched_in_codeblock():
    doc = MarkdownDocument()
    doc.add_codeblock("def bar(txt):\n    print(txt.upper())")
    expected = "```\ndef bar(txt):\n    print(txt.upper())\n```\n\n"
    assert doc.render() == expected


def test_example_heading1_empty():
    doc = MarkdownDocument()
    doc.add_heading1("")
    expected = "# \n\n"
    assert doc.render() == expected


def test_example_kebabtårta():
    doc = MarkdownDocument()
    doc.add_heading1("Kebabtårta")
    expected = "# Kebabtårta\n\n"
    assert doc.render() == expected


def test_example_poem_flows():
    doc = MarkdownDocument()
    doc.add_heading1(
        "In a world where code flows like a fountain,\nPython reigns, a versatile mountain."
    )
    expected = "# In a world where code flows like a fountain, Python reigns, a versatile mountain.\n\n"
    assert doc.render() == expected


def test_example_strong_liquor():
    doc = MarkdownDocument()
    doc.add_heading1("<strong>liquor</strong>")
    expected = "# <strong>liquor</strong>\n\n"
    assert doc.render() == expected


def test_example_codeblock():
    doc = MarkdownDocument()
    doc.add_codeblock(
        "<marquee>\n  <blink>\n    <h1>WELCOME TO MY WEBSITE\n    1990's called, they want their marquee back.\n  </blink>\n</marquee>"
    )
    expected = "```\n<marquee>\n  <blink>\n    <h1>WELCOME TO MY WEBSITE\n    1990's called, they want their marquee back.\n  </blink>\n</marquee>\n```\n\n"

    assert doc.render() == expected


def test_example_poem_serenity():
    doc = MarkdownDocument()
    doc.add_heading1("Serenity in Syntax").add_paragraph(
        "Gentle logic flows,\nPython's calm, a stream that grows,\nIn code, tranquility shows."
    )

    expected = "# Serenity in Syntax\n\nGentle logic flows,\nPython's calm, a stream that grows,\nIn code, tranquility shows.\n\n"
    assert doc.render() == expected


def test_example_multiple():
    doc = MarkdownDocument()
    doc.add_heading1("A poetic embrace in code").add_paragraph(
        "Created by a self-aware AI."
    ).add_codeblock(
        'sky = "vast"; dreams = "deep"\necho = lambda sky, dreams: f"The {sky} holds the {dreams}"\nprint(echo(sky, dreams))'
    )

    expected = '# A poetic embrace in code\n\nCreated by a self-aware AI.\n\n```\nsky = "vast"; dreams = "deep"\necho = lambda sky, dreams: f"The {sky} holds the {dreams}"\nprint(echo(sky, dreams))\n```\n\n'

    assert doc.render() == expected
