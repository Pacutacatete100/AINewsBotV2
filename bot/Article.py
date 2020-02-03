class Article:
    def __init__(self, title, summary, link):
        self.title = title
        self.summary = summary
        self.link = link

    def matches_search(self, *args):
        for word in args:
            if word in self.title:
                return True
        return False
