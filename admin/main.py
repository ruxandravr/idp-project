from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import csv
import sys

app = Flask(__name__)

def helper_inserare_bauturi(nume, pret):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('inserare_bauturi', (nume, pret))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_inserare_mancare(nume, pret):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('inserare_mancare', (nume, pret))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_inserare_inventar(furnizor, nume, cantitate):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('inserare_inventar', (furnizor, nume, cantitate))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_inserare_clienti(nume, data, stoc):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('inserare_clienti', (nume, data, stoc))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_stergere_bauturi(id):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('stergere_bauturi', (id,))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()


def helper_stergere_mancare(id):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('stergere_mancare', (id,))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()

def helper_stergere_inventar(id):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('stergere_inventar', (id,))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()


def helper_stergere_clienti(id):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    try:
        db_cursor.callproc('stergere_clienti', (id,))
        if db_cursor.stored_results() is not None:
            for res in db_cursor.stored_results():
                print("RESULT, ", res.fetchall(), file=sys.stderr)
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()


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

def helper_selectare_clienti():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('selectare_clienti')
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

def helper_bilant_zilnic():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('bilant_zilnic')
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

def helper_top_produse():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('top_produse')
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

def helper_cel_mai_vandut_produs():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.execute('SELECT cel_mai_vandut_produs()')
        if db_cursor.stored_results() is not None:
            result = db_cursor.fetchone()
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result

def helper_castig_total_luna(luna):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.execute('SELECT castig_total_luna(' + luna + ')')
        if db_cursor.stored_results() is not None:
            result = db_cursor.fetchone()
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result

def helper_castig_total_data(data):
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.execute('SELECT castig_total_data(\"' + data + '\")')
        if db_cursor.stored_results() is not None:
            result = db_cursor.fetchone()
    except mysql.connector.Error:
        print("EROARE ", mysql.connector.Error, file=sys.stderr)
    finally:
        connection.commit()
        db_cursor.close()
        connection.close()
    return result

def helper_selectare_backup_produse():
    connection = mysql.connector.connect(**config)
    db_cursor = connection.cursor()
    result = None
    try:
        db_cursor.callproc('selectare_backup_produse')
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


# database configs
config = {
'user': 'bd',
'password': '1234',
'host': 'db',
'port': '3306',
'database': 'bd'
}

# admin app's main page displays all the options
@app.route('/', methods=['GET', 'POST'])
def index() -> str:
    return render_template("main.html")

# adauga o bautura cu datele extrase din formular
@app.route('/inserare_bautura', methods=['GET', 'POST'])
def inserare_bautura() -> str:
    if request.method == 'POST':
        formDetails = request.form
        nume = formDetails['nume']
        pret = formDetails['pret']
        helper_inserare_bauturi(nume, pret)
        return redirect('/')
    return render_template("inserare_bautura.html")

# adauga un fel de mancare cu datele extrase din formular
@app.route('/inserare_mancare', methods=['GET', 'POST'])
def inserare_mancare() -> str:
    if request.method == 'POST':
        formDetails = request.form
        nume = formDetails['nume']
        pret = formDetails['pret']
        helper_inserare_mancare(nume, pret)
        return redirect('/')
    return render_template("inserare_mancare.html")

# adauga un fel de mancare cu datele extrase din formular
@app.route('/inserare_inventar', methods=['GET', 'POST'])
def inserare_inventar() -> str:
    if request.method == 'POST':
        formDetails = request.form
        nume = formDetails['nume']
        furnizor = formDetails['furnizor']
        cantitate = formDetails['cantitate']
        helper_inserare_inventar(furnizor, nume, cantitate)
        return redirect('/')
    return render_template("inserare_inventar.html")

    # adauga un fel de mancare cu datele extrase din formular
@app.route('/inserare_clienti', methods=['GET', 'POST'])
def inserare_clienti() -> str:
    if request.method == 'POST':
        formDetails = request.form
        nume = formDetails['nume']
        data = formDetails['data']
        stoc = formDetails['stoc']
        helper_inserare_clienti(nume, data, stoc)
        return redirect('/')
    return render_template("inserare_clienti.html")

# sterge o bautura cu idul selectat din formular
@app.route('/stergere_bautura', methods=['GET', 'POST'])
def stergere_bautura() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        helper_stergere_bauturi(id)
        return redirect('/')
    return render_template("stergere_bautura.html")

# sterge un fel de mancare cu idul selectat din formular
@app.route('/stergere_mancare', methods=['GET', 'POST'])
def stergere_mancare() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        helper_stergere_mancare(id)
        return redirect('/')
    return render_template("stergere_mancare.html")

@app.route('/stergere_inventar', methods=['GET', 'POST'])
def stergere_inventar() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        helper_stergere_inventar(id)
        return redirect('/')
    return render_template("stergere_inventar.html")

