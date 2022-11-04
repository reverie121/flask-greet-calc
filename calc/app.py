from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from operations import add, sub, mult, div

app = Flask(__name__)

app.config['SECRET_KEY'] = 'do*not*tell'
debug = DebugToolbarExtension(app)

math_operations = {'add': add, 'sub': sub, 'mult': mult, 'div': div}

def call_operation(operation):
    """Uses the math_operaitons dict to call the appropriate operation function using query string variables."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return str(math_operations[operation](a,b))

@app.route('/')
def index():
    return render_template('calc.html')

@app.route('/<operation>')
@app.route('/math/<operation>')
def do_math(operation):
    return call_operation(operation)

@app.route('/calc_submit')
def calc_submit():
    a = int(request.args["a"])
    b = int(request.args["b"])
    operator = request.args["operator"]
    expressions =  {'add': 'plus', 'sub': 'minus', 'mult': 'multiplied by', 'div': 'divided by'}
    return render_template('answer.html', a = a, b = b, operation = expressions[operator], answer = round(math_operations[operator](a,b), 2))