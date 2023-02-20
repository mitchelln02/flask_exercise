from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def index():
   if request.method == "POST":
      register = {
         "name" : request.form.get(name),
         "org" : request.form.get(org)
      }
      list =[]
      list.append(register)
   return render_template(registered.html, registered=registered)
return render_template(register.html)


if __name__=='__main__':
   app.run()