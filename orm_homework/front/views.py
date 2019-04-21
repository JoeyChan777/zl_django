from django.shortcuts import render
from django.http import HttpResponse
from .models import Student,Teacher,Score,Course
from django.db.models import Avg,Sum,Count,Q,F,Max,Min
from django.db import connection


def index1(request):
    # 查询平均成绩大于60分的同学的id和平均成绩
    # 提取出的QuerySet中的数据类型不是模型，而是在values方法中指定的字段和值形成的字典
    students = Student.objects.annotate(avg_score=Avg('score__number')).filter(avg_score__gt=60).values('id', 'name',
                                                                                                        'avg_score')
    for student in students:
        print('{}/{}/{}'.format(student['name'], student['id'], student['avg_score']))
    print(connection.queries)
    return HttpResponse('success')


def index2(request):
    # 查询所有同学的id、姓名、选课的数量、总成绩
    students = Student.objects.annotate(course_count=Count('score__student_id')).annotate(
        sum_score=Sum('score__number'))
    for student in students:
        print('{}/{}/{}/{}'.format(student.id, student.name, student.course_count, student.sum_score))
    return HttpResponse('success')


def index3(request):
    # 查询姓“李”的老师的个数
    teachers = Teacher.objects.filter(name__startswith='李').count()
    print(teachers)
    print(connection.queries)
    return HttpResponse('success')


def index4(request):
    # 查询没学过“李老师”课的同学的id、姓名
    students = Student.objects.exclude(score__course__teacher__name='李老师').values('id', 'name')
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse('success')


def index5(request):
    # 查询学过课程id为1和2的所有同学的id、姓名
    students = Student.objects.filter(score__course_id__in=[1, 2]).values('id', 'name').distinct()
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse('success')


def index6(request):
    # 查询学过“黄老师”所教的“所有课”的同学的id、姓名
    # 1. 首先先找到每一位学生学习的黄老师课程的数量；A
    # 2. 在课程的表中找到黄老师教的课程的数量；B
    # 3. 判断A是否等于B，如果相等，那么意味着这位学生学习了黄老师教的
    # 所有课程，如果不相等，那么意味着这位学生没有学完黄老师教的所有课程
    students = Student.objects.annotate(
        nums=Count('score__course_id', filter=Q(score__course__teacher__name='黄老师'))).filter(
        nums=Course.objects.filter(teacher__name='黄老师').count()).values('id', 'name')
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse('success')


def index7(request):
    # 查询所有课程成绩小于60分的同学的id和姓名
    # 每个同学所学的课程总数
    #students = Student.objects.aggregate(course_num=Count('score__student_id'))
    #students = Student.objects.annotate(nums=Count('score__number',filter=Q(score__number__lt=60))).filter(nums=Student.objects.aggregate(course_num=Count('score__student_id'))).values('id','name')
    # for student in students:
    #     print(student)
    students = Student.objects.exclude(score__number__gt=60)
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse('success')


def index8(request):
    # 查询没有学全所有课的同学的id、姓名
    students = Student.objects.annotate(course_num=Count('score__course')).exclude(course_num=Course.objects.all().count()).values('id','name')
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse('success')


def index9(request):
    # 查询所有学生的姓名、平均分，并且按照平均分从高到低排序
    students = Student.objects.annotate(avg_score=Avg('score__number')).order_by('-avg_score').values('name','avg_score')
    for student in students:
        print(student)
    print(connection.queries)
    return HttpResponse('success')


def index10(request):
    # 查询各科成绩的最高和最低分，以如下形式显示：课程ID，课程名称，最高分，最低分
    courses = Course.objects.annotate(max=Max('score__number'),min=Min('score__number')).values('id','name','max','min')
    for course in courses:
        print(course)
    print(connection.queries)
    return HttpResponse('success')


def index11(request):
    # 查询每门课程的平均成绩，按照平均成绩进行排序
    courses = Course.objects.annotate(avg=Avg('score__number')).order_by('-avg').values('id','name','avg')
    for course in courses:
        print(course)
    print(connection.queries)
    return HttpResponse('success')


def index12(request):
    # 统计总共有多少女生，多少男生
    
    return HttpResponse('success')


def index13(request):
    # 将“黄老师”的每一门课程都在原来的基础之上加5分
    rows = Score.objects.filter(course__teacher__name='黄老师').update(number=F('number')+5)
    print(rows)
    print(connection.queries)
    return HttpResponse('success')


def index14(request):
    # 查询两门以上不及格的同学的id、姓名、以及不及格课程数
    return HttpResponse('success')


def index15(request):
    # 查询每门课的选课人数
    return HttpResponse('success')
