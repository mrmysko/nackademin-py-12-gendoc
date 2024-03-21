from GenericDocument import GenericDocument
from PartType import Part


class MarkdownDocument(GenericDocument):
    def render(self):
        for type, line in self._document_parts:
            match type:
                case Part.HEADING1:
                    print("# " + line)
                case Part.HEADING2:
                    print("## " + line)
                case Part.HEADING3:
                    print("### " + line)
                case Part.PARAGRAPH:
                    print(line)
                case Part.CODEBLOCK:
                    print("```" + line + "```")
                case _:
                    pass

    def render_paragraph(self, text):
        pass


markdown = MarkdownDocument()
markdown.add_heading1("Heading 1")
markdown.add_heading2("Heading 2")
markdown.add_heading3("Heading 3")
markdown.add_paragraph("Här är body-text i markdown.")
markdown.add_codeblock("i = 0\nwhile i != 3\n\ti += 1\n")

markdown.render()
