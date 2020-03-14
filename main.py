import glob
import os
from flask import Flask, render_template
server = Flask("IceRain")

@server.route("/")
def index():
  ds = glob.glob("gamer/*")
  ds = [d.split("/")[-1] for d in ds]
  return render_template("index.html", dirs=ds)

@server.route("/gamer/<c>")
def gamer(c):
  fs = glob.glob("gamer/" + c + "/*.txt")
  contents = []
  for i,fn in enumerate(fs):
    name = os.path.split(fn)[-1].replace(".txt", "")
    f = open(fn)
    gamer = f.read()
    f.close()
    contents.append((name,gamer,i))
  return render_template("gamer.html", cs=contents)
