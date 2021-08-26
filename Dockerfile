FROM python:3.8-slim
EXPOSE 5000
COPY flask-study/ /work
WORKDIR /work/flask-study/
RUN pip install Flask
ENV FLASK_APP=form
CMD ["flask", "run"]
