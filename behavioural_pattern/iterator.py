
"""
    The iterator design pattern is a behavioral design pattern that provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
"""


#!AlphabeticalOrderIterator
class AlphabeticalOrderIterator:
    def __init__(self,words,reverse:bool=False):
        self.collection = sorted(words)
        self.reverse = reverse
        self.position = len(words) - 1 if reverse==True else 0
        
    def next(self):
        value = self.collection[self.position]        
        self.position += -1 if self.reverse==True else 1
        return value
    
    
    def has_next(self):
        if self.reverse and self.position > -1:
            return True
        elif not self.reverse and self.position < len(self.collection):
            return True
        else:
            return False
        

#!WordsCollection
class WordsCollection:
    def __init__(self,collection):
        self.collection = collection
        
    
    def get_iterator(self):
        return AlphabeticalOrderIterator(self.collection,False)
    
    def get_reverse_iterator(self):
        return AlphabeticalOrderIterator(self.collection,True)


if __name__ == '__main__':
    collection = WordsCollection(['John','Alice','Michael','Carol'])
    iterator = collection.get_iterator()
    reverse_iterator = collection.get_reverse_iterator()
    
    while iterator.has_next():
        print(iterator.next())
        
    print()

    while reverse_iterator.has_next():
        print(reverse_iterator.next())
