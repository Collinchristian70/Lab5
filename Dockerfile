FROM python:3.8

WORKDIR /opt/app

COPY . . 

ADD appclass.py .

RUN pip install requests flask markupsafe

RUN Pip install redis

EXPOSE 5000

CMD [ "python3", "./appclass.py" ]
