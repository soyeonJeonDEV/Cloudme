FROM python:3.8

RUN pip3 install django
RUN pip3 install pymysql==1.0.2
RUN pip install django-redis
RUN pip install requests
RUN pip install bs4
RUN pip install xmltodict

 
WORKDIR /usr/src/app

RUN mkdir -p /usr/src/app
RUN cd /usr/src/app

COPY . .

WORKDIR ./django

CMD ["python3", "manage.py", "runserver", "0:8000"]

EXPOSE 8000
