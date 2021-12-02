FROM python:3.8

WORKDIR /opt/app

COPY . . 

ADD testerapp.py .

RUN pip install requests flask markupsafe

RUN pip install redis

EXPOSE 5000

CMD [ "python3", "./testerapp.py" ]
