from flask import Flask,request, flash, url_for, redirect, render_template

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/songs_api'
                                        #postgresql://{seu_usuario}:{sua_senha}@{maquina_do_postgres}:{porta}/{banco_postegres}
app.config['SECRET_KEY'] = "random string"
db = SQLAlchemy(app)
migrate = Migrate(app, db)

class SongsModel(db.Model):
    __tablename__ = "songs"

    id = db.Column(db.Integer, primary_key=True)
    name_song =db.Column(db.String)
    singer=db.Column(db.String)
    music_style= db.Column(db.String)
    song_writer= db.Column(db.String)
    release_year= db.Column(db.String)


    def __init__ (self, name_song, singer, music_style, song_writer,release_year):
        self.name_song = name_song
        self.singer= singer
        self.music_style= music_style
        self.song_writer=song_writer
        self.release_year=release_year

    def __repr__(self):
        return f' <Song: {self.name_song}>'


    @app.route('/')
    def show_all():
        return render_template('show_all.html', songs = SongsModel.query.all() )

    @app.route('/new', methods = ['GET', 'POST'])
    def new():
        if request.method == 'POST':
            if not request.form['name_song'] or not request.form['singer'] or not request.form['music_style'] or not request.form['song_writer'] or not request.form['release_year']:
                flash('Please enter all the fields', 'error')
            else:
                newsong = SongsModel(request.form['name_song'], request.form['singer'], request.form['music_style'], request.form['song_writer'], request.form['release_year'])
                db.session.add(newsong)
                db.session.commit()
                
                flash('Record was successfully added')
                return redirect(url_for('show_all'))
        return render_template('new.html')
                    
if __name__ == '__main__':
        db.create_all()
        app.run(debug=True)
