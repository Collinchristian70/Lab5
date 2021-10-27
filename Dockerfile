FROM python:3.8

ADD appclass.py .

RUN pip install requests flask

CMD [ "python", "./appclass.py" ]
