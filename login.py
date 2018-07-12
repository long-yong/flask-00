#!/usr/bin/python3

from flask import Flask

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        logger.debug("login post method")
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'admin123':

            session['username'] = username
            session['password'] = password
            resp = make_response(render_template('index.html', name=username))
            resp.set_cookie('username', username)
            # return resp
            return jsonify({'status': '0', 'errmsg': 'successful log in！'})
        else:
            # return redirect(url_for('error'))
            return jsonify({'status': '-1', 'errmsg': 'Username or Password error！'})

    logger.debug("login get method")
    return render_template('login.html')