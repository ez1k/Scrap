class Quote:
    def __init__(self, text, author, tags):
        self.text = text
        self.author = author
        self.tags = tags

    def __repr__(self):
        return f'{{"text": "{self.text}", "by": "{self.author}", "tags": {self.tags}}}'
