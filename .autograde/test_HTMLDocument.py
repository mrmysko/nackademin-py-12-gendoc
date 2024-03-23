from HTMLDocument import HTMLDocument


def test_render_small_heading1():
    doc = HTMLDocument()
    doc.add_heading1("Heading 1")
    expected = "<h1>Heading 1</h1>"
    assert doc.render() == expected


def test_render_small_heading2():
    doc = HTMLDocument()
    doc.add_heading2("Heading 2")
    expected = "<h2>Heading 2</h2>"
    assert doc.render() == expected


def test_render_small_heading3():
    doc = HTMLDocument()
    doc.add_heading3("Heading 3")
    expected = "<h3>Heading 3</h3>"
    assert doc.render() == expected


def test_render_small_paragraph():
    doc = HTMLDocument()
    doc.add_paragraph("Text")
    expected = "<p>Text</p>"
    assert doc.render() == expected


def test_render_small_codeblock():
    doc = HTMLDocument()
    doc.add_codeblock("x = 1")
    expected = "<pre><code>x = 1</code></pre>"
    assert doc.render() == expected


def test_render_amp_heading1():
    doc = HTMLDocument()
    doc.add_heading1("Test & in heading 1")
    expected = "<h1>Test &amp; in heading 1</h1>"
    assert doc.render() == expected


def test_render_amp_heading2():
    doc = HTMLDocument()
    doc.add_heading2("Test & in heading 2")
    expected = "<h2>Test &amp; in heading 2</h2>"
    assert doc.render() == expected


def test_render_amp_heading3():
    doc = HTMLDocument()
    doc.add_heading3("Test & in heading 3")
    expected = "<h3>Test &amp; in heading 3</h3>"
    assert doc.render() == expected


def test_render_amp_paragraph():
    doc = HTMLDocument()
    doc.add_paragraph("Test & in paragraph")
    expected = "<p>Test &amp; in paragraph</p>"
    assert doc.render() == expected


def test_render_amp_codeblock():
    doc = HTMLDocument()
    doc.add_codeblock("foo(&window) {..}")
    expected = "<pre><code>foo(&amp;window) {..}</code></pre>"
    assert doc.render() == expected


def test_render_newline_heading1():
    doc = HTMLDocument()
    doc.add_heading1("Test \n in heading 1")
    expected = "<h1>Test <br> in heading 1</h1>"
    assert doc.render() == expected


def test_render_newline_heading2():
    doc = HTMLDocument()
    doc.add_heading2("Test \n in heading 2")
    expected = "<h2>Test <br> in heading 2</h2>"
    assert doc.render() == expected


def test_render_newline_heading3():
    doc = HTMLDocument()
    doc.add_heading3("Test \n in heading 3")
    expected = "<h3>Test <br> in heading 3</h3>"
    assert doc.render() == expected


def test_render_newline_paragraph():
    doc = HTMLDocument()
    doc.add_paragraph("Test \n in paragraph")
    expected = "<p>Test <br> in paragraph</p>"
    assert doc.render() == expected


def test_render_newline_untouched_in_codeblock():
    doc = HTMLDocument()
    doc.add_codeblock("def bar(txt):\n    print(txt.upper())")
    expected = "<pre><code>def bar(txt):\n    print(txt.upper())</code></pre>"
    assert doc.render() == expected


def test_example_heading1_empty():
    doc = HTMLDocument()
    doc.add_heading1("")
    expected = "<h1></h1>"
    assert doc.render() == expected


def test_example_kebabtårta():
    doc = HTMLDocument()
    doc.add_heading1("Kebabtårta")
    expected = "<h1>Kebabtårta</h1>"
    assert doc.render() == expected


def test_example_poem_flows():
    doc = HTMLDocument()
    doc.add_heading1(
        "In a world where code flows like a fountain,\nPython reigns, a versatile mountain."
    )
    expected = "<h1>In a world where code flows like a fountain,<br>Python reigns, a versatile mountain.</h1>"
    assert doc.render() == expected


def test_example_strong_liquor():
    doc = HTMLDocument()
    doc.add_heading1("<strong>liquor</strong>")
    expected = "<h1>&lt;strong&gt;liquor&lt;/strong&gt;</h1>"
    assert doc.render() == expected


def test_example_codeblock():
    doc = HTMLDocument()
    doc.add_codeblock(
        "<marquee>\n  <blink>\n    <h1>WELCOME TO MY WEBSITE</h1>\n    1990's called, they want their marquee back.\n  </blink>\n</marquee>"
    )
    expected = "<pre><code>&lt;marquee&gt;\n  &lt;blink&gt;\n    &lt;h1&gt;WELCOME TO MY WEBSITE&lt;/h1&gt;\n    1990&#39;s called, they want their marquee back.\n  &lt;/blink&gt;\n&lt;/marquee&gt;</code></pre>"
    assert doc.render() == expected


def test_example_poem_serenity():
    doc = HTMLDocument()
    doc.add_heading1("Serenity in Syntax").add_paragraph(
        "Gentle logic flows,\nPython's calm, a stream that grows,\nIn code, tranquility shows."
    )

    expected = "<h1>Serenity in Syntax</h1><p>Gentle logic flows,<br>Python&#39;s calm, a stream that grows,<br>In code, tranquility shows.</p>"
    assert doc.render() == expected


def test_example_multiple():
    doc = HTMLDocument()
    doc.add_heading1("A poetic embrace in code").add_paragraph(
        "Created by a self-aware AI."
    ).add_codeblock(
        """sky = "vast"; dreams = "deep"
echo = lambda sky, dreams: f"The {sky} holds the {dreams}"
print(echo(sky, dreams))"""
    )

    expected = "<h1>A poetic embrace in code</h1><p>Created by a self-aware AI.</p><pre><code>sky = &quot;vast&quot;; dreams = &quot;deep&quot;\necho = lambda sky, dreams: f&quot;The {sky} holds the {dreams}&quot;\nprint(echo(sky, dreams))</code></pre>"
    assert doc.render() == expected
