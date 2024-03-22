from PartType import Part
from abc import ABC, abstractmethod


class GenericDocument(ABC):
    def __init__(self):
        self._document_parts = list()
        self.result = ""

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

        # 6 lines for this? Yikes, refactor...
        # Assign old type and line
        old_type, old_line = self._document_parts[dst_index]
        mod_list = list()
        mod_list.append(old_line)
        # Add document lines to temporary list.
        mod_list.extend([self._document_parts[index][1] for index in src_indices])

        # Join list elements and add at old index.
        self._document_parts[dst_index] = (old_type, sep.join(mod_list))

        # Remove source indexes in reverse order, forward order decrements following elements, so 1, 2 src_indices would remove index 1, 3.
        [self._document_parts.pop(index) for index in reversed(src_indices)]

        return self

    def merge_consecutive(self, partType):

        mod_list = list()
        for index, (part, line) in enumerate(self._document_parts):
            if part == partType:
                mod_list.append(index)

        # So this is a list of indices with the right partType...
        # Now smash together consecutive numbers into the first element of a consecutive sequence.
        print(mod_list)

        # Adds indices after partType match to src_indices if they match partType
        # Doesnt work on multiple separate consecutives.
        # src_indices = [
        #    index
        #    for index, (type, line) in enumerate(self._document_parts)
        #    if type.name == partType
        #    and self._document_parts[index - 1][0].name == partType
        # ]

        # self.merge_indices(src_indices[0] - 1, *src_indices)

        return self

    def render(self):

        # Rätt output.
        # Hur använder jag getattr? Och får in prion? Och vad är det för text den här funktionen ska ta in?
        self.result = ""
        for type, line in self._document_parts:
            if type.value == 1:
                self.result = self.result + "".join(self.render_heading1(line)) + "\n"
            elif type.value == 2:
                self.result = self.result + "".join(self.render_heading2(line)) + "\n"
            elif type.value == 3:
                self.result = self.result + "".join(self.render_heading3(line)) + "\n"
            elif type.value == 4:
                self.result = self.result + "".join(self.render_paragraph(line)) + "\n"
            elif type.value == 5:
                self.result = self.result + "".join(self.render_codeblock(line)) + "\n"
            else:
                raise Exception

        return self.result

    @abstractmethod
    def render_paragraph(text):
        pass
