import GenericDocument


class HTML(GenericDocument):
    def render(self):

        for type, line in self._document:
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
