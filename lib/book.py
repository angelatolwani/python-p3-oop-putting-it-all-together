#!/usr/bin/env python3

class Book:
    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count

    def get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title

    title = property(get_title, set_title)

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            # raise TypeError("page_count must be an integer\n")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")