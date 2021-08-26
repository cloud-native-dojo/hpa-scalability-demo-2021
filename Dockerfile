FROM python:3.8-slim
EXPOSE 5000
COPY flask-study/ /work
WORKDIR /work
RUN pip install --no-cache-dir Flask
ENV FLASK_APP=form
CMD ["flask", "run", "--host=0.0.0.0"]
