class Author:

    all = []

    def __init__(self,name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in Contract.all if contract.author ==self]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        roylaties_sum = 0
        for contract in Contract.all: 
            if contract.author == self:
                roylaties_sum += contract.royalties

        return roylaties_sum


class Book:

    all = []

    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in Contract.all if contract.book == self]


class Contract:

    all = []

    def __init__(self, author, book, date, royalties):
        
        if isinstance(author,Author):
            self.author = author
        else:
            raise Exception
        
        if isinstance(book,Book):
            self.book = book
        else:
            raise Exception
        
        if type(date) == str:
                self.date = date
        else:
            raise Exception
        
        if type(royalties) == int:
            self. royalties = royalties
        else:
            raise Exception

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls,date=0):
        return [contract for contract in cls.all if contract.date == date]