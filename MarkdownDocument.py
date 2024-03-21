from GenericDocument import GenericDocument


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
        text = "# " + self.escape_markdown(text)
        return text.replace("\n", "\n# ")

    def render_heading2(self, text):
        text = "## " + self.escape_markdown(text)
        return text.replace("\n", "\n## ")

    def render_heading3(self, text):
        text = "### " + self.escape_markdown(text)
        return text.replace("\n", "\n### ")

    def render_paragraph(self, text):
        return " " + self.escape_markdown(text) + " "

    def render_codeblock(self, text):
        return "```" + self.escape_markdown(text) + "```"


markdown = MarkdownDocument()
markdown.add_heading1("Heading 1\nHeading1.0")
markdown.add_heading2("Heading 2")
markdown.add_heading3("Heading 3")
markdown.add_paragraph("Här är body-text i markdown.")
markdown.add_codeblock("i = 0\nwhile i != 3\n\ti += 1\n")


markdown.merge_indices(1, 2, 3)

markdown.render()
print(markdown)
