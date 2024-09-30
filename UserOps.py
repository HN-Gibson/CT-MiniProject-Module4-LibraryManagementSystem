class User:
    def __init__(self,name,id):
        self.__name = name
        self.__id = id
        self.__borrowed_books = []
    
    def get_name(self):
        return self.__name
    def get_id(self):
        return self.__id
    def get_borrowed_books(self):
        return self.__borrowed_books
