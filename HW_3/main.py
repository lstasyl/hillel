from http import HTTPStatus

import pandas as pd
import requests
from faker import Faker
from flask import Flask, request, jsonify, Response
import csv


import httpx

app = Flask(__name__)
fake = Faker()


@app.route('/generate-students', methods=['GET'])
def generate_students():
    number_student = request.args.get("number_student", "100")

    if not number_student.isdigit():
        return "Error! Enter the number of students"

    number_student = int(number_student)

    if not 1 <= number_student <= 1000:
        return "Error! Enter the number of students between 1 and 1000"

    students = []
    for _ in range(number_student):
        student = {
            'First Name': fake.first_name(),
            'Last Name': fake.last_name(),
            'Email': fake.email(),
            'Password': fake.password(),
            'Birthday': fake.date_of_birth(minimum_age=18, maximum_age=60).isoformat()
        }
        students.append(student)

    df = pd.DataFrame(students)
    csv_file = 'students.csv'
    df.to_csv(csv_file)

    data = []
    with open(csv_file, newline='') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    return jsonify(data)


@app.route('/bitcoin-rate', methods=['GET'])
def get_bitcoin_value():
    currency = request.args.get('currency', 'USD')
    count = int(request.args.get('count', 1))

    url = f"https://bitpay.com/api/rates/{currency}"
    result = httpx.get(url)

    if result.status_code != HTTPStatus.OK:
        return Response("ERROR: Something went wrong with bitpay.com!", status=result.status_code)

    data = result.json()
    rate = data['rate']
    total_value = rate * count

    return jsonify({'currency': currency, 'rate': rate, 'count': count, 'total_value': total_value})


if __name__ == '__main__':
    app.run(debug=True)
