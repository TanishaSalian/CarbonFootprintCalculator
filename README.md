Carbon Footprint Tracker - Student Project

Overview

The Carbon Footprint Tracker is a web application designed to help the clients to calculate their carbon emissions based on their travel habits, energy usage, and waste generation. By using this application, users can better understand their environmental impact and receive suggestions on how to reduce their carbon footprint. This project is created as part of a student assignment to explore the impact of human activities on the environment.

Features

Travel Emissions Calculation: Calculates carbon emissions from car usage, public transport, and air travel.
Energy Emissions Calculation: Calculates emissions based on electricity and gas usage, with an option to consider renewable energy sources.
Waste Emissions Calculation: Provides an estimate of emissions based on the amount of waste generated.
Personalized Suggestions: Offers personalized tips on how to reduce emissions in areas like travel, energy consumption, and waste management.
Carbon Footprint Chart: Generates a visual representation of your carbon footprint to help you understand the breakdown of your emissions.
Requirements

This project uses Python with the Flask web framework and requires the following dependencies:

Python 3.x
Flask
Matplotlib
Other required libraries listed in requirements.txt
Libraries:
To install the required libraries, follow the steps in the Installation section.

Installation

1. Clone the Repository
Clone this repository to your local machine using the command
git clone https://github.com/TanishaSalian/CarbonFootprintCalculator

2. Install Dependencies
Navigate to the project directory and install the necessary libraries:
cd carbon-footprint-tracker
pip install -r requirements.txt
3. Run the Application
Once all dependencies are installed, start the Flask application by running:

python app.py

The application will run locally on your computer. Open your web browser and navigate to:
http://127.0.0.1:5000/

Usage

1. Home Page
On the Home Page, you'll find a form where you can input details about your travel, energy usage, and waste generation. The information is used to calculate your carbon footprint.

2. Input Form
Fill out the following fields to calculate your carbon footprint:
Travel: Weekly car mileage, car fuel type, public transport usage, and air travel distance.
Energy: Monthly electricity and gas usage, renewable energy source status (yes/no).
Waste: Weekly waste generation.

3. Result Page
After submitting your data, the application will:
Calculate your carbon footprint based on the provided details.
Display the total emissions along with a breakdown of emissions in three categories: Travel, Energy, and Waste.
Show a visual chart that represents the breakdown of your carbon footprint.

5. Suggestions Page
The Suggestions Page will provide you with personalized recommendations for reducing your emissions in the following areas:
Travel: Suggestions like using public transport, switching to electric cars, carpooling, etc.
Energy: Advice on adopting renewable energy sources, improving home insulation, and using energy-efficient appliances.
Waste: Tips on recycling, composting, and minimizing the use of single-use plastics.

5. Navigation
You can navigate between the Home page, Results page, and Suggestions page using the links available at the bottom of the pages.
Technologies Used
Flask: A lightweight Python web framework used to create the web application.
Matplotlib: A Python library used for creating static, animated, and interactive visualizations (used to generate the carbon footprint chart).
HTML/CSS: Used to structure and style the web pages.
Python: The primary programming language used for calculations and backend logic.

