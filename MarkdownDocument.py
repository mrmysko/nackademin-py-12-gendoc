from GenericDocument import GenericDocument


class MarkdownDocument(GenericDocument):

    def render_heading1(self, text):
        return "<h1>" + text + "</h1>"

    def render_heading2(self, text):
        return "<h2>" + text + "</h2>"

    def render_heading3(self, text):
        return "<h3>" + text + "</h3>"

    def render_paragraph(self, text):
        return "<p>" + text + "<p>"

    def render_codeblock(self, text):
        return "<code>" + text + "</code"


markdown = MarkdownDocument()
markdown.add_heading1("Heading 1")
markdown.add_heading2("Heading 2")
markdown.add_heading3("Heading 3")
markdown.add_paragraph("Här är body-text i markdown.")
markdown.add_codeblock("i = 0\nwhile i != 3\n\ti += 1\n")

print(markdown.render())
