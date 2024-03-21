import pytest

html_test = HTML()
html_test.add_heading1("Heading 1")
html_test.add_heading2("Heading 2")
html_test.add_heading3("Heading 3")
html_test.add_paragraph("Det här är lite brödtext")
html_test.add_codeblock("Code-block")

print()
html_test.render()
