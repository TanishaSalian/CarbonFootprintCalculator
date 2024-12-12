import matplotlib.pyplot as plt  
from flask import Flask, render_template, request
import os

app = Flask(__name__)

# Function to calculate emissions
def calculate_footprint(data):
    conversion_factors = {
        "travel": {
            "car_petrol": 2.31 / 100,
            "car_diesel": 2.68 / 100,
            "car_electric": 0.50 / 100,
            "public_transport": 0.1 / 100,
            "air_travel": 0.25 / 100
        },
        "energy": {
            "electricity": 0.233,
            "gas": 2.05
        },
        "waste": 0.15
    }

    travel_emissions = 0
    if data["car_fuel_type"] == "petrol":
        travel_emissions += data["car_mileage"] * conversion_factors["travel"]["car_petrol"]
    elif data["car_fuel_type"] == "diesel":
        travel_emissions += data["car_mileage"] * conversion_factors["travel"]["car_diesel"]
    elif data["car_fuel_type"] == "electric":
        travel_emissions += data["car_mileage"] * conversion_factors["travel"]["car_electric"]

    travel_emissions += data["public_transport_km"] * conversion_factors["travel"]["public_transport"]
    travel_emissions += data["air_travel_km"] * conversion_factors["travel"]["air_travel"]

    energy_emissions = data["electricity_kwh"] * conversion_factors["energy"]["electricity"]
    if data["renewable_source"] == "no":
        energy_emissions += data["gas_usage"] * conversion_factors["energy"]["gas"]

    waste_emissions = data["waste_generated"] * conversion_factors["waste"]

    total_emissions = travel_emissions + energy_emissions + waste_emissions
    return {
        "travel": travel_emissions,
        "energy": energy_emissions,
        "waste": waste_emissions,
        "total": total_emissions
    }

# Route for the home page
@app.route("/")
def index():
    return render_template("index.html")

# Route for calculating and displaying the results
@app.route("/result", methods=["POST"])
def result():
    data = {
        "car_mileage": float(request.form["car_mileage"]),
        "car_fuel_type": request.form["car_fuel_type"].lower(),
        "public_transport_km": float(request.form["public_transport_km"]),
        "air_travel_km": float(request.form["air_travel_km"]),
        "electricity_kwh": float(request.form["electricity_kwh"]),
        "gas_usage": float(request.form["gas_usage"]),
        "renewable_source": request.form["renewable_source"].lower(),
        "waste_generated": float(request.form["waste_generated"]),
    }

    emissions = calculate_footprint(data)
    generate_chart(emissions)

    return render_template("result.html", emissions=emissions)

@app.route("/suggestions")
def suggestions():
    suggestions_list = [
        {
            "Category": "Travel",
            "Suggestion": [
                "Usage of public transport, biking, or carpooling to reduce emissions.",
                "Consider  to an electric vehicle or hybrid car.",
                "Limit air travel and opt for virtual meetings whenever possible."
            ]
        },
        {
            "category": "Energy",
            "suggestion": [
                "Switch to renewable energy sources like solar or wind power.",
                "Install energy-efficient appliances and LED lighting.",
                "Seal drafts and insulate your home to save energy."
            ]
        },
        {
            "category": "Waste",
            "suggestion": [
                "Reduce, reuse, and recycle to minimize waste.",
                "Compost organic waste instead of sending it to a landfill.",
                "Avoid single-use plastics and choose sustainable packaging."
            ]
        }
    ]
    return render_template("suggestions.html", suggestions=suggestions_list)


# Function to generate the chart
def generate_chart(emissions):
    categories = ["Travel", "Energy", "Waste"]
    values = [emissions["travel"], emissions["energy"], emissions["waste"]]

    plt.figure(figsize=(8, 6))
    plt.bar(categories, values, color=["#3498db", "#2ecc71", "#e74c3c"])
    plt.xlabel("Emissions Categories")
    plt.ylabel("Emissions (kg CO2)")
    plt.title(" A Breakdown of your Carbon Footprint")
    plt.savefig("static/chart.png")
    plt.close()

if __name__ == "__main__":
    app.run(debug=True)


