from flask import Flask,render_template,request
from day0411 import func
app = Flask(__name__)

@app.route('/test.do',methods=['GET','POST'])
def test():
    # age = ''
    # workclass = ''
    # education = ''
    # occupation = ''
    # race = ''
    # sex = ''
    # hoursperweek = ''
    # data = ''
    msg = ''
    if request.method == 'POST':
        age = request.form['age']
        workclass = request.form['workclass']
        education = request.form['education']
        occupation = request.form['occupation']
        race = request.form['age']
        sex = request.form['sex']
        hoursperweek = request.form['hoursperweek']
        income = request.form['income']
        data = func.adult_d(age,workclass,education,occupation,race,sex,hoursperweek,income)
        print(data)
        if data == '1':
            msg = "대출 가능"
        else:
            msg = '대출 불가능'
    return render_template('test.html',msg=msg)


if __name__=='__main__':
    app.run(debug=True)