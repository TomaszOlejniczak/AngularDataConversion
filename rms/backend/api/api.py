import json
import os

import flask
from flask import jsonify
from flask import request
from flask_cors import CORS

from rms.backend.constants import LOCATION_COLUMNS, BUILDING_COLUMNS, EQ_VAL_COLUMNS, EQ_SITE_COLUMNS, WS_VAL_COLUMNS, \
    WS_SITE_COLUMNS, TO_VAL_COLUMNS, TO_SITE_COLUMNS, FR_VAL_COLUMNS, FR_SITE_COLUMNS, TR_VAL_COLUMNS, TR_SITE_COLUMNS, \
    FL_VAL_COLUMNS, FL_SITE_COLUMNS, EQ_FEATURES, WS_FEATURES, TO_FEATURES, FL_FEATURES, FR_FEATURES
from rms.backend.conversions import Converter
from rms.backend.spreadsheet import Spreadsheet

COLUMNS = LOCATION_COLUMNS + BUILDING_COLUMNS + EQ_VAL_COLUMNS + EQ_SITE_COLUMNS + WS_VAL_COLUMNS \
         + WS_SITE_COLUMNS + TO_VAL_COLUMNS + TO_SITE_COLUMNS + FR_VAL_COLUMNS + FR_SITE_COLUMNS + TR_VAL_COLUMNS\
         + TR_SITE_COLUMNS + FL_VAL_COLUMNS + FL_SITE_COLUMNS + EQ_FEATURES + WS_FEATURES + TO_FEATURES + FL_FEATURES\
         + FR_FEATURES


app = flask.Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS = CORS(app, resources={r"/api/*": {"origins": "*"}})


SAVE_DIR = '/home/tomasz/Pulpit'

@app.route("/api/process_spreadsheet", methods=["POST"])
def process_spreadsheet():
    """Processing the spreadsheet."""
    params = json.loads(request.form['read_params'])
    file = request.files['file']
    save_path = os.path.join(SAVE_DIR, file.filename)
    file.save(save_path)
    spreadsheet = Spreadsheet(save_path)
    spreadsheet.load(**params)
    converter = Converter()
    proposals = converter.generate_columns_mapping(spreadsheet)
    return jsonify(spreadsheet=spreadsheet.df.to_dict(), column_conversions=proposals,
                   rms_columns=COLUMNS)


@app.route("/api/apply_conversion", methods=["POST"])
def apply_conversion():
    sov_name = request.get_json().get('sov_name')
    conversions = request.get_json().get('conversions')


def main():
    """Starting the Flask server for API."""

    app.run()


if __name__ == "__main__":
    main()
