from flask import Flask,render_template,request
from day0411 import func
app = Flask(__name__)

@app.route('/test.do',methods=['GET','POST'])
def test():
    # workclass, education, occupation, race, sex = func.getDomain()
    domain = func.getDomain()
    msg = ''
    if request.method == 'POST':
        age = request.form['age']
        workclass = request.form['workclass']
        education = request.form['education']
        occupation = request.form['occupation']
        race = request.form['race']
        sex = request.form['sex']
        hoursperweek = request.form['hoursperweek']
        data = func.adult_d(age,workclass,education,occupation,race,sex,hoursperweek)
        print(data[0])
        if data[0] == 1:
            msg = "대출 가능"
        else:
            msg = '대출 불가능'
    return render_template('test.html',msg=msg,domain=domain)

if __name__=='__main__':
    app.run(debug=True)