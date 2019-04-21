from django.shortcuts import render
from django.http import HttpResponse
from .models import Books,Author
from datetime import datetime
from django.utils.timezone import make_aware
from django.db.models import Q,F



def index1(request):
    # 查询Author,Books所有对象
    books = Books.objects.all()
    authors = Author.objects.all()
    for book in books:
        print(book)
    print('*'*30)
    for author in authors:
        print(author)
    return HttpResponse('success')


def index2(request):
    # 查询Books中id=2的书，Author中name=‘月关’的作者
    book = Books.objects.get(pk=2)
    author = Author.objects.get(name='月关')
    print(book)
    print(author)
    return HttpResponse('success')


def index3(request):
    # 分别查询Books,Author所有对象的数量
    books = Books.objects.all().count()
    authors = Author.objects.all().count()
    print(books,authors)
    return HttpResponse('success')


def index4(request):
    # 分别查询书名含有‘明朝’，‘大’的图书
    books_1 = Books.objects.filter(title__contains='明朝')
    books_2 = Books.objects.filter(title__contains='大')
    for book in books_1:
        print(book)
    print('-'*30)
    for book in books_2:
        print(book)
    return HttpResponse('success')


def index5(request):
    # 查询书名以‘斗’开头的图书，查询出版社以‘社’结尾的图书
    books_1 = Books.objects.filter(title__startswith='斗')
    books_2 = Books.objects.filter(publisher__endswith='社')
    for book in books_1:
        print(book)
    print('-'*30)
    for book in books_2:
        print(book)
    return HttpResponse('success')


def index6(request):
    # 查询书名id为2或8或10的图书
    books = Books.objects.filter(id__in=[2, 8, 10])
    for book in books:
        print(book)
    return HttpResponse('success')


def index7(request):
    # 查询书名id 2-5的图书
    books = Books.objects.filter(id__in=[x for x in range(2, 6)])
    for book in books:
        print(book)
    return HttpResponse('success')


def index8(request):
    # 查询出版日期为2012年的图书
    # books = Books.objects.filter(publish_day__gte=datetime(year=2012,month=1,day=1)).filter(publish_day__lte=datetime(year=2012,month=12,day=31))
    start_date = make_aware(datetime(year=2012, month=1, day=1))
    end_date = make_aware(datetime(year=2012, month=12, day=31))
    books = Books.objects.filter(publish_day__range=(start_date, end_date))
    for book in books:
        print(book)
    return HttpResponse('success')


def index9(request):
    # 查询出版日期大于等于2013-09-01的图书（date需要导包）
    books = Books.objects.filter(publish_day__gte=datetime(year=2013,month=9,day=1))
    for book in books:
        print(book)
    return HttpResponse('success')


def index10(request):
    # 查询出版日期大于2007年，id小于5的图书（Q对象需要导入）
    books = Books.objects.filter(Q(publish_day__gt=datetime(year=2007,month=12,day=31)) & Q(id__lt=5))
    for book in books:
        print(book)
    return HttpResponse('success')


def index11(request):
    # 查询作者‘烽火戏诸侯’的所有书
    books = Books.objects.filter(author__name='烽火戏诸侯')
    for book in books:
        print(book)
    return HttpResponse('success')


def index12(request):
    # 查询书名为‘回到明朝当王爷’的作者
    book = Books.objects.get(title='回到明朝当王爷')
    author = Author.objects.get(id=book.author_id)
    print(author)
    return HttpResponse('success')


def index13(request):
    # 添加新的作者（name=‘南派三叔’，true_name=‘徐磊’,birth_year=‘1982’）
    Author.objects.create(name='南派三叔',true_name='徐磊',birth_year='1982')
    return HttpResponse('success')


def index14(request):
    # 添加新的图书（title='大主宰',publish_day='2013-07-01',publisher='起点中文网'）作者天蚕土豆
    # book = Books()
    # book.title = '大主宰'
    # book.publish_day = '2013-07-01'
    # book.publisher = '起点中文网'
    # book.author = Author.objects.get(name='天蚕土豆')
    # book.save()
    Books.objects.create(title='大主宰',publish_day='2013-07-01',publisher='起点中文网',author=Author.objects.get(name='天蚕土豆'))
    return HttpResponse('success')


def index15(request):
    # 添加新的图书（title='盗墓笔记',publish_day='2007-06-04',publisher='中国友谊'）作者南派三叔
    Books.objects.create(title='盗墓笔记',publish_day='2007-06-04',publisher='中国友谊',author=Author.objects.get(name='南派三叔'))
    return HttpResponse('success')


def index16(request):
    # 将图书龙王传说，修改为绝世唐门(title='绝世唐门',publish_day='2012-11-13')
    book = Books.objects.get(title='龙王传说')
    book.title = '绝世唐门'
    book.publish_day = '2012-11-13'
    # 千万不要忘记了save
    book.save()
    return HttpResponse('success')


def index17(request):
    # 删除书名为'陈二狗的妖孽人生'的图书
    book = Books.objects.get(title='陈二狗的妖孽人生')
    book.delete()
    book.save()
    return HttpResponse('success')