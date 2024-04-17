# FROM python:3.12
# # Or any preferred Python version.
# ADD main.py .
# RUN pip install requests beautifulsoup4 python-dotenv
# CMD ["python3", “./main.py”]
# # Or enter the name of your unique directory and parameter set.


FROM python:3.10

WORKDIR /app

# ADD main.py .
# COPY requirements.txt ./
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt
# COPY . /app
COPY . .
WORKDIR /app/web
EXPOSE 5000
ENV FLASK_APP=app.py
ENV PYTHONPATH="${PYTHONPATH}:/app/modules/databases:/app/modules/cosmosdb:/app/web:/app/packages:/app/progs"
# ENTRYPOINT [ "python" ]
# CMD ["flask", "run"]
# CMD ["flask", "run", "--host", "0.0.0.0"]
CMD [“python3”, “./main.py”]
