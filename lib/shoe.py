#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    @property
    def brand(self):
        """gets the brand"""
        return self._brand
    
    @brand.setter
    def brand(self, brand):
        """sets the brand"""
        self._brand = brand

    @property
    def size(self):
        """gets the size"""
        return self._size
    
    @size.setter
    def size(self, size):
        """sets the size"""
        if isinstance(size, int):
            self._size = size
        else:
            print("size must be an integer")
    
    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"