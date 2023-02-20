from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('home.html')
    
@app.route('/calculate', methods=['GET'])
def calculate():
    number = request.args.get('number')

    if len(request.args)==0:
        return render_template('calculate.html')
    number = request.args['number']
    try:
        if int(number) % 2 == 0:
            result='even'
        elif int(number) % 2 != 0:
            result='odd'
    except:
        result='not an integer!'
    return render_template('calculate.html', number=number, name=result)

if __name__ == "__main__":
    app.run()