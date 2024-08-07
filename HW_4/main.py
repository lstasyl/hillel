from flask import Flask, request, render_template_string, jsonify
from webargs import fields
from webargs.flaskparser import use_args

from database import execute_query

app = Flask(__name__)


def order_price(country=None):
    if country:
        query = """
            SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS Sales
            FROM invoices
            JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
            WHERE invoices.BillingCountry = ?
            GROUP BY invoices.BillingCountry
        """
        results = execute_query(query, (country,))
    else:
        query = """
            SELECT invoices.BillingCountry, SUM(invoice_items.UnitPrice * invoice_items.Quantity) AS Sales
            FROM invoices
            JOIN invoice_items ON invoices.InvoiceId = invoice_items.InvoiceId
            GROUP BY invoices.BillingCountry
        """
        results = execute_query(query)

    return results

def get_all_info_about_track(track_id):
    query = """
        SELECT tracks.Name, albums.Title, artists.Name, tracks.GenreId, tracks.Composer, tracks.Milliseconds, tracks.Bytes, tracks.UnitPrice
        FROM tracks
        JOIN albums ON tracks.AlbumId = albums.AlbumId
        JOIN artists ON albums.ArtistId = artists.ArtistId
        WHERE tracks.TrackId = ?
    """
    track_info = execute_query(query, (track_id,))
    return track_info[0] if track_info else None

def get_total_track_time():
    query = """
        SELECT SUM(Milliseconds)
        FROM tracks
    """
    total_time_ms = execute_query(query)[0][0]
    total_time_hours = total_time_ms / (1000 * 60 * 60)
    return total_time_hours

order_price_args = {
    'country': fields.Str(required=False)
}

track_info_args = {
    'track_id': fields.Int(required=True)
}


@app.route('/')
def home():
    return "Welcome to the music store!"

@app.route('/order_price', methods=['GET'])
@use_args(order_price_args, location="query")
def order_price_route():
    country = request.args.get('country')
    results = order_price(country)

    sales_data = [{'country': result[0], 'sales': result[1]} for result in results]
    return jsonify(sales_data)

@app.route('/track_info/<int:track_id>', methods=['GET'])
@use_args(track_info_args, location="view_args")
def track_info_route(track_id):
    track_info = get_all_info_about_track(track_id)

    if track_info:
        track_data = {
            'track_name': track_info[0],
            'album': track_info[1],
            'artist': track_info[2],
            'genre': track_info[3],
            'composer': track_info[4],
            'milliseconds': track_info[5],
            'bytes': track_info[6],
            'unit_price': track_info[7]
        }
        return jsonify(track_data)
    else:
        return jsonify({'error': 'Track not found'}), 404

@app.route('/total_track_time', methods=['GET'])
def total_track_time_route():
    total_time_hours = get_total_track_time()
    return jsonify({'total_track_time_hours': total_time_hours})


if __name__ == '__main__':
    app.run(debug=True)
