from flask import Flask
import random
import string
import pandas as pd

app = Flask(__name__)


@app.route("/generate_password")
def generate_password(min_length = 10, max_length = 20):
    password_length = random.randint(min_length, max_length)
    conditions = (string.digits + string.ascii_letters + string.punctuation)
    password = ''.join(random.choice(conditions) for i in range(password_length))
    return password

CSV_FILENAME = 'hw.csv'
@app.route("/calculate_average")
def calculate_average():

    data = pd.read_csv(CSV_FILENAME)
    # видалення пробілів
    data.columns = data.columns.str.strip()

    average_height = data['Height'].mean()
    average_weight = data['Weight'].mean()

    return {
        'average_height': average_height,
        'average_weight': average_weight
    }



if __name__ == '__main__':

    app.run(
        port=5000, debug=True
    )
