# Gunakan image resmi Python
FROM python:3.11.2-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Pasang dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

# Salin proyek Django ke dalam kontainer
COPY . /app
WORKDIR /app

# Jalankan server Django saat kontainer dimulai
CMD ["gunicorn", "watermarkapp.wsgi:application", "--bind", "0.0.0.0:8000"]

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    gcc \
    pkg-config
