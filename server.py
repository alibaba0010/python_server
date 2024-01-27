# python3 -m http.server 5000 
from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__) # main file
import csv
# app.add_url_rule('/favicon.ico',
                #  redirect_to=url_for('static', filename='favicon.ico'))
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/submit_form", methods=["POST","GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict() # transmit form data to dict == object(js)
        print(data)
        save_data(data)
    return redirect("/thank-you.html")

def save_data(data):
    with open("database.csv", newline="",mode="a") as database_csv:
        name = data["name"]
        email = data["email"]
        message = data["message"]
        # file = database_csv.write(f"\n{name}, {email}, {message}")
        file = csv.writer(database_csv, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        writer = file.writerow([name, email, message])