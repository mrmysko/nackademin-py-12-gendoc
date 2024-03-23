from PartType import Part
from abc import ABC, abstractmethod

# Todo - Refactor everything...


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
        part_index = list()

        # Iterate over lines in document.
        for index, (part, line) in enumerate(self._document_parts):
            # print(f"DEBUG: {index} {type(part)} {part} {part.value} {part.name} {line}")

            # If the part is same as partType
            if part == partType:
                # Set that index as the start of the consecutive sequence.
                part_index.append(index)

                # Add that line to the list.
                mod_list.append(line)

            # Commit to document and reset if part is not correct type and mod_list is not empty.
            elif mod_list:
                # Add the appended line at correct index.
                self._document_parts[part_index[0]] = (partType, "\n".join(mod_list))
                # print(f"INSERTED TUPLE: {self._document_parts[part_index[0]]}")

                # Set merged lines to None, removing them in the loop creates issues with indexing.
                for index in part_index[1:]:
                    self._document_parts[index] = None

                # Reset insert_index and mod_list.
                part_index = list()
                mod_list = list()

        # If part is partType on the last iteration the last append wont happen, so need to run it once outside the loop.
        if mod_list:
            self._document_parts[part_index[0]] = (partType, "\n".join(mod_list))
            for index in part_index[1:]:
                self._document_parts[index] = None

        # Remove None lines.
        self._document_parts = [
            pair for pair in self._document_parts if pair is not None
        ]

        return self

    def render(self):

        # This is very clunky.......
        for part, line in self._document_parts:

            # Heading 1 prio
            if part == Part.HEADING1:
                if getattr(self, "render_heading1", None):
                    self.result = (
                        f'{self.result}{"".join(self.render_heading1(line))}\n'
                    )
                else:
                    self.result = (
                        f'{self.result}{"".join(self.render_paragraph(line))}\n'
                    )

            # Heading 2 prio
            elif part == Part.HEADING2:
                if getattr(self, "render_heading2", None):
                    self.result = (
                        f'{self.result}{"".join(self.render_heading2(line))}\n'
                    )
                elif getattr(self, "render_heading1", None):
                    self.result = (
                        f'{self.result}{"".join(self.render_heading1(line))}\n'
                    )
                else:
                    self.result = (
                        f'{self.result}{"".join(self.render_paragraph(line))}\n'
                    )

            # Heading 3 prio
            elif part == Part.HEADING3:
                if getattr(self, "render_heading3", None):
                    self.result = (
                        f'{self.result}{"".join(self.render_heading3(line))}\n'
                    )
                elif getattr(self, "render_heading2", None):
                    self.result = (
                        f'{self.result}{"".join(self.render_heading2(line))}\n'
                    )
                elif getattr(self, "render_heading1", None):
                    self.result = (
                        f'{self.result}{"".join(self.render_heading1(line))}\n'
                    )
                else:
                    self.result = (
                        f'{self.result}{"".join(self.render_paragraph(line))}\n'
                    )

            # Codeblock prio
            elif part == Part.CODEBLOCK:
                if getattr(self, "render_codeblock", None):
                    self.result = (
                        f'{self.result}{"".join(self.render_codeblock(line))}\n'
                    )
                else:
                    self.result = (
                        f'{self.result}{"".join(self.render_paragraph(line))}\n'
                    )

            # If part is something thats not been handled so far, try to render it as a paragraph. Else raise exception.
            else:
                if getattr(self, "render_paragraph", None):
                    self.result = (
                        f'{self.result}{"".join(self.render_paragraph(line))}\n'
                    )
                else:
                    raise Exception

        return self.result

    @abstractmethod
    def render_paragraph(text):
        pass
