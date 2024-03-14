FROM python:3.9

WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app/

# Debugging steps
RUN ls -la
RUN cat manage.py

# Start the Django application
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver
