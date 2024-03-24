from GenericDocument import GenericDocument
from PartType import PartType as Part


class MarkdownDocument(GenericDocument):

    #@classmethod
    #def escape_markdown(cls, text):
    #    return text.replace("\\", "\\\\").replace("`", "\\`").replace("#", "\\#")

    # Headings have to split on newline and add # to every line.
    def render_heading1(self, text):
        return f'# {text.replace("\n", " ").replace("`", "\\`")}\n\n'

    def render_heading2(self, text):
        return f'## {text.replace("\n", " ").replace("`", "\\`")}\n\n'

    def render_heading3(self, text):
        return f'### {text.replace("\n", " ").replace("`", "\\`")}\n\n'

    def render_paragraph(self, text):
        return f'{text.replace("`", "\\`")}\n\n'

    def render_codeblock(self, text):
        return f"```\n{text.replace("`", "\\`")}\n```\n\n"


if __name__ == "__main__":

    markdown = MarkdownDocument()

    markdown.add_heading1("Heading ## 1") # -> "# Heading ## 1" Visas korrekt 

    markdown.render()
    print(markdown)
