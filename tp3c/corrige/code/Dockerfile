FROM python:3.12-slim
RUN useradd --create-home --uid 10001 appli
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY --chown=appli:appli . .
USER appli
ENV FLASK_APP=app.py HOST=0.0.0.0 PORT=5000
EXPOSE 5000
CMD ["sh", "-c", "flask init-db && python app.py"]
