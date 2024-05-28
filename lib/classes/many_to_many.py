class Article:
    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise TypeError("Author must be an instance of Author class")
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be an instance of the Magazine class")
        self._author = author
        self._magazine = magazine
        self._set_title(title)
        author.add_article(self)
        magazine.add_article(self)

    def _set_title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be of type str")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters and inclusive")
        self._title = title

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def magazine(self):
        return self._magazine

        
        
class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Article must be an instance of Article class")
        self._articles.append(article)

    @property
    def articles(self):
        return self._articles

    @property
    def magazines(self):
        return list({article.magazine for article in self._articles})

    @property
    def topic_areas(self):
        if not self._articles:
            return None
        return list({article.magazine.category for article in self._articles})


class Magazine:
    def __init__(self, name, category):
        self._set_name(name)
        self._set_category(category)
        self._articles = []

    def _set_name(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be of type str")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2-16 characters and inclusive")
        self._name = name

    def _set_category(self, category):
        if not isinstance(category, str):
            raise TypeError("Category must be of type str")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters")
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._set_name(value)

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._set_category(value)

    def add_article(self, article):
        if not isinstance(article, Article):
            raise TypeError("Article must be of type Article class")
        self._articles.append(article)

    @property
    def articles(self):
        return self._articles

    def contributors(self):
        return list({article.author for article in self._articles})

    def article_titles(self):
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        if not self._articles:
            return None
        author_count = {}
        for article in self._articles:
            author = article.author
            if author not in author_count:
                author_count[author] = 0
            author_count[author] += 1
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None
