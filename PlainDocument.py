from GenericDocument import GenericDocument
from PartType import Part


class PlainDocument(GenericDocument):

    def render_paragraph(self, text):
        return text + "\n\n"


plain = PlainDocument()

plain.add_heading1("Test")

# plain.render_paragraph()

plain.render()
