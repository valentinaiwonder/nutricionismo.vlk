from flask import Flask, render_template, request

app = Flask(__name__) 

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/faleconosco')
def contato():
    return render_template('faleconosco.html')

@app.route('/serviço')
def servico():
    return reder_template('servico.html')


@app.route('/calculadora')
def imc():
    return reder_template('calculadora.html')


@app.route('/resultado', methods=['POST'])
def calcular_imc():
    peso = float(input("Digite seu peso em kg: "))
    altura = float(input("Digite sua altura em metros: "))
    imc = peso / (altura ** 2)
    print("Seu IMC é: {:.2f}".format(imc))


if __name__ == '__main__':
    app.run(debug=True)