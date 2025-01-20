import os
from sunau import Au_read

import django
from django.shortcuts import aget_object_or_404

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_lesson.settings")
django.setup()

from orm_test.models import User, Lesson, Homework

'''
user = User.objects.create(username="Magan", age=22, email= "magan@gmail.com", logiks=9999, note="Sigma tutor", role="teacher")

user = User.objects.create(username="krustalek", age=71, email="krustalek@gmail.com", logiks=154, note="Meme guy", role="student")
user = User.objects.create(username="dimo_moldavan", age=17, email="dimon@gmail.com", logiks=177, note="Nice bro", role="student")
user = User.objects.create(username="Kaef", age=17, email="kaefoviy@gmail.com", logiks=163, note="Silent student", role="student")
user = User.objects.create(username="Ramzes(._.Бабенко._.)", age=17, email="bobenko@gmail.com", logiks=189, note="Giga coder", role="student")
user = User.objects.create(username="Vitalliy", age=22, email="vitalya@gmail.com", logiks=178, note="Vitalya", role="student")'''


'''user = User.objects.all()
print(user)'''

#user = User.objects.get(username="Magan")

#Lesson.objects.create(title="DjangoOrm lesson 2", description="Studying deeper aspects of Django", author=user)
#Lesson.objects.create(title="DjangoOrm lesson 1", description="Start of learning Django", author=user)
#Lesson.objects.create(title="SQL lesson 1", description="Studying SQL", author=user)'''

#lesson = Lesson.objects.filter(author=user).all()


ramzes = User.objects.get(username="Ramzes(._.Бабенко._.)")
dimo = User.objects.get(username="dimo_moldavan")
vitaliy = User.objects.get(username="Vitalliy")
krustalek = User.objects.get(username="krustalek")

lesson_1 = Lesson.objects.get(title="DjangoOrm lesson 1")
lesson_2 = Lesson.objects.get(title="DjangoOrm lesson 2")
sql_lesson = Lesson.objects.get(title="SQL lesson 1")

'''Homework.objects.create(user=ramzes, lesson=lesson_2, body="Well done homework with interesting features")
Homework.objects.create(user=ramzes, lesson=lesson_1, body="Nice start of unique project")
Homework.objects.create(user=vitaliy, lesson=lesson_1, body="Big features of a big code")
Homework.objects.create(user=dimo, lesson=lesson_1, body="Great realization of all the methods we learned")
Homework.objects.create(user=dimo, lesson=lesson_1, body="Amazing and custom database")
Homework.objects.create(user=dimo, lesson=sql_lesson, body="Good understanding of each method")
Homework.objects.create(user=krustalek, lesson=lesson_2, body="Good enough hm for the one who skipped previous lesson")
Homework.objects.create(user=krustalek, lesson=sql_lesson, body="Despite a small copyright, code is fine")'''


'''print(post)
print(post.created_at)
print(post.updated_at)

print(post.author.name)
print(post.author.email)

post.description = "KKKKK"
post.save()'''


