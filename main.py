from flask import Flask, render_template, request


app = Flask(__name__)
app.secret_key = "super secret key"


@app.route('/rekruto', methods = ['GET'])
def handler_get():
    name = request.args['name']
    message = request.args['message']
    print(name, message)
    return render_template('index.html', name=name, message=message)


if __name__ == "__main__":
    app.run(debug=True)
