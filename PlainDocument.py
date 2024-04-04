from GenericDocument import GenericDocument


class PlainDocument(GenericDocument):
    def render_paragraph(self, text):
        return f"{text}\n\n"


plain = PlainDocument()

plain.add_heading1("Heading 1")
plain.add_paragraph("Paragraph1")
plain.add_paragraph("Paragraph2")

plain.render()

print(plain)
