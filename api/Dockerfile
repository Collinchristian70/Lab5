FROM python:3.8

WORKDIR /opt/app

COPY . . 

ADD appclass.py .

RUN pip install requests flask markupsafe

RUN pip install redis

EXPOSE 80

CMD [ "python3", "./appclass.py" ]
