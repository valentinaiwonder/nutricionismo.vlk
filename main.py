from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/faleconosco')
def contato():
    return render_template('faleconosco.html')

@app.route('/servico')
def servico():
    return render_template('servico.html')


@app.route('/calculadora')
def imc():
    return render_template('calculadora.html')


@app.route('/resultado', methods=['POST'])
def resultado():
    peso = float(request.form["peso"])
    altura = float(request.form["altura"])

    imc = round(peso / (altura**2), 2)
    return render_template('calculadora.html', resultado=imc)


if __name__ == '__main__':
    app.run(debug=True)