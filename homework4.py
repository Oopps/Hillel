
from flask import Flask, request

app = Flask(__name__)

@app.route('/emails/list/')
def e_list():
    import sqlite3

    try:
        conn = sqlite3.connect('./db.sqlite3')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM emails;')
        result = cursor.fetchall()

        conn.commit()
    finally:
        conn.close()

    return str(result)


@app.route('/emails/create/')
def e_create():
    import sqlite3

    id = request.args['id']
    ename = request.args['ename']
    user_id = request.args['user_id']



    try:
        conn = sqlite3.connect('./db.sqlite3')
        cursor = conn.cursor()

        query = f"INSERT INTO emails VALUES ({id}, {ename}, {user_id});"

        cursor.execute(query)


        conn.commit()
    finally:
        conn.close()

    return 'ok'

@app.route('/users/create/')
def u_create():
    import sqlite3

    id = request.args['id']
    first_name = request.args['first_name']
    last_name = request.args['last_name']



    try:
        conn = sqlite3.connect('./db.sqlite3')
        cursor = conn.cursor()

        query = f"INSERT INTO emails VALUES ({id}, '{first_name}', '{last_name}');"

        cursor.execute(query)


        conn.commit()
    finally:
        conn.close()

    return 'ok'


@app.route('/users/list/')
def u_list():
    import sqlite3

    try:
        conn = sqlite3.connect('./db.sqlite3')
        cursor = conn.cursor()

        cursor.execute('SELECT * FROM users;')
        result = cursor.fetchall()

        conn.commit()
    finally:
        conn.close()

    return str(result)



@app.route('/emails/update/')
def e_update():
    import sqlite3

    id = request.args['id']
    new_ename = request.args['new_ename']


    try:
        conn = sqlite3.connect('./db.sqlite3')
        cursor = conn.cursor()

        query = f'UPDATE emails SET email = "{new_ename}" WHERE id = {id};'

        cursor.execute(query)

        conn.commit()
    finally:
        conn.close()


    return 'Updated'


@app.route('/emails/delete/')
def e_delete():
    import sqlite3

    id = request.args['id']

    try:
        conn = sqlite3.connect('./db.sqlite3')
        cursor = conn.cursor()

        query = f'DELETE FROM emails WHERE id = {id}'

        cursor.execute(query)

        conn.commit()
    finally:
        conn.close()


    return 'Deleted'

@app.route('/users/emails/')
def users_emails():
    import sqlite3

    try:
        conn = sqlite3.connect('./db.sqlite3')
        cursor = conn.cursor()

        query = f'SELECT users.first_name, users.last_name, emails.email ' \
                f'FROM users ' \
                f'INNER JOIN emails ON users.id = emails.user_id;'

        cursor.execute(query)
        result = cursor.fetchall()

        conn.commit()
    finally:
        conn.close()


    return str(result)