@app.route('/stergere_clienti', methods=['GET', 'POST'])
def stergere_clienti() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        helper_stergere_clienti(id)
        return redirect('/')
    return render_template("stergere_clienti.html")


# afiseaza un tabel cu toate bauturile
@app.route('/selectare_bautura')
def selectare_bautura() -> str:
    detalii = helper_selectare_bauturi()
    return render_template("selectare_bautura.html", detalii=detalii)

# afiseaza un tabel cu toate felurile de mancare
@app.route('/selectare_mancare')
def selectare_mancare() -> str:
    detalii = helper_selectare_mancare()
    return render_template("selectare_mancare.html", detalii=detalii)

@app.route('/selectare_inventar')
def selectare_inventar() -> str:
    detalii = helper_selectare_inventar()
    return render_template("selectare_inventar.html", detalii=detalii)

@app.route('/selectare_clienti')
def selectare_clienti() -> str:
    detalii = helper_selectare_clienti()
    return render_template("selectare_clienti.html", detalii=detalii)

@app.route('/selectare_tranzactii')
def selectare_tranzactii() -> str:
    detalii = helper_selectare_tranzactii()
    return render_template("selectare_tranzactii.html", detalii=detalii)

@app.route('/selectare_backup_produse')
def selectare_backup_produse() -> str:
    detalii = helper_selectare_backup_produse()
    return render_template("selectare_backup_produse.html", detalii=detalii)

@app.route('/modificare_bautura_nume', methods=['GET', 'POST'])
def modificare_bautura_nume() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        nume = formDetails['nume']
        helper_modificare_bautura_nume(id, nume)
        return redirect('/')
    return render_template("modificare_bautura_nume.html")

@app.route('/modificare_bautura_pret', methods=['GET', 'POST'])
def modificare_bautura_pret() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        pret = formDetails['pret']
        helper_modificare_bautura_pret(id, pret)
        return redirect('/')
    return render_template("modificare_bautura_pret.html")

@app.route('/modificare_mancare_nume', methods=['GET', 'POST'])
def modificare_mancare_nume() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        nume = formDetails['nume']
        helper_modificare_mancare_nume(id, nume)
        return redirect('/')
    return render_template("modificare_mancare_nume.html")

@app.route('/modificare_mancare_pret', methods=['GET', 'POST'])
def modificare_mancare_pret() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        pret = formDetails['pret']
        helper_modificare_mancare_pret(id, pret)
        return redirect('/')
    return render_template("modificare_mancare_pret.html")

@app.route('/modificare_inventar_nume', methods=['GET', 'POST'])
def modificare_inventar_nume() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        nume = formDetails['nume']
        helper_modificare_inventar_nume(id, nume)
        return redirect('/')
    return render_template("modificare_inventar_nume.html")

@app.route('/modificare_inventar_furnizor', methods=['GET', 'POST'])
def modificare_inventar_furnizor() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        furnizor = formDetails['furnizor']
        helper_modificare_inventar_furnizor(id, furnizor)
        return redirect('/')
    return render_template("modificare_inventar_furnizor.html")

@app.route('/modificare_inventar_cantitate', methods=['GET', 'POST'])
def modificare_inventar_cantitate() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        cantitate = formDetails['cantitate']
        helper_modificare_inventar_cantitate(id, cantitate)
        return redirect('/')
    return render_template("modificare_inventar_cantitate.html")


@app.route('/bilant_zilnic')
def bilant_zilnic() -> str:
    detalii = helper_bilant_zilnic()
    return render_template("bilant_zilnic.html", detalii=detalii)


@app.route('/top_produse')
def top_produse() -> str:
    detalii = helper_top_produse()
    return render_template("top_produse.html", detalii=detalii)

@app.route('/best_produs')
def best_produs() -> str:
    best = helper_cel_mai_vandut_produs()[0]
    return render_template("afisare_mesaj.html", msj1="Cel mai vândut produs este ", msj2=best)

@app.route('/castig_data', methods=['GET', 'POST'])
def castig_data() -> str:
    if request.method == 'POST':
        formDetails = request.form
        data = formDetails['data']
        castig = helper_castig_total_data(data)[0]
        return render_template("afisare_mesaj.html", msj1="Câștigul in această dată este ", msj2=castig)
    return render_template("castig_data.html")

@app.route('/castig_luna', methods=['GET', 'POST'])
def castig_luna() -> str:
    if request.method == 'POST':
        formDetails = request.form
        luna = formDetails['luna']
        castig = helper_castig_total_luna(luna)[0]
        return render_template("afisare_mesaj.html", msj1="Câștigul in această lună este ", msj2=castig)
    return render_template("castig_luna.html")

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
