from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/add", methods=["GET", "POST"])
def add_task():
    if request.method == "POST":
        task = request.form.get("task")
        if task:
            tasks.append(task)
        return redirect("/tasks")
    return render_template("add.html")

@app.route("/tasks")
def view_tasks():
    return render_template("tasks.html", tasks=tasks)

if __name__ == "__main__":
    app.run()
