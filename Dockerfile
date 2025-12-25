FROM python:3.13-slim

WORKDIR /app

# Install deps
COPY api/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy only the API code
COPY api ./api

EXPOSE 8000

CMD ["gunicorn", "-b", "0.0.0.0:8000", "api.app:app"]
