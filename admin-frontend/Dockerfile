FROM python:3.6

EXPOSE 5003
ADD . /admin-frontend
WORKDIR /admin-frontend

COPY requirements.txt /admin-frontend
COPY templates /admin-frontend
RUN pip install -r requirements.txt

COPY main.py /admin-frontend
CMD ["python", "main.py", "http://admin-backend:5002/"]
