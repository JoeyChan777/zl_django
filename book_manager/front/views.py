from django.shortcuts import render, redirect, reverse
from django.db import connection


def get_cursor():
    return connection.cursor()


def index(request):
    cursor = get_cursor()
    cursor.execute('select * from books')
    books = cursor.fetchall()
    return render(request, 'index.html', {'books': books})


def add_book(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        cursor = get_cursor()
        cursor.execute('insert into books values(null,"{}","{}")'.format(name, author))
        return redirect(reverse('index'))
    else:
        return render(request, 'add_book.html')


def book_detail(request, book_id):
    cursor = get_cursor()
    cursor.execute('select * from books where id={}'.format(book_id))
    book = cursor.fetchone()
    return render(request, 'book_detail.html', {'book': book})


def delete_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute('delete from books where id={}'.format(book_id))
        return redirect(reverse('index'))
    else:
        raise RuntimeError('删除图书的method错误！')


def edit_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        cursor = get_cursor()
        cursor.execute('select * from books where id={}'.format(book_id))
        book = cursor.fetchone()
        return render(request, 'edit_book.html', {'book': book})
    else:
        raise RuntimeError('编辑图书的method错误！')


def save_book(request, book_id):
    if request.method == 'POST':
        name = request.POST.get('name')
        author = request.POST.get('author')
        cursor = get_cursor()
        cursor.execute("update books set name='{}',author='{}' where id={}".format(name, author, book_id))
        return redirect(reverse('book_detail', kwargs={'book_id': book_id}))
    else:
        raise RuntimeError('保存的method错误！')