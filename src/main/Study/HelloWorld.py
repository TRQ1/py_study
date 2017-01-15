class Hello:
    def shows(self, words):
       self.words = words
       print(words)

views = Hello()
views.shows('Hello, World')
