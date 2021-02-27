FROM python:3.6


ADD . /jcapp

WORKDIR /jcapp

RUN pip install flask gunicorn requests
# RUN pip install -U appdynamics
RUN pip install -U flask-cors
RUN chmod +x startup.sh
ENV FLASK_APP manage.py

EXPOSE 8000
ENTRYPOINT [ "/jcapp/startup.sh" ]


