from GenericDocument import GenericDocument
from PartType import Part


class HTMLDocument(GenericDocument):
    def render(self):

        for type, line in self._document_parts:
            match type:
                case Part.HEADING1:
                    print("<h1>" + line + "</h1>")
                case Part.HEADING2:
                    print("<h2>" + line + "</h2>")
                case Part.HEADING3:
                    print("<h3>" + line + "</h3>")
                case Part.PARAGRAPH:
                    print("<p>" + line + "</p>")
                case Part.CODEBLOCK:
                    print("<code>" + line + "</code>")
                case _:
                    pass

    def render_paragraph(self, text):
        pass


html = HTMLDocument()

html.add_heading1("Heading 1")
html.add_heading2("Heading 2")
html.add_heading3("Heading 3")
html.add_paragraph("Paragraph1")
html.add_paragraph("Paragraph2")
html.add_codeblock("i = 0\nwhile i != 3\n\ti += 1\n")

html.merge_consecutive(Part.PARAGRAPH)

html.render()
