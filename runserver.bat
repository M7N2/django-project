@echo off
cd /d C:\Users\flesb\blog
call ll_env\Scripts\activate
python manage.py runserver
pause