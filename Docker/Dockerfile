FROM python:3.8
WORKDIR /app
COPY . /app
RUN python -m pip install -r /app/requirements.txt
EXPOSE 5000
CMD ["python","/app/app.py"]
