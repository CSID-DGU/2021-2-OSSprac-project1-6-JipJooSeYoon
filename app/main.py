from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def student():
   main = dict()
   main['Name'] = ""
   main['StudentNumber'] = ""
   main['Gender'] =""
   main['Major'] = ""
   return render_template('main.html', main = main)

@app.route('/detail', methods = ['POST', 'GET'])
def detail():
   if request.method == 'POST':
      detail = dict()
      detail['Name'] = request.form.get('Name')
      detail['StudentNumber'] = request.form.get('StudentNumber')
      detail['Gender'] = request.form.get('Gender')
      detail['Major'] = request.form.get('Major')
      return render_template("detail.html",detail = detail)

@app.route('/main', methods = ['POST', 'GET'])
def back():
   if request.method == 'POST':
      main = dict()
      main['Name'] = request.form.get('Name')
      main['StudentNumber'] = request.form.get('StudentNumber')
      main['Gender'] = request.form.get('Gender')
      main['Major'] = request.form.get('Major')
      return render_template('main.html', main = main)

@app.route('/result', methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['StudentNumber'] = request.form.get('StudentNumber')
      result['Gender'] = request.form.get('Gender')
      result['Major'] = request.form.get('Major')
      return render_template("result.html",result = result)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
