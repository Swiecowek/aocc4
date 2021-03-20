from flask import Flask, render_template 

app=Flask(__name__)

@app.route("/")
def home():
  data = [
    ('red', 25),
    ('blue', 25),
    ('yellow', 25),
    ('subeer', 25),
   
  ]

  labels = [row[0] for row in data]
  values  = [row[1] for row in data]
  return render_template("graph.html", labels=labels, values=values)

