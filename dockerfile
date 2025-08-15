# 1️⃣ Use official Python base imag
# 2️⃣ Set working directory inside containerWORKDIR /app

# 3️⃣ Copy all files to the containerCOPY . .

# 4️⃣ Install dep RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Command to run your Python fileCMD ["python", "app.py"]


FROM python:3.9

WORKDIR /app

# Copy only requirements first, to leverage Docker cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy rest of the application
COPY . .

CMD ["python", "app.py"]

