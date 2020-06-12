from flask import Flask, render_template, url_for, request,redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/<string:page>')
def pages(page):
    return render_template(page)

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try: 
            data = request.form.to_dict()
            # save_info_textfile(data)
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return 'Did not save to database'
    else:
        return "something went wrong"


def write_to_csv(data):
    with open('database.csv',newline='',mode='a')as csvfile:
        fullname=data["Fname"]
        email = data["Email"]
        phonenumber =data["Phonenumber"]
        message = data["Message"]
        csv_writer = csv.writer(csvfile, delimiter=',',quotechar='|', lineterminator='\n', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([fullname,email,phonenumber,message])


def save_info_textfile(data):
    with open('database.txt', mode='a') as database:
        fullname=data["Fname"]
        email = data["Email"]
        phonenumber =data["Phonenumber"]
        message = data["Message"]
        database.write(f'\n{fullname}, {email}, {phonenumber}, {message}')
        

   



