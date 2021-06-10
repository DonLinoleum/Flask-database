from flask import Flask, request, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///base.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class snr(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'STB {self.serial}'


class stb (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'STB - {self.serial}'


class snr_arenda (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(100), nullable=False)
    nomer = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'SNR_ARENDA - {self.serial}'


class stb_arenda (db.Model):
    id = db.Column(db.Integer, primary_key=True)
    model = db.Column(db.String(100), nullable=False)
    serial = db.Column(db.String(100), nullable=False)
    nomer = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f'STB_ARENDA - {self.serial}'

# Основная страница


@app.route('/')
def main():
    Snr = snr.query.all()
    Stb = stb.query.all()
    Snr_arenda = snr_arenda.query.all()
    Stb_arenda = stb_arenda.query.all()
    return render_template('index.html', Snr=Snr, Stb=Stb, Snr_arenda=Snr_arenda, Stb_arenda=Stb_arenda)


# Добавление SNR
@app.route('/addsnr', methods=['POST', 'GET'])
def addsnr():
    if request.method == 'POST':
        Model = request.form['name']
        Serial = request.form['serial']

        Snr = snr(model=Model, serial=Serial)

        try:
            db.session.add(Snr)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так...."
    else:
        return render_template('addsnr.html')

# Добавление STB


@app.route('/addstb', methods=['POST', 'GET'])
def addstb():
    if request.method == 'POST':
        Model = request.form['name']
        Serial = request.form['serial']

        Stb = stb(model=Model, serial=Serial)
        try:
            db.session.add(Stb)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так...."

    else:
        return render_template('addsnr.html')

# Удаление SNR


@app.route('/delsnr/<int:id>', methods=['POST', 'GET'])
def delsnr(id):
    Id = id
    if request.method == "GET":
        return render_template('/delsnr.html', Id=id)
    elif request.method == "POST":
        DelItem = snr.query.get_or_404(Id)
        try:
            db.session.delete(DelItem)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так...."

# Удаление STB


@app.route('/delstb/<int:id>', methods=['POST', 'GET'])
def delstb(id):
    Id = id
    if request.method == "GET":
        return render_template('/delstb.html', Id=id)
    elif request.method == "POST":
        DelItem = stb.query.get_or_404(Id)
        try:
            db.session.delete(DelItem)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так...."


# Добавление SNR в аренду


@app.route('/addsnrarenda/<int:id>', methods=['POST', 'GET'])
def addsnrarenda(id):
    Id = id
    Item = snr.query.get_or_404(id)
    if request.method == "GET":
        return render_template('addsnrarenda.html', Id=Id)
    elif request.method == "POST":
        Model = Item.model
        Serial = Item.serial
        Nomer = request.form['nomer']
        Address = request.form['address']
        AddItem = snr_arenda(model=Model, serial=Serial,
                             nomer=Nomer, address=Address)
        try:
            db.session.add(AddItem)
            db.session.delete(Item)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так"


# Добавление STB в аренду


@app.route('/addstbarenda/<int:id>', methods=['POST', 'GET'])
def addstbarenda(id):
    Id = id
    Item = stb.query.get_or_404(id)
    if request.method == "GET":
        return render_template('addstbarenda.html', Id=Id)
    elif request.method == "POST":
        Model = Item.model
        Serial = Item.serial
        Nomer = request.form['nomer']
        Address = request.form['address']
        AddItem = stb_arenda(model=Model, serial=Serial,
                             nomer=Nomer, address=Address)
        try:
            db.session.add(AddItem)
            db.session.delete(Item)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так"


# Удаление SNR из аренды

@app.route('/delsnrarenda/<int:id>', methods=['POST', 'GET'])
def delsnrarenda(id):
    Id = id
    Item = snr_arenda.query.get_or_404(id)
    if request.method == "GET":
        return render_template('delsnrarenda.html', Id=Id)
    elif request.method == "POST":
        Model = Item.model
        Serial = Item.serial
        AddItem = snr(model=Model, serial=Serial)

        try:
            db.session.add(AddItem)
            db.session.delete(Item)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так"

# Удаление STB из аренды


@app.route('/delstbarenda/<int:id>', methods=['POST', 'GET'])
def delstbarenda(id):
    Id = id
    Item = stb_arenda.query.get_or_404(id)
    if request.method == "GET":
        return render_template('delstbarenda.html', Id=Id)
    elif request.method == "POST":
        Model = Item.model
        Serial = Item.serial
        AddItem = stb(model=Model, serial=Serial)

        try:
            db.session.add(AddItem)
            db.session.delete(Item)
            db.session.commit()
            return redirect('/')
        except:
            return "Что-то пошло не так"


if __name__ == "__main__":
    app.run(debug=True)
