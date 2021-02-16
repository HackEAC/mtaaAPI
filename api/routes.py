from flask import current_app as app
from flask import jsonify
from mtaa import tanzania
from typing import List, Dict

@app.route('/api/tanzania', methods=['GET'])
def tanzan():
    return jsonify({ "regions": list(tanzania.get_dict().keys()) })

@app.route('/api/tanzania/<region>', methods=['GET'])
def regions(region: str) -> Dict:
    temp: str = region.lower().capitalize()
    payload = tanzania.get_dict()[temp]
    return jsonify({ "post_code": payload.post_code if hasattr(payload, 'post_code') else 'None', "districts": list(payload.districts.get_dict().keys()) })

@app.route('/api/tanzania/<region>/<district>', methods=['GET'])
def districts(region: str, district: str) -> Dict:
    reg: str = region.lower().capitalize()
    temp: str = district.lower().capitalize()
    payload = tanzania.get_dict()[reg].districts.get_dict()[temp]
    return jsonify({ "post_code": payload.district_post_code if hasattr(payload, 'district_post_code') else 'None', "wards": list(payload.wards.get_dict().keys()) })


@app.route('/api/tanzania/<region>/<district>/<ward>', methods=['GET'])
def wards(region: str, district: str, ward: str) -> Dict:
    reg: str = region.lower().capitalize()
    dist: str = district.lower().capitalize()
    temp: str = ward.lower().capitalize()
    payload = tanzania.get_dict()[reg].districts.get_dict()[dist].wards.get_dict()[temp]
    return jsonify({ "post_code": payload.ward_post_code if hasattr(payload, 'ward_post_code') else "None", "streets": list(payload.streets.get_dict().keys()) })


@app.route('/api/tanzania/<region>/<district>/<ward>/<street>', methods=['GET'])
def streets(region: str, district: str, ward: str, street: str) -> Dict:
    reg: str = region.lower().capitalize()
    dist: str = district.lower().capitalize()
    ward: str = ward.lower().capitalize()
    temp: str = street.lower().capitalize()
    payload = tanzania.get_dict()[reg].districts.get_dict()[dist].wards.get_dict()[ward].streets.get_dict()[temp]
    return jsonify({ "more": payload })
