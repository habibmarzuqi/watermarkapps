# Gunakan versi Python yang sesuai dengan kebutuhan Anda, dalam kasus ini 3.10-slim
FROM python:3.10-slim

# Tetapkan direktori kerja
WORKDIR /app

# Update dan install dependencies yang diperlukan untuk membangun mysqlclient
RUN apt-get update \
    && apt-get install -y python3-dev default-libmysqlclient-dev gcc curl pkg-config libmariadb-dev-compat \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*


# Salin file pyproject.toml dan poetry.lock (jika ada)
COPY pyproject.toml poetry.lock* /app/

# Instalasi ketergantungan menggunakan poetry
RUN curl -sSL https://install.python-poetry.org | python3 - \
    && export PATH="/root/.local/bin:$PATH" \
    && poetry config virtualenvs.create false \
    && poetry install --no-dev


# Salin sisa proyek
COPY . /app/

# Buat user non-root untuk menjalankan aplikasi
RUN useradd -m myuser
USER myuser

# Jalankan collectstatic
RUN python manage.py collectstatic --noinput

# Tetapkan perintah untuk menjalankan aplikasi menggunakan Gunicorn
CMD ["gunicorn", "watermarkapp.wsgi:application", "--bind", "0.0.0.0:8000"]
