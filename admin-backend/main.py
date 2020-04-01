from flask import Flask, render_template, request, redirect, url_for, jsonify
import mysql.connector
import csv
import sys

app = Flask(__name__)

# database configs
config = {
'user': 'bd',
'password': '1234',
'host': 'db',
'port': '3306',
'database': 'bd'
}


def helper_selectare_bauturi():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('selectare_bauturi')
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                result = res.fetchall()
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result

def helper_selectare_mancare():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('selectare_mancare')
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                result = res.fetchall()
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result

def helper_selectare_inventar():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('selectare_inventar')
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                result = res.fetchall()
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result

def helper_selectare_carduri():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('selectare_carduri')
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                result = res.fetchall()
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result

def helper_selectare_tranzactii():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('selectare_tranzactii')
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                result = res.fetchall()
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result


def helper_modificare_bautura_nume(id, nume):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('modificare_bauturi_nume', (id, nume))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_modificare_bautura_pret(id, pret):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('modificare_bauturi_pret', (id, pret))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()


def helper_modificare_mancare_nume(id, nume):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('modificare_mancare_nume', (id, nume))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_modificare_mancare_pret(id, pret):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('modificare_mancare_pret', (id, pret))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()


def helper_modificare_inventar_nume(id, nume):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('modificare_inventar_nume', (id, nume))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_modificare_inventar_furnizor(id, furnizor):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('modificare_inventar_furnizor', (id, furnizor))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_modificare_inventar_cantitate(id, cant):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('modificare_inventar_cantitate', (id, cant))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_adaugare_card(number, name, month, year, cvv, sold):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('inserare_card', (number, name, month, year, cvv, sold))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE Adaugare card", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()


def get_password(id):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    parola = None
    try:
        db_cursor.execute("SELECT parola from administrator where id = %s", (id,) )
        parola = db_cursor.fetchall()
    except mysql.connector.Error:
        print("EROARE get password", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    if len(parola) > 0:
        print("Parola este", parola[0][0], file=sys.stderr)
        return parola[0][0]
    return None

# admin app's main page displays all the options
@app.route('/', methods=['GET', 'POST'])
def main() -> str:
    return "ok"

# verify user id and password
@app.route('/verify_user/<id>/<pwd>', methods = ['GET', 'POST'])
def verify_user(id, pwd) -> str:
    good_pwd = get_password(id)
    if str(good_pwd) == pwd:
        return "yes"
    return "no"

@app.route('/get_items/<item>', methods = ['GET', 'POST'])
def get_items(item) -> str:
    if item == "drink":
        return jsonify(helper_selectare_bauturi())
    return jsonify(helper_selectare_mancare())

@app.route('/get_tranzactions', methods = ['GET', 'POST'])
def get_tranzactions() -> str:
    return jsonify(helper_selectare_tranzactii())

@app.route('/get_inventory', methods = ['GET', 'POST'])
def get_inventory() -> str:
    return jsonify(helper_selectare_inventar())

@app.route('/get_cards', methods = ['GET', 'POST'])
def get_cards() -> str:
    return jsonify(helper_selectare_carduri())

# add card details
@app.route('/add_card/<number>/<name>/<month>/<year>/<cvv>/<sold>', methods = ['GET', 'POST'])
def add_card(number, name, month, year, cvv, sold) -> str:
    helper_adaugare_card(number, name, month, year, cvv, sold)
    return "yes"

@app.route('/modify_drink/<id>/<nume>/<pret>', methods = ['GET', 'POST'])
def modify_drink(id, nume, pret) -> str:
    helper_modificare_bautura_nume(id, nume)
    helper_modificare_bautura_pret(id, pret)
    return "yes"

@app.route('/modify_food/<id>/<nume>/<pret>', methods = ['GET', 'POST'])
def modify_food(id, nume, pret) -> str:
    helper_modificare_mancare_nume(id, nume)
    helper_modificare_mancare_pret(id, pret)
    return "yes"

@app.route('/modify_inventory/<id>/<nume>/<furnizor>/<cantitate>', methods = ['GET', 'POST'])
def modify_inventory(id, nume, furnizor, cantitate) -> str:
    helper_modificare_inventar_nume(id, nume)
    helper_modificare_inventar_furnizor(id, furnizor)
    helper_modificare_inventar_cantitate(id, cantitate)
    return "yes"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5002)
