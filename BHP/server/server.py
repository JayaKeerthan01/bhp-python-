from flask import Flask,jsonify,request
import util

app=Flask(__name__)

@app.route('/get_location_names')
def get_location_names():
    response=jsonify({
        'locations':util.get_location_names()
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

@app.route("/get_predict_price",methods=["POST"])
def get_predict_prices():
    sqft=float(request.form["sqft"])
    location=request.form["location"]
    bhk=int(request.form["bhk"])
    bath=int(request.form["bath"])

    response=jsonify({
        "estimated_price":util.get_estimated_price(location,sqft,bath,bhk)
    })
    response.headers.add("Access-Control-Allow-Origin","*")
    return response

if __name__ == "__main__":
    app.run(debug=True)























































