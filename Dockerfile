FROM python:3.12-slim AS builder

ARG VERSION

LABEL org.label-schema.version=$VERSION

COPY ./requirements.txt /webapp/requirements.txt


RUN pip install --no-cache-dir --target=/webapp/dependencies -r /webapp/requirements.txt



FROM python:3.12-slim

WORKDIR /webapp

COPY --from=builder /webapp/dependencies /usr/local/lib/python3.12/site-packages 

COPY webapp/app.py /webapp

EXPOSE 5001

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]