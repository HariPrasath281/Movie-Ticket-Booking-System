from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
from config import DB_HOST, DB_USER, DB_PASSWORD, DB_NAME

app = Flask(__name__)
app.secret_key = "supersecretkey"


# -----------------------------
# Database Connection
# -----------------------------
def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )


# -----------------------------
# Home Route
# -----------------------------
@app.route("/")
def home():
    return redirect(url_for("login"))


# -----------------------------
# Register Route
# -----------------------------
@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)"
        cursor.execute(query, (username, email, password))

        conn.commit()
        conn.close()

        return redirect(url_for("login"))

    return render_template("register.html")


# -----------------------------
# Login Route
# -----------------------------
@app.route("/login", methods=["GET", "POST"])
def login():

    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username=%s AND password=%s"
        cursor.execute(query, (username, password))

        user = cursor.fetchone()
        conn.close()

        if user:
            session["username"] = username
            return redirect(url_for("movies"))
        else:
            error = "Invalid username or password"

    return render_template("login.html", error=error)

# -----------------------------
# Logout Route
# -----------------------------

@app.route("/logout")
def logout():
    session.pop("username", None)
    session.pop("admin", None)
    return redirect(url_for("login"))

# -----------------------------
# Movies Page
# -----------------------------
@app.route("/movies")
def movies():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template("movies.html")


# -----------------------------
# Admin Page
# -----------------------------
@app.route("/admin")
def admin():

    if "admin" not in session:
        return redirect(url_for("admin_login"))

    return render_template("admin.html")
# -----------------------------
# Admin Login Page
# -----------------------------
@app.route("/admin-login", methods=["GET", "POST"])
def admin_login():

    error = None

    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # simple admin credentials
        if username == "admin" and password == "admin123":
            session["admin"] = True
            return redirect(url_for("admin"))
        else:
            error = "Invalid admin credentials"

    return render_template("admin_login.html", error=error)

# -----------------------------
# Run Server
# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)