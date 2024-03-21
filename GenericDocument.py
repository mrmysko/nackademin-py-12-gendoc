from PartType import Part
from abc import ABC, abstractmethod


class GenericDocument(ABC):
    def __init__(self):
        self._document = list()

    def add_heading1(self, text):
        self._document.append((Part.HEADING1, text))
        return self

    def add_heading2(self, text):
        self._document.append((Part.HEADING2, text))
        return self

    def add_heading3(self, text):
        self._document.append((Part.HEADING3, text))
        return self

    def add_paragraph(self, text):
        self._document.append((Part.PARAGRAPH, text))
        return self

    def add_codeblock(self, text):
        self._document.append((Part.CODEBLOCK, text))

    def merge_indices(self, dst_index, *src_indices, sep):
        pass

    def merge_consecutive(self, partType):
        pass

    def render(text):
        pass

    @abstractmethod
    def render_paragraph(text):
        pass
