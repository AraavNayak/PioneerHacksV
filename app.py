import os
import uuid
from flask import Flask, flash, request, redirect, render_template
import matplotlib.pyplot as plt

UPLOAD_FOLDER = 'files'

# x axis values  
x = [1,2,3]  
# corresponding y axis values  
y = [2,4,1]  
    
# plotting the points   
plt.plot(x, y)  
    
# naming the x axis  
plt.xlabel('x - axis')  
# naming the y axis  
plt.ylabel('y - axis')  
    
# giving a title to my graph  
plt.title('My first graph!')  
    
# function to show the plot  
plt.show()  

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/save-record', methods=['POST'])
def save_record():
    # check if the post request has the file part
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    file_name = str(uuid.uuid4()) + ".mp3"
    full_file_name = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
    file.save(full_file_name)
    return '<h1>Success</h1>'


if __name__ == '__main__':
    app.run()