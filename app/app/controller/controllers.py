from app.controller.app import *
from app.model.models import Task, db
from flask import render_template, url_for, request, make_response, redirect
import json


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html', tasks=Task.query.all())


@app.route('/updateElemDone', methods=['POST'])
def update_elem_by_id():
    resp = make_response(json.dumps(request.form))
    try:
        task_id = int(request.form['id'])
        done = int(request.form['done'])
    except ValueError:
        resp.status_code = 400
        return resp
    task = Task.query.get_or_404(task_id)
    task.done = done
    db.session.commit()
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/task/<id>')
def task_details(id):
    task = Task.query.filter_by(id=id).first_or_404()
    return render_template('edit.html', task=task)


@app.route('/editElem', methods=['POST'])
def edit_task_component():
    resp = make_response(json.dumps(request.form))
    try:
        task_id = int(request.form['id'])
        task_title = request.form['title']
        task_content = request.form['content']
        done = int(request.form['done'])
    except ValueError:
        resp.status_code = 400
        return resp
    task = Task.query.get_or_404(task_id)
    task.title = task_title
    task.content = task_content
    task.done = done
    db.session.commit()
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/deleteElem', methods=['POST'])
def delete_task():
    resp = make_response(json.dumps(request.form))
    try:
        task_id = request.form['id']
    except ValueError:
        resp.status_code = 400
        return resp
    db.session.delete(Task.query.get_or_404(task_id))
    db.session.commit()
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route('/create')
def create_page():
    return render_template('create.html')


@app.route('/createElem', methods=['POST'])
def create_task():
    resp = make_response(json.dumps(request.form))
    title_val = request.form['title']
    content_val = request.form['content']
    db.session.add(Task(title_val, content_val))
    db.session.commit()
    resp.status_code = 200
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return redirect('/index')
