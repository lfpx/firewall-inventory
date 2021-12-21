from application import app, db
from application.models import Hosts, Rules
from application.forms import HostForm
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    all_hosts = Hosts.query.all()
    return render_template("index.html", title="Home", all_hosts=all_hosts)

@app.route('/create-host', methods=['GET','POST'])
def create_host():
    form = HostForm()

    if request.method=='POST':
        new_host = Hosts(host_name=form.host_name.data, host_ip=form.host_ip.data)
        db.session.add(new_host)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("create_host.html", title="Add a Host", form=form)