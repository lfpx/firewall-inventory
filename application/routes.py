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

@app.route('/update-host/<int:host_id>', methods=['GET','POST'])
def update_host(host_id):
    host = Hosts.query.get(host_id)
    form = HostForm(host_name=host.host_name, host_ip=host.host_ip)
    form.submit.label.text="Update Host"

    if request.method=='POST':
        host.host_name = form.host_name.data
        host.host_ip = form.host_ip.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("host_form.html", title="Update a Host", form=form)

@app.route('/delete-host/<int:host_id>')
def delete_host(host_id):
    host = Hosts.query.get(host_id)
    db.session.delete(host)
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/create-rule/<int:host_id>', methods=['GET','POST'])
def create_rule(host_id):
    # host = Hosts.query.get(id)
    form = RuleForm()
    form.submit.label.text = "Add Rule"

    if request.method=='POST':
        new_rule = Rules(port=form.port.data, allow=form.allow.data, host_id=host_id)
        db.session.add(new_rule)
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("rule_form.html", title="Add a Rule", form=form)

@app.route('/update-rule/<int:rule_id>', methods=['GET','POST'])
def update_rule(rule_id):
    rule = Rules.query.get(rule_id)
    form = RuleForm(port=rule.port, allow=rule.allow)
    form.submit.label.text="Update Rule"

    if request.method=='POST':
        rule.port = form.port.data
        rule.allow = form.allow.data
        db.session.commit()
        return redirect(url_for("home"))

    return render_template("rule_form.html", title="Update a Rule", form=form)