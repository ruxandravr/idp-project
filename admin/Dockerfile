FROM python:3.6

EXPOSE 5000
ADD . /admin
WORKDIR /admin

COPY requirements.txt /admin
COPY templates /admin
COPY static /admin
RUN pip install -r requirements.txt

COPY main.py /admin
CMD python main.py
