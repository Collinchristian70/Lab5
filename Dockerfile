FROM python:3.8

WORKDIR /opt/app

COPY . . 

ADD appclass.py .

RUN pip install requests flask markupsafe

CMD [ "python", "./appclass.py" ]
