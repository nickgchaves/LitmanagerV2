class Book:
    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author

    @property
    def author(self) -> str:
        return self._author

    @author.setter
    def author(self, author_string: str) -> None:
        if not author_string:
            raise ValueError("Author cannot be empty")
        self._author = author_string

    @property
    def title(self) -> str:
        return self._title

    @title.setter
    def title(self, title_string: str) -> None:
        if not title_string:
            raise ValueError("Title cannot be empty")
        self._title = title_string