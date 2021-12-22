from application import app, db
from application.models import Hosts, Rules
from application.forms import HostForm, RuleForm
from flask import render_template, request, redirect, url_for

@app.route('/')
def home():
    all_hosts = Hosts.query.all()
    return render_template("index.html", title="Home", all_hosts=all_hosts)

@app.route('/create-host', methods=['GET','POST'])
def create_host():
    form = HostForm()
    form.submit.label.text = "Add Host"

    if request.method=='POST':
        new_host = Hosts(host_name=form.host_name.data, host_ip=form.host_ip.data)
        db.session.add(new_host)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("host_form.html", title="Add a Host", form=form)

@app.route('/update-host/<int:id>', methods=['GET','POST'])
def update_host(id):
    host = Hosts.query.get(id)
    form = HostForm(host_name=host.host_name, host_ip=host.host_ip)
    form.submit.label.text="Update Host"

    if request.method=='POST':
        host.host_name = form.host_name.data
        host.host_ip = form.host_ip.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("host_form.html", title="Update a Host", form=form)

@app.route('/delete-host/<int:id>')
def delete_host(id):
    host = Hosts.query.get(id)
    db.session.delete(host)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/create-rule/<int:id>', methods=['GET','POST'])
def create_rule(id):
    # host = Hosts.query.get(id)
    form = RuleForm()
    form.submit.label.text = "Add Rule"

    if request.method=='POST':
        new_rule = Rules(port=form.port.data, allow=form.allow.data, host_id=id)
        db.session.add(new_rule)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("rule_form.html", title="Add a Rule", form=form)