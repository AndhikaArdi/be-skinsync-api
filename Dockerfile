# Gunakan image Python
FROM python:3.10-slim

# Buat direktori kerja
WORKDIR /app

# Salin requirements dan install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file proyek ke image
COPY . .

# Buka port untuk Flask
EXPOSE 3000

# Jalankan server
CMD ["python", "recomend_api.py"]
