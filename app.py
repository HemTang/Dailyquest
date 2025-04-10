import psycopg2
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    try:
        conn = psycopg2.connect(
            host="db",
            dbname="flaskdb",
            user="postgres"
        )
        return "✅ Connected to Postgres (no auth)"
    except Exception as e:
        return f"❌ Failed to connect: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
