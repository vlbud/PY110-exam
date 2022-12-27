import conf as cf
import random as rd
from faker import Faker
import json


def model():
    return cf.model

def title():
    f = open("books.txt", "r")
    s_books = f.read()
    f.close()
    l_books = s_books.split("\n")
    return l_books[rd.randint(0,len(l_books)-1)]

def isbn():
    fake = Faker()
    Faker.seed()
    return fake.isbn13()


def autor(r):
    autor = []
    Faker.seed()
    fake = Faker()
    for _ in range(r):
        autor.append(fake.name())
    return autor[rd.randint(0,r-1)]


def book_generator(start_pk):
    pk=start_pk
    books=[]
    isb=isbn()
    aut=autor(10)
    for i in range(100):
        books.append({"model": model(),"pk":pk, "Title":title(),"year":rd.randint(2000, 2022),"pages": rd.randint(70,100),"isbn13": isb,"price": round(rd.random()*rd.randint(100,1000),2),"rating":round(rd.random()*5,2),"author": aut})
        pk+=1
    for i in books:
        yield i


def main():
    gen=book_generator(1)
    data = {}
    data['books'] = []
    for i in range(100):
        data['books'].append(next(gen))
    with open('books.txt', 'w') as outfile:
        json.dump(data, outfile)

if __name__== "__main__":
    main()

