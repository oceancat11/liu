from flask import Flask,request,render_template
import replicate
import os
import time

app=Flask(__name__)
os.environ["REPLICATE_API_TOKEN"]="787f515cb0624813736c11e7fefec66473394f02"

r=""
first_time=1
@app.route("/",methods=["GET","POST"])
def index():
  return(render_template("index.html"))

@app.route("/main",methods=["GET","POST"])
def main():
  r=request.form.get("r")
  return(render_template("main.html",r=r))

@app.route("/image_gpt",methods=["GET","POST"])
def image_gpt():
  return(render_template("image_gpt.html"))

@app.route("/end",methods=["GET","POST"])
def image_result():
q=request.form.get("q")  
r = replicate.run(
    "stability-ai/stable-diffusion:db21e45d3f7023abc2a46ee38a23973f6dce16bb082a930b0c49861f96d1e5bf",
    input={
        "prompt": q,
  }
)
return(render_template("image_gpt.html",r=r[0]))

@app.route("/end",methods=["GET","POST"])
def end():
  first_time=1
  return(render_template("end.html"))

  if __name__=="__main__":
         app.run()
