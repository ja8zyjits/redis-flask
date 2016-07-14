from flask import Flask, request, render_template
from redis  import Redis

app = Flask(__name__)
db = Redis('localhost')

@app.route("/")
def hello():
    return render_template("sum_finder.html")

@app.route("/sum")
def view_sum():
    number = int(request.values.get('number'))
    value = find_sum(number)
    return render_template("sum_finder.html", sum_value=value)



def find_sum(number):
    if not db.exists(number):
        return get_sum(number)
    else:
        return db.get(number)

def get_sum(number):
    value = sum(xrange(10**9)) + number
    db.set(number,value)
    return value


if __name__ == "__main__":
    app.run(port=8000, debug=True)
