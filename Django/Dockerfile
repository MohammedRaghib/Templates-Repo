FROM python:3.13-slim

WORKDIR /app

# Install MS SQL
RUN apt-get update && apt-get install -y \
    curl \
    gnupg2 \
    gcc \
    g++ \
    unixodbc-dev \
    && curl -fsSL https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor -o /usr/share/keyrings/microsoft-prod.gpg \
    && curl https://packages.microsoft.com/config/debian/12/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && sed -i 's|deb \[|deb [signed-by=/usr/share/keyrings/microsoft-prod.gpg |' /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql18 mssql-tools18 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Change ports if necessary
EXPOSE 9010

CMD ["python", "manage.py", "runserver", "0.0.0.0:9010"]