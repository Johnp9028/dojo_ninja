from flask import render_template, redirect, request
from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja




@app.route('/')
def index():
    return redirect('/dojos')



@app.route('/dojos')
def dojos():
    dojos = Dojo.get_all()
    return render_template("index.html",all_dojos = dojos)



@app.route('/create/dojo',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')


@app.route('/dojos/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    Dojo.delete(data)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def copy(id):
    data= {
        "id":id
    }
    return render_template("dojo.html", dojo=Dojo.get_one(data))