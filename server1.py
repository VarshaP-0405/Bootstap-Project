from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/room')
def room():
    return render_template('room.html')

@app.route('/amenities')
def amenities():
    return render_template('amenities.html')

@app.route('/gallery')
def gallery():
    return render_template('gallery.html')

@app.route('/reservation')
def reservation():
    return render_template('reservation.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/submit_reservation', methods=['POST'])
def submit_reservation():
    return render_template('thankyou.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == '__main__':
    app.run(debug=True)



