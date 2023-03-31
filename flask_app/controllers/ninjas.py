from flask import render_template,redirect,request,session,flash
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/dojos/ninjas')
def ninjas():
    dojos = Dojo.get_all()
    return render_template("ninja.html",all_dojos = dojos)


@app.route('/create/ninjas',methods=['POST'])
def create_ninja():
    Ninja.save(request.form)
    return redirect('/')



if __name__=="__main__":
    app.run(debug=True)

