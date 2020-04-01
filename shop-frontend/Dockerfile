FROM python:3.6

EXPOSE 5001
ADD . /shop-frontend
WORKDIR /shop-frontend

COPY requirements.txt /shop-frontend
COPY templates /shop-frontend
COPY static /shop-frontend
RUN pip install -r requirements.txt

COPY main.py /shop-frontend
CMD ["python", "main.py", "http://shop-backend:5000/"]
