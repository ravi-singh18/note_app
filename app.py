from flask import Flask, render_template, request, session #used session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my key'
@app.route('/', methods=["GET","POST"]) #GET method also included
def index():
    if request.method == 'POST':
        if request.form['submit_action'] == 'add':
            curr_notes = session['notes']
            note = request.form['note']
            if bool(note) & (note not in curr_notes):
                curr_notes.append(note)
        else:
            del_notes = request.form.getlist('del_notes')
            curr_notes = session['notes']
            for note in del_notes:
                if note in del_notes:
                    curr_notes.remove(note)
        session['notes'] = curr_notes
    else:
        if 'notes' not in session:
            session['notes'] = []
    return render_template('home.html', notes = session['notes'])

if __name__ == '__main__':
    app.run(debug=True)