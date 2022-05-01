FROM python:3.8

RUN apt update
RUN apt install gettext -y

RUN pip3 install django==3.1.3
RUN pip3 install pymysql==1.0.2
RUN pip install django-redis
RUN pip install xmltodict
RUN pip install requests
RUN pip install bs4

 
WORKDIR /usr/src/app

RUN mkdir -p /usr/src/app
RUN cd /usr/src/app

COPY . .

WORKDIR ./django

CMD ["python3", "manage.py", "runserver", "0:8000"]

EXPOSE 8000
