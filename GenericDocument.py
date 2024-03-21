from PartType import Part
from abc import ABC, abstractmethod


class GenericDocument(ABC):
    def __init__(self):
        self._document_parts = list()

    def __str__(self):
        return self.result

    def add_heading1(self, text):
        self._document_parts.append((Part.HEADING1, text))
        return self

    def add_heading2(self, text):
        self._document_parts.append((Part.HEADING2, text))
        return self

    def add_heading3(self, text):
        self._document_parts.append((Part.HEADING3, text))
        return self

    def add_paragraph(self, text):
        self._document_parts.append((Part.PARAGRAPH, text))
        return self

    def add_codeblock(self, text):
        self._document_parts.append((Part.CODEBLOCK, text))
        return self

    def merge_indices(self, dst_index, *src_indices, sep="\n"):
        """pop remove index of line, get tuple value [1] and add to dst tuple[1]."""
        for type, line in self._document_parts:
            print(type, line)

    def merge_consecutive(self, partType):
        for type, line in self._document_parts:
            print(type, line)

    """for line, if type[line index] and type[line index + 1] == samma, merge"""

    def render(self):

        # Rätt output (utom en newline i början).
        # Hur använder jag getattr? Och får in prion? Och vad är det för text den här funktionen ska ta in?
        self.result = ""
        for type, line in self._document_parts:
            if type.value == 1:
                self.result = self.result + "\n" + "".join(self.render_heading1(line))
            elif type.value == 2:
                self.result = self.result + "\n" + "".join(self.render_heading2(line))
            elif type.value == 3:
                self.result = self.result + "\n" + "".join(self.render_heading3(line))
            elif type.value == 4:
                self.result = self.result + "\n" + "".join(self.render_paragraph(line))
            elif type.value == 5:
                self.result = self.result + "\n" + "".join(self.render_codeblock(line))
            else:
                raise Exception

        return self.result

    @abstractmethod
    def render_paragraph(text):
        pass
