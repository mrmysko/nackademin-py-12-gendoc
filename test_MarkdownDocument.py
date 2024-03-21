import pytest

markdown_test = Markdown()
markdown_test.add_heading1("Heading 1")
markdown_test.add_heading2("Heading 2")
markdown_test.add_heading3("Heading 3")
markdown_test.add_paragraph("Här är body-text i markdown.")
markdown_test.add_codeblock("Code-block")

print()
markdown_test.render()
