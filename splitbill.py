from flask import Flask,render_template
app = Flask(__name__)
@app.route('/')
def list(): 
      return render_template("split.html")

if __name__ == "__main__":   
app.run()
