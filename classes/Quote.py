class Quote:
    def __init__(self, text, by, tags):
        self.text = text
        self.by = by
        self.tags = tags

    def __repr__(self):
        return f'{{"text": "{self.text}", "by": "{self.by}", "tags": {self.tags}}}'
