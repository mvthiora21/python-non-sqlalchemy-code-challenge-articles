class Article:
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        Article.all.append(self)
        author.add_article(self)
        magazine.add_article(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not (5 <= len(value) <= 50):
            raise ValueError("Title must be between 5 and 50 characters inclusive.")
        self._title = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be of type Author.")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be of type Magazine.")
        self._magazine = value


class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Author name must be a non-empty string.")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("Only Article instances can be added.")
        self._articles.append(article)

    def topic_areas(self):
        categories = {article.magazine.category for article in self._articles}
        return list(categories) if categories else None


class Magazine:
    all_magazines = []

    def __init__(self, name, category):
        if not (2 <= len(name) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters inclusive.")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._name = name
        self._category = category
        self._articles = []
        Magazine.all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters inclusive.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string.")
        self._category = value

    @property
    def articles(self):
        return self._articles

    def add_article(self, article):
        if not isinstance(article, Article):
            raise ValueError("Only Article instances can be added.")
        self._articles.append(article)

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        author_article_count = {}
        for article in self._articles:
            author = article.author
            if author not in author_article_count:
                author_article_count[author] = 0
            author_article_count[author] += 1
        return [author for author, count in author_article_count.items() if count > 2]

    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        return max(cls.all_magazines, key=lambda mag: len(mag.articles))
