FROM python:3.6

EXPOSE 5002
ADD . /admin-backend
WORKDIR /admin-backend

COPY requirements.txt /admin-backend
RUN pip install -r requirements.txt

COPY main.py /admin-backend
CMD python main.py
