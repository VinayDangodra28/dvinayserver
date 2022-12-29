from __future__ import with_statement
from __future__ import absolute_import
from flask import Flask, render_template, request
from datetime import datetime
from flask_mail import Mail,Message
import json
from datetime import date
import pandas as pd
import webbrowser as wb
from io import open

app = Flask(__name__)
app.config[u'MAIL_SERVER'] = u'smtp.gmail.com'
app.config[u'MAIL_PORT'] = 465
app.config[u'MAIL_USERNAME'] = u"vinaydangodra28@gmail.com"
app.config[u'MAIL_PASSWORD'] = u'neigzvqmcabepapi'
app.config[u'MAIL_USE_TLS'] = False
app.config[u'MAIL_USE_SSL'] = True

mail = Mail(app)

def doEntry(name, email, message):
    with open(u'contacts.json') as json_file:
            data = json.load(json_file)
            sno = data[u'sno']
            names = data[u'name']
            emails = data[u'email']
            messages = data[u'message']
            newsno = sno[-1] +1
            sno.append(newsno)
            names.append(name)
            emails.append(email)
            messages.append(message)

            newdict = {
                u"sno":sno,
                u"name":names,
                u"email":emails,
                u"message":messages,
            }
            json_object = json.dumps(newdict, indent = 4)
            with open(u"contacts.json", u"w") as json_file_final:
                json_file_final.write(json_object)
                print(json_file_final)
    








@app.route(u"/", methods=[u'GET', u'POST'])
def hello_world():
    if request.method == u'POST':
        name = request.form[u'name']
        email = request.form[u'email']
        msg = request.form[u'message']
        doEntry(name, email, msg)
        subject = u"message from dvinay"
        message = Message(subject, sender=u"vinaydangodra841@gmail.com", recipients=[u"vinaydangodra28@gmail.com"])
        message.body = f"Someone filled your contact form\nName: {name}\nEmail: {email}\nMessage: {msg}"
        mail.send(message)
    return render_template(u'index.html', name=u"Vinay Dangodra")



@app.route(u"/database")
def table():
    with open(u'contacts.json') as json_file:
        data_dic = json.load(json_file)
        columns = [u'sno', u'name', u'email', u'message']
        index = data_dic[u'sno']
        df = pd.DataFrame(data_dic, columns=columns, index=index)
        table = df.to_html(index=False)
        return render_template(u'formsubmissions.html', table=table) 

@app.route(u"/posts")
def posts():
    return render_template(u'posts.html')


@app.route(u"/admin")
def admin():
    password=u"@All8652410990"
    return render_template(u'admin.html', password=password)





if __name__ == u'__main__':
    
    wb.open_new(u'http://localhost:9990')
    app.run(port=u"9990")
     