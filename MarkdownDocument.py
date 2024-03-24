from GenericDocument import GenericDocument
from PartType import PartType as Part


class MarkdownDocument(GenericDocument):

    @classmethod
    def escape_markdown(cls, text):
        # Exempel på en enkel escape-funktion, den kan behöva utökas lite men ramla
        # inte ned i det bottenlösa hål som innebär att få denna funktion perfekt.
        parts = text.split("`")
        for i in range(len(parts)):
            if i % 2 == 0:  # Utanför backticks
                parts[i] = parts[i].replace("\\", "\\\\").replace("#", "\\#")
            else:  # Inom backticks
                parts[i] = parts[i].replace("`", "\\`")
        return "`".join(parts)

    # Headings have to split on newline and add # to every line.
    def render_heading1(self, text):
        # Should merged headings end on one or two newlines?
        text = f"# {self.escape_markdown(text)}"
        return f'{text.replace("\n", "\n# ")}\n'

    def render_heading2(self, text):
        text = f"## {self.escape_markdown(text)}"
        return f'{text.replace("\n", "\n## ")}\n'

    def render_heading3(self, text):
        text = f"### {self.escape_markdown(text)}"
        return f'{text.replace("\n", "\n### ")}\n'

    def render_paragraph(self, text):
        return f" {self.escape_markdown(text)} \n"

    def render_codeblock(self, text):
        return f"```\n{self.escape_markdown(text)}\n```\n"


markdown = MarkdownDocument()

markdown.add_heading1("Heading 1.1")
markdown.add_heading1("Heading 1.2")
markdown.add_heading1("Heading 1.3")
markdown.add_heading2("Heading 2.1")
markdown.add_heading2("Heading 2.2")
markdown.add_heading1("Heading 1.4")
markdown.add_codeblock('Codeblock:\n\tSome code:\n\t\tsys.exit("NAN")')
markdown.add_paragraph("Paragraph")


# markdown.merge_consecutive(Part.HEADING1)
markdown.merge_indices(2, 1, 6)

markdown.render()
print(markdown)
