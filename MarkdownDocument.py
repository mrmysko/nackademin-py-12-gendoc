import GenericDocument


class Markdown(GenericDocument):
    def render(self):
        for type, line in self._document:
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
