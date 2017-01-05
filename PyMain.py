#_*_ coding:utf-8_*_
#记录日常看书的进度
import datetime

lib_path = 'lib.txt'
book_modle = '%s,%s,%s'


class lib_book:

    def __init__(self, name, progress, update_time):
        self.name = name
        self.progress = progress
        self.update_time = update_time
        self.save_format = book_modle % (name, progress, update_time)

def get_now_time():
    now = datetime.datetime.now()
    now_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return now_time

def get_books():
    f = open(lib_path, 'r')
    books = []
    for line in f.readlines():
        data = line.replace('\n', '').split(',')
        book = lib_book(data[0], data[1], data[2])
        books.append(book)
    return books

def put_book(name):
    book = lib_book(name, '0%', get_now_time())
    f = open(lib_path, 'aw')
    f.write(book.save_format + '\n')
    f.close()

def update_book(name, progress):
    books = get_books()
    clear_books()
    f = open(lib_path, 'aw')
    is_avaliable = 0
    for book in books:
        if book.name == name:
            is_avaliable = 1
            book = lib_book(name, progress, get_now_time())
        f.write(book.save_format)
    f.write('\n')
    f.close()
    return is_avaliable

def clear_books():
    clear_lib = open(lib_path, 'w')
    clear_lib.truncate()
    clear_lib.close()

print 'Welcome to Vaugh Lib u can store ur book progress and add more book'
while(1):
    code = raw_input('>')
    if code == 'put book':
        print 'Please tell me the book name:'
        book_name = raw_input('>')
        put_book(book_name)
        print 'the book《' + book_name + '》 is added'

    elif code == 'show books':
        for book in get_books():
            print book.name, book.progress, book.update_time

    elif code == 'update book':
        print 'Please tell me the book name u want to update:'
        book_name = raw_input('>')
        print 'Please tell me the progress u want to update:'
        book_progress = raw_input('>')
        if update_book(book_name, book_progress) == 0:
            print 'Sorry The book is not exist'
        else:
            print 'The progress is updated'

    elif code == 'remove books':
        print 'R u sure u want to remove all books? y/n:'
        answer = raw_input('>')
        if answer == 'y' or answer == 'Y':
            clear_books()
            print 'u have clear all books'

    elif code == 'help':
        print 'u can type commands like these:'
        print 'put book: u can add new book'
        print 'show books: u can get all books'
        print 'update book: u can type book name and update its progress'
        print 'remove books: u can clear all books'

    else:
        print 'I beg ur pardon?'