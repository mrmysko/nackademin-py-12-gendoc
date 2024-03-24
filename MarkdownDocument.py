from GenericDocument import GenericDocument
from PartType import PartType as Part


class MarkdownDocument(GenericDocument):

    # Headings have to split on newline and add # to every line.
    def render_heading1(self, text):
        # Should merged headings end on one or two newlines?
        #text = f"# {self.escape_markdown(text)}"
        return f'# {text.replace("\n", " ").replace("`", "\\`")}\n\n'

    def render_heading2(self, text):
        #text = f"## {self.escape_markdown(text)}"
        return f'## {text.replace("\n", " ").replace("`", "\\`")}\n\n'

    def render_heading3(self, text):
        #text = f"### {self.escape_markdown(text)}"
        return f'### {text.replace("\n", " ").replace("`", "\\`")}\n\n'

    def render_paragraph(self, text):
        return f' {text.replace("`", "\\`")} \n\n'

    def render_codeblock(self, text):
        return f"```\n{text.replace("`", "\\`")}\n```\n\n"


if __name__ == "__main__":

    markdown = MarkdownDocument()


    # So...the default separator in merge methods i newlines, the return values of those is a tuple of (obj, str).
    # So a string coming from a merge method is impossible to separate from an in-string newline at this point.
    # Here like a "\n".join(<list of merged strings>) would have to come in instead of a replace...but the methods expect a text.
    markdown.add_heading1("A poetic embrace in code").add_paragraph(
        "Created by a self-aware AI."
    ).add_codeblock(
        'sky = "vast"; dreams = "deep"\necho = lambda sky, dreams: f"The {sky} holds the {dreams}"\nprint(echo(sky, dreams))'
    )

    markdown.render()
    print(markdown)
