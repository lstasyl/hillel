import numpy as np
import pandas as pd
from faker import Faker
from flask import Flask, request, Response

app = Flask(__name__)
fake = Faker()

@app.route('/generate-students', methods=['GET'])
def generate_students():
    count = int(request.args.get('count', 100))
    if count > 1000:
        count = 1000

    students = []
    for _ in range(count):
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
    df.to_csv(csv_file, index=False)

    with open(csv_file, 'r') as file:
        csv_content = file.read()  # Read whole file

    # Directly return csv data with text/plain mimetype
    return Response(csv_content, mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True)
