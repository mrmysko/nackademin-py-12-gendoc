from GenericDocument import GenericDocument


class MarkdownDocument(GenericDocument):
    @classmethod
    def escape_markdown(cls, text):
        return text.replace("\\", "\\\\").replace("`", "\\`").replace("#", "\\#")

    def render_heading1(self, text):
        return f'# {self.escape_markdown(text).replace("\n", " ")}\n\n'

    def render_heading2(self, text):
        return f'## {self.escape_markdown(text).replace("\n", " ")}\n\n'

    def render_heading3(self, text):
        return f'### {self.escape_markdown(text).replace("\n", " ")}\n\n'

    def render_paragraph(self, text):
        return f"{self.escape_markdown(text)}\n\n"

    def render_codeblock(self, text):
        return f"```\n{text.replace("`", "\\`")}\n```\n\n"


if __name__ == "__main__":
    markdown = MarkdownDocument()

    markdown.add_heading1("Heading 1")
    markdown.add_heading1("Heading 1.1")
    markdown.add_heading1("Heading 1.2")

    markdown.add_paragraph("Some-text")

    markdown.render()
    print(markdown)
