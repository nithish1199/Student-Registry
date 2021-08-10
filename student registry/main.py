from flask import Flask, redirect, url_for, render_template, flash, request
import os.path
import csv
app = Flask(__name__)
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/add-student", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        student_id = request.form["std_id"]
        name = request.form["name"]
        gender = request.form["gender"]
        dob = request.form["birthday"]
        city = request.form["city"]
        state = request.form["state"]
        email = request.form["email"]
        qualification = request.form["quali"]
        stream = request.form["stream"]
        file_exist=os.path.isfile('student.csv')
        with open('student.csv', 'a+', newline='') as csvfile:
            fieldName = ["Id", "Name", "Gender", "DateOfBirth",
                         "City", "State", "Email", "Qualification", "Stream"]
            csvwriter = csv.DictWriter(csvfile, fieldnames=fieldName)
            if not file_exist:
                csvwriter.writeheader()
            csvwriter.writerow({"Id": student_id, "Name": name, "Gender": gender, "DateOfBirth": dob,
                               "City": city, "State": state, "Email": email, "Qualification": qualification, "Stream": stream})
        return render_template("add-student.html")
    else:
        return render_template("add-student.html")
@app.route("/search", methods=["POST", "GET"])
def search():
    r = 0
    state = False
    if request.method == "POST":
        sid = request.form.get("search")
        print(sid)
        with open('student.csv', 'r', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['Id'] == str(sid):
                    r = row
        state = True
        return render_template("search-student.html", row=r, state=state)
    else:
        return render_template("search-student.html", row=r, state=state)


@app.route("/display", methods=["POST", "GET"])
def display():
    rows=[]
    with open('student.csv','r',newline='') as csvfile:
        reader=csv.DictReader(csvfile)
        for row in reader:
            rows.append(row)  
    return render_template("display-student.html",rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
