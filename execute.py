import pywhatkit as pykit
from flask import Flask,render_template,request,redirect,url_for
import time

app = Flask(__name__)

@app.route('/')
def home_page():
    
    return render_template('base.html')

@app.route('/search',methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        print('Enter')
        searchid = request.form['search']
        searching = request.form['searching']
        if searchid=="1":
            pykit.playonyt(searching)
        elif searchid=="2":
            pykit.search(searching)
        elif searchid=="3":
            filename = f'{searching[:2]}_{str(time.time())[-5:]}.png'
            filepath = f'D:\Data Analytics for Business\Keras learning\Flask_pywhat_lib\static\{filename}'
            
            pykit.text_to_handwriting(searching,save_to=filepath)
    if searchid=="3":
        print("Entering image show")
        return render_template('base.html',im=filename)
    else:
        return render_template('base.html')

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='/'+filename), code=301)




if __name__ == '__main__':
    app.run(debug=True, port=7000)