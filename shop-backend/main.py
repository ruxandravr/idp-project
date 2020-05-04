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

retete_cafea = {
    "b1" : [("p2", 10)],
    "b2" : [("p2", 15), ("p4", 150), ("p8", 5)],
    "b3" : [("p1", 10), ("p5", 100), ("p6", 30)],
    "b4" : [("p1", 7), ("p3", 100), ("p7", 15), ("p8", 7)],
    "b5" : [("p5", 200), ("p11", 20)],
    "b6" : [("p6", 20), ("p9", 10), ("p3", 100)],
    "b7" : [("p5", 150), ("p11", 15), ("p6", 20)],
    "b8" : [("p3", 100), ("p9", 10), ("p11", 10)],
    "b9" : [("p1", 15), ("p5", 100), ("p8", 20)],
    "b10" : [("p1", 10), ("p4", 100), ("p11", 10), ("p6", 50)]
    }

numar_tranzactie = 0

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
        print("EROARE helper selectare inventar", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result


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
        print("EROARE helper selectare bauturi ", mysql.connector.Error, file=sys.stderr)
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
        print("EROARE helper selectare mancare", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result

def helper_cumparare_produs(id_tranzactie, id_produs, numar_card):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('cumparare_produs', (id_tranzactie, id_produs, numar_card))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE helper cumparare produs", mysql.connector.Error, file=sys.stderr)
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
        print("EROARE modificare inventar cantitate", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()


# returneaza cantitatea produsului id
def cantitate_produs(inventar, id):
    for t in inventar:
        if t[0] == id:
            return t[3]
    return 0

# verifica daca se poate prepara produsul id
def check_available(id, inventar):
    global retete_cafea
    if id in retete_cafea:
        # cerintele pentru produsul id
        cerinte = retete_cafea[id]
        # verific daca exista suficienta cantitate pentru fiecare resursa
        for k, v in cerinte:
            if (cantitate_produs(inventar, k) < v):
                return False
    return True

def bauturi_disponibile(bauturi, inventar):
    bauturi_ok = []
    for b in bauturi:
        if check_available(b[0], inventar):
            bauturi_ok.append(b)
    return bauturi_ok


def modifica_inventar(id):
    if id[0] == "m":
        return
    for k, v in retete_cafea[id]:
        inventar = helper_selectare_inventar()
        cantitate_veche = cantitate_produs(inventar, k)
        cantitate_noua = cantitate_veche - v
        helper_modificare_inventar_cantitate(k, cantitate_noua)

def verificare_cumparare(id_produs):
    # mai intai verificam sa fie un produs disponibil
    bauturi = bauturi_disponibile(helper_selectare_bauturi(), helper_selectare_inventar())
    found = False
    cost = 0
    for b in bauturi:
        if b[0] == id_produs:
            found = True
            # daca am gasit produsul ii updatam si costul
            cost = b[2]
            break
    # cautam produsul in lista de mancare
    if not found:
        for m in helper_selectare_mancare():
            if m[0] == id_produs:
                found = True
                cost = m[2]
                break

    if not found:
        return False
    return True


def get_drinks():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.execute("SELECT * from bauturi")
        drinks = db_cursor.fetchall()
    except mysql.connector.Error:
        print("EROARE get drinks", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    print(drinks, file=sys.stderr)
    return drinks

def get_food():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.execute("SELECT * from mancare")
        food = db_cursor.fetchall()
    except mysql.connector.Error:
        print("EROARE get food", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    print(food, file=sys.stderr)
    return food

def get_card_details(number):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    card = None
    try:
        db_cursor.execute("SELECT * from carduri where numar = %s",(number,))
        card = db_cursor.fetchall()
    except mysql.connector.Error:
        print("EROARE get card details", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    print("CArdul este: ", card, file=sys.stderr)
    return card[0]

def get_price(id):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    price = None
    try:
        if id[0] == "b":
            db_cursor.execute("SELECT pret from bauturi where id_produs = %s", (id,) )
        else:
            db_cursor.execute("SELECT pret from mancare where id_produs = %s", (id,) )
        price = db_cursor.fetchall()
    except mysql.connector.Error:
        print("EROARE get price", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    print(price[0], file=sys.stderr)
    return price[0][0]

def update_card(number, sold):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.execute("UPDATE carduri set sold = sold - %s where numar = %s",(sold, number))
    except mysql.connector.Error:
        print("EROARE update card", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

# admin app's main page displays all the options
@app.route('/', methods=['GET', 'POST'])
def main() -> str:
    return "ok"

# buy functionality called from the client
@app.route('/drinks', methods=['GET', 'POST'])
def drinks() -> str:
    drinks = get_drinks()
    return jsonify(drinks)

# buy functionality called from the client
@app.route('/food', methods=['GET', 'POST'])
def food() -> str:
    food = get_food()
    return jsonify(food)

# verify card details
@app.route('/verify_card/<number>/<name>/<month>/<year>/<cvv>', methods = ['GET', 'POST'])
def verify_card(number, name, month, year, cvv) -> str:
    card_details = get_card_details(number)
    if str(card_details[1]) == name and str(card_details[2]) == month and str(card_details[3]) == year and str(card_details[4]) == cvv:
        return "yes"
    return "no"

@app.route('/complete_tranzaction/<arg>', methods = ['GET', 'POST'])
def complete_tranzaction(arg)-> str:
    arg = arg.strip('][').split(', ')
    arg = [x[1:-1] for x in arg]
    print("Arg is", arg, file=sys.stderr)
    numar = arg[0]
    sold = get_card_details(numar)[5]
    total = 0
    for id in arg[1:]:
        total += int(get_price(id))
    print("Sold and total ", sold, total, file=sys.stderr)

    availbale = True
    for id in arg[1:]:
        if not verificare_cumparare(id):
            availbale = False
            break

    if sold > total and availbale:
        global numar_tranzactie
        for id in arg[1:]:
            numar_tranzactie += 1
            helper_cumparare_produs("t" + str(numar_tranzactie), id, numar)
            modifica_inventar(id)
        update_card(numar, total)
        return "yes"
    return "no"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
