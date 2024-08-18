from flask import Flask, jsonify
import math
from webargs import fields
from webargs.flaskparser import use_args

from database import execute_query

app = Flask(__name__)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def contains(self, point):
        distance = math.sqrt((point.x - self.x) ** 2 + (point.y - self.y) ** 2)
        return distance <= self.radius


check_point_args = {
    "circle_x": fields.Float(required=True),
    "circle_y": fields.Float(required=True),
    "radius": fields.Float(required=True),
    "point_x": fields.Float(required=True),
    "point_y": fields.Float(required=True),
}

@app.route('/check-point', methods=['GET'])
@use_args(check_point_args, location="query")
def check_point(args):
    circle_x = args['circle_x']
    circle_y = args['circle_y']
    radius = args['radius']
    point_x = args['point_x']
    point_y = args['point_y']

    circle = Circle(circle_x, circle_y, radius)
    point = Point(point_x, point_y)

    result = circle.contains(point)

    return jsonify({"inside": result})


stats_by_city_args = {
    "genre": fields.Str(required=True)
}

@app.route('/stats-by-city', methods=['GET'])
@use_args(stats_by_city_args, location="query")
def stats_by_city(args):
    genre = args['genre']

    query = """
    SELECT customers.city, COUNT(invoice_items.invoicelineid) AS purchasecount
    FROM customers
    JOIN invoices ON customers.customerid = invoices.customerid
    JOIN invoice_items ON invoices.invoiceid = invoice_items.invoiceid
    JOIN tracks ON invoice_items.trackid = tracks.trackid
    JOIN genres ON tracks.genreid = genres.genreid
    WHERE genres.name = ?
    GROUP BY customers.city
    ORDER BY purchasecount DESC
    LIMIT 1;
    """

    results = execute_query(query, (genre,))

    if not results:
        return jsonify({"message": "No sales data found"}), 404

    city, total_sales = results[0]

    return jsonify({"city": city, "total_sales": total_sales})

if __name__ == '__main__':
    app.run(debug=True)
