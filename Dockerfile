FROM python:3.5.2

WORKDIR /extracredit

ADD . /extracredit

EXPOSE 7777

RUN pip install -r /extracredit/requirements.txt

CMD ["python", "/extracredit/app.py"]