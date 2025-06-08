from datetime import datetime
import re
import csv
import numpy
from sklearn.svm import SVR
import matplotlib.pyplot as point
import sys

dates = []
stock_prices = []

def get_data(filename):
    with open(filename, "r") as CSVfile:
        csvFileReader = csv.reader(CSVfile)
        next(csvFileReader)

        for row in csvFileReader:
            dates.append(int(row[0].split("/")[0]))
            stock_prices.append(float(row[1]))
    return

def predict_price(dates, prices, x):
    dates_np = numpy.reshape(dates, (len(dates), 1))

    svr_lin = SVR(kernel= "linear", C=1e3)
    svr_poly = SVR(kernel= "poly", C=1e3, degree=2)
    svr_rbf = SVR(kernel= "rbf", C=1e3, gamma=0.5)
    
    # Ensure prices is an array that works with numpy
    prices_np = numpy.array(prices)

    svr_rbf.fit(dates_np, prices_np)
    svr_poly.fit(dates_np, prices_np)
    svr_lin.fit(dates_np, prices_np)

    # Graphing each point on graph
    point.scatter(dates_np, prices_np, color="black", label="Data")
    point.plot(dates_np, svr_rbf.predict(dates_np), color="red", label="RBF Model")
    point.plot(dates_np, svr_lin.predict(dates_np), color="green", label="Linear Model")
    point.plot(dates_np, svr_poly.predict(dates_np), color="blue", label="Polynomial Model")

    # Labeling the graph 
    point.xlabel("Date")
    point.ylabel("Price")
    point.legend()
    point.show()

    # Converting x to be used for the 2D array
    x_for_prediction = numpy.array([[x]])

    # Self contain each prediction
    svr_rbf = svr_rbf.predict(x_for_prediction)[0]
    svr_lin = svr_lin.predict(x_for_prediction)[0]
    svr_poly = svr_poly.predict(x_for_prediction)[0]
    
    return svr_rbf, svr_lin, svr_poly

# PUT YOUR CSV FILE HERE 
get_data("Prices - Main.csv")

def main():
    # Input for grabbing the date
    target_date_str = input("What is your date? ").strip()

    if re.search(r"\d+\/\d+\/\d+", target_date_str):
        try:
            target_date_object = datetime.strptime(target_date_str, "%m/%d/%Y")
            x_value_for_prediction = target_date_object.timestamp()
            predict_price(dates, stock_prices, x_value_for_prediction)
            print("Exit success!")
        except ValueError:
            sys.exit("Format: MONTH/DAY/YEAR")
    else:
        sys.exit("Wrong format: MONTH/DAY/YEAR")

if __name__ == "__main__":
    main()