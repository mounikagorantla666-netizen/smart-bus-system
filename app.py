import random
import joblib
import numpy as num
from flask import Flask, render_template,request,redirect

app = Flask(__name__)
model=joblib.load("bus_arrival_model.pkl")

# Bus database
buses = {
    "101": {
        "route": "City Center",
        "arrival": "5 minutes",
        "seats": 20,
        "crowd": "Low",
        "status": "On Time"
    },

    "205": {
        "route": "Railway Station",
        "arrival": "10 minutes",
        "seats": 10,
        "crowd": "Medium",
        "status": "Running"
    },

    "330": {
        "route": "Airport",
        "arrival": "15 minutes",
        "seats": 3,
        "crowd": "High",
        "status": "Delayed"
    }
}

@app.route('/')
def home():
    return render_template("index.html", buses=buses)
    
    
@app.route('/search', methods=['POST'])
def search():
    bus_no = request.form['bus_no']

    bus = buses.get(bus_no)

    return render_template("result.html", bus=bus, bus_no=bus_no)
    
@app.route('/map')
def map():
    return render_template("map.html")

@app.route('/graph')
def graph():
    return render_template("graph.html")

@app.route('/admin', methods=['GET','POST'])
def admin():

    if request.method == 'POST':

        bus_no = request.form['bus_no']
        route = request.form['route']
        arrival = request.form['arrival']
        seats = request.form['seats']
        crowd = request.form['crowd']

        buses[bus_no] = {
            "route": route,
            "arrival": arrival,
            "seats": seats,
            "crowd": crowd,
            "status": "Running"
        }

    return render_template("admin.html")  


@app.route('/prediction')
def prediction():
    return render_template("prediction.html")


@app.route('/predict', methods=['POST'])
def predict():

    distance = float(request.form['distance'])
    traffic = float(request.form['traffic'])
    speed = float(request.form['speed'])

    prediction = model.predict([[distance,traffic,speed]])

    return render_template("prediction_result.html",time=round(prediction[0],2))    


@app.route('/display')

def display():

    buses = [

        {"bus_no":"101","route":"City Center","arrival":str(random.randint(2,10))+" min","crowd":random.choice(["Low","Medium","High"])},

        {"bus_no":"205","route":"Railway Station","arrival":str(random.randint(5,15))+" min","crowd":random.choice(["Low","Medium","High"])},

        {"bus_no":"330","route":"Bus Depot","arrival":str(random.randint(8,20))+" min","crowd":random.choice(["Low","Medium","High"])},
        
        {"bus_no":"350","route":"University","arrival":str(random.randint(8,20))+" min","crowd":random.choice(["Low","Medium","High"])},
        
        {"bus_no":"504","route":"Hospital","arrival":str(random.randint(8,20))+" min","crowd":random.choice(["Low","Medium","High"])}

    ]

    return render_template("display.html", buses=buses)


@app.route('/stop', methods=['Get','POST'])

def stop():

    stop = request.form.get('stop')
    
    if not stop:
        return redirect('/')

    buses = [

        {"bus_no":"101","route":"City Center","arrival":"5 min","crowd":"Low"},

        {"bus_no":"205","route":"Railway Station","arrival":"10 min","crowd":"Medium"},

        {"bus_no":"330","route":"Airport","arrival":"15 min","crowd":"High"}

    ]

    filtered = []

    for bus in buses:

        if bus["route"].lower() == stop.lower():

            filtered.append(bus)

    return render_template("display.html", buses=filtered)


    
if __name__ == "__main__":
    app.run(debug=True)