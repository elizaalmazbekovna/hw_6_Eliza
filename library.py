import os
import re

class Library:
    __secret_key=os.environ.get('SECRET_LIB_KEY')
    __books_list=["Martin Iden", "Anna Karenina","Voina i Mir","Molniya"]


    @classmethod
    def get_books(cls):
        if os.environ.get('secret_key') is None:
            print("Forbidden action")
        else:
            print(cls.__books_list)

    @classmethod
    def give_book(cls):
        find_book=input("Enter your reading book: ")
        if find_book in cls.__books_list:
            cls.__books_list.remove(find_book)
            print(cls.__books_list)

        else:
            print(f"Can't give this book {find_book} to you")
            return False

    @classmethod
    def check_student_key(cls,pub_key):
        cls.pub_key=pub_key
        STUDENT_PUB_KEY=r"[\d\w]{4}-[\d\w]{4}-[\d\w]{6}"

        try:
            cls.pub_key=STUDENT_PUB_KEY
            print("Public Key Success")
            return True
        except:
            print("Wrong Public Key")
            return False






Library.check_student_key('af12-sdsffv12-zhjjkbhj1a')



