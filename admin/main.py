from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import csv
import sys

app = Flask(__name__)

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
        print(nume, pret, file=sys.stderr)

        return redirect('/')
    return render_template("inserare_bautura.html")

# adauga un fel de mancare cu datele extrase din formular
@app.route('/inserare_mancare', methods=['GET', 'POST'])
def inserare_mancare() -> str:
    if request.method == 'POST':
        formDetails = request.form
        nume = formDetails['nume']
        pret = formDetails['pret']
        print(nume, pret, file=sys.stderr)

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
        print(nume, furnizor, cantitate, file=sys.stderr)

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
        print(nume, data, stoc, file=sys.stderr)

        return redirect('/')
    return render_template("inserare_clienti.html")

# sterge o bautura cu idul selectat din formular
@app.route('/stergere_bautura', methods=['GET', 'POST'])
def stergere_bautura() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        print(id, file=sys.stderr)

        return redirect('/')
    return render_template("stergere_bautura.html")

# sterge un fel de mancare cu idul selectat din formular
@app.route('/stergere_mancare', methods=['GET', 'POST'])
def stergere_mancare() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        print(id, file=sys.stderr)

        return redirect('/')
    return render_template("stergere_mancare.html")

@app.route('/stergere_inventar', methods=['GET', 'POST'])
def stergere_inventar() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        print(id, file=sys.stderr)

        return redirect('/')
    return render_template("stergere_inventar.html")

@app.route('/stergere_clienti', methods=['GET', 'POST'])
def stergere_clienti() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        print(id, file=sys.stderr)

        return redirect('/')
    return render_template("stergere_clienti.html")


# afiseaza un tabel cu toate bauturile
@app.route('/selectare_bautura')
def selectare_bautura() -> str:
    return render_template("selectare_bautura.html", detalii=detalii)

# afiseaza un tabel cu toate felurile de mancare
@app.route('/selectare_mancare')
def selectare_mancare() -> str:
    return render_template("selectare_mancare.html", detalii=detalii)

@app.route('/selectare_inventar')
def selectare_inventar() -> str:
    return render_template("selectare_inventar.html", detalii=detalii)

@app.route('/selectare_clienti')
def selectare_clienti() -> str:
    return render_template("selectare_clienti.html", detalii=detalii)

@app.route('/selectare_tranzactii')
def selectare_tranzactii() -> str:
    return render_template("selectare_tranzactii.html", detalii=detalii)

@app.route('/selectare_backup_produse')
def selectare_backup_produse() -> str:
    return render_template("selectare_backup_produse.html", detalii=detalii)

@app.route('/modificare_bautura_nume', methods=['GET', 'POST'])
def modificare_bautura_nume() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        nume = formDetails['nume']
        print(id, nume, file=sys.stderr)
        return redirect('/')
    return render_template("modificare_bautura_nume.html")

@app.route('/modificare_bautura_pret', methods=['GET', 'POST'])
def modificare_bautura_pret() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        pret = formDetails['pret']
        print(id, pret, file=sys.stderr)
        return redirect('/')
    return render_template("modificare_bautura_pret.html")

@app.route('/modificare_mancare_nume', methods=['GET', 'POST'])
def modificare_mancare_nume() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        nume = formDetails['nume']
        print(id, nume, file=sys.stderr)

        return redirect('/')
    return render_template("modificare_mancare_nume.html")

@app.route('/modificare_mancare_pret', methods=['GET', 'POST'])
def modificare_mancare_pret() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        pret = formDetails['pret']
        print(id, pret, file=sys.stderr)

        return redirect('/')
    return render_template("modificare_mancare_pret.html")

@app.route('/modificare_inventar_nume', methods=['GET', 'POST'])
def modificare_inventar_nume() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        nume = formDetails['nume']
        print(id, nume, file=sys.stderr)

        return redirect('/')
    return render_template("modificare_inventar_nume.html")

@app.route('/modificare_inventar_furnizor', methods=['GET', 'POST'])
def modificare_inventar_furnizor() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        furnizor = formDetails['furnizor']
        print(id, furnizor, file=sys.stderr)

        return redirect('/')
    return render_template("modificare_inventar_furnizor.html")

@app.route('/modificare_inventar_cantitate', methods=['GET', 'POST'])
def modificare_inventar_cantitate() -> str:
    if request.method == 'POST':
        formDetails = request.form
        id = formDetails['id']
        cantitate = formDetails['cantitate']
        print(id, cantitate, file=sys.stderr)

        return redirect('/')
    return render_template("modificare_inventar_cantitate.html")

@app.route('/bilant_zilnic')
def bilant_zilnic() -> str:
    detalii = ""
    return render_template("bilant_zilnic.html", detalii=detalii)


@app.route('/top_produse')
def top_produse() -> str:
    detalii = []
    return render_template("top_produse.html", detalii=detalii)

@app.route('/best_produs')
def best_produs() -> str:
    best = "ERROR"
    return render_template("afisare_mesaj.html", msj1="Cel mai vândut produs este ", msj2=best)

@app.route('/castig_data', methods=['GET', 'POST'])
def castig_data() -> str:
    if request.method == 'POST':
        formDetails = request.form
        data = formDetails['data']
        castig = ""
        return render_template("afisare_mesaj.html", msj1="Câștigul in această dată este ", msj2=castig)
    return render_template("castig_data.html")

@app.route('/castig_luna', methods=['GET', 'POST'])
def castig_luna() -> str:
    if request.method == 'POST':
        formDetails = request.form
        luna = formDetails['luna']
        castig = ""
        return render_template("afisare_mesaj.html", msj1="Câștigul in această lună este ", msj2=castig)
    return render_template("castig_luna.html")


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
