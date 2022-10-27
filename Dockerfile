FROM python:3.8.10

COPY pickles/ ./pickles/

COPY pretrained/ ./pretrained/

COPY requirements.txt ./requirements.txt

COPY SeoulAirIndex.db ./SeoulAirIndex.db

ENV SCALEPATH="/pickles/minmaxscaler.pkl"
ENV DI_ENCODER="/pickles/division_encoder.pkl"
ENV LO_ENCODER="/pickles/location_encoder.pkl"
ENV PRETRAINED="/pretrained/lstm29.h5"

RUN pip install -r requirements.txt

COPY db_manage.py ./db_manage.py

COPY ML_API.py ./ML_API.py

COPY emart_model.py ./emart_model.py

CMD python3 ML_API.py