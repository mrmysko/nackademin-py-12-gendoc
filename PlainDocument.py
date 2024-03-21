from GenericDocument import GenericDocument


class PlainDocument(GenericDocument):

    def render_paragraph(self, text):
        return text + "\n\n"


plain = PlainDocument()

plain.add_paragraph("Paragraph")

plain.render()

print(plain)
