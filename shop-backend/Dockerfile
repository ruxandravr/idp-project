FROM python:3.6

EXPOSE 5000
ADD . /shop-backend
WORKDIR /shop-backend

COPY requirements.txt /shop-backend
RUN pip install -r requirements.txt

COPY main.py /shop-backend
CMD python main.py
