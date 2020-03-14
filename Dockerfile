FROM python:3.7.6-slim as Base

RUN apt-get update
COPY ./requirements.txt /airbnb-ml/
WORKDIR /airbnb-ml/
RUN pip install -r requirements.txt

COPY ./src/app.py /airbnb-ml/
COPY ./src/const.py /airbnb-ml/

ENTRYPOINT ["python"]
CMD ["app.py"]