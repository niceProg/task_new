from flask import Flask,request

app = Flask(__name__)

@app.route('/BMI', methods=['POST'])
def BMI():
    tb = float(request.form.get("tb"))
    bb = float(request.form.get("bb"))

    BMI = bb / (tb/100)**2
    if BMI <= 18.5:
        hasil = "KURUS"
    elif BMI <= 25:
        hasil = "SEHAT"
    elif BMI <= 40:
        hasil = "BERLEBIHAN"
    else:
        hasil = "OBESITAS"
    data = {'Score BMI': BMI,'Tergolong': hasil}
    return data

if __name__ == '__main__':
    app.run(debug=True, port=4000)