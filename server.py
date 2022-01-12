from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/predict_disease', methods=['GET', 'POST'])
def predict_disease():
    age = int(request.form['age'])
    alb = float(request.form['alb'])
    alp = float(request.form['alp'])
    alt = float(request.form['alt'])
    ast = float(request.form['ast'])
    bil = float(request.form['bil'])
    che = float(request.form['che'])
    chol = float(request.form['chol'])
    crea = int(request.form['crea'])
    ggt = float(request.form['ggt'])
    prot = float(request.form['prot'])
    sex = request.form['sex']
   
    response = jsonify({
        'predicted_disease': util.predict_disease(age, alb, alp, alt, ast, bil, che, chol, crea, ggt, prot, sex)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__=="__main__":
    print("Starting Python flask server to predict disease")
    util.load_saved_artifacts()
    app.run()