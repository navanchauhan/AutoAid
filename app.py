from flask import Flask, render_template, request
from htmx_flask import Htmx
import random

from autoAidModules.search_funcs import *

htmx = Htmx()

app = Flask(__name__)

current_task = []

htmx.init_app(app)

@app.route("/")
def hello_world():
    for _ in range(len(current_task)):
        current_task.pop()
    return render_template("index.html")

@app.route("/search", methods=["POST"])
def search():
    if request.headers.get("HX-Request"):
        print(request.form["search"])
        print(request.form["car_details"])
        make = request.form["car_details"].split(" ")[1]
        car_details = request.form["car_details"]
        for _ in range(len(current_task)):
            current_task.pop()
        current_task.append({
            "date": "Oct 7",
            "desc_plain": "Searching for ",
            "desc_bold": request.form["search"],
            "icon": "check"
        })

        pref_forum = get_preferred_forums(make)
        current_task.append({
            "date": "Oct 7",
            "desc_plain": "Searching for forums related to ",
            "desc_bold": pref_forum[0],
            "icon": "prog"
        })
        data = search_on_forum(pref_forum[0], request.form["search"], random.randint(4,8))
        current_task[-1]["icon"] = "check"
        current_task.append({
            "date": "Oct 7",
            "desc_plain": "Found the following results: ",
            "desc_bold": f"{len(data)} forum pages",
            "icon": "check"
        })
        current_task.append({   
            "date": "Oct 7",
            "desc_plain": "Using Claude to generate a tasklist",
            "desc_bold": "",
            "icon": "prog"
        })
        pred = get_tasks_from_pages(data, request.form["search"], car_details)
        current_task[-1]["icon"] = "check"
        tasks = ["Have you tried turning your car on and off?"]
        try:
            tasks = pred.split('\n\n')[0].replace("- ","").splitlines()
        except:
            print("Uh oh! Claude didn't return any results!")
        return render_template("tasks.html", to_do=tasks)
    
@app.route("/progress")
def progress():
    if request.headers.get("HX-Request"):
        print(f"current ask is", current_task)
        return render_template("progress.html", tasks=current_task)

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5123,
        debug=True,
    )