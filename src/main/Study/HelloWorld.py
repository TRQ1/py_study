class Hello:
    def shows(self, words):
       self.words = words
       print(words)

if __name__ == '__main__':
    views = Hello()
    views.shows('Hello, World')
