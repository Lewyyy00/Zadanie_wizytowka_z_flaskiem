from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/Strona_1', methods=['GET'])
def websiteone():
    return render_template('Strona_1.html')

@app.route('/Strona_2', methods=['GET', 'POST'])
def websitetwo():
    if request.method == 'POST':
        wiadomosc = request.form.get('wiadomosc', '')
        return render_template('Strona_2.html', wiadomosc=wiadomosc)
    return render_template('Strona_2.html', wiadomosc=None)

if __name__ == '__main__':
    app.run(debug=True)
