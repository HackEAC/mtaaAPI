from flask import current_app as app
from flask import jsonify, render_template
from mtaa import tanzania
from typing import Dict


@app.get('/')
def home():
    return render_template('README.html')


@app.get('/api')
def api():
    return render_template('index.html')


@app.get('/api/tanzania')
def tanzan():
    """
    Returns a list of all the regions in Tanzania
    """
    return jsonify({"regions": list(tanzania.get_dict().keys())})


@app.get('/api/tanzania/<region>')
def regions(region: str) -> Dict:
    """
    Returns a list of all the districts in the given Region and the region's post code
    """
    temp: str = region.lower().capitalize()
    payload = tanzania.get_dict()[temp]
    return jsonify({"post_code": payload.post_code if hasattr(payload, 'post_code') else 'None', "districts": list(payload.districts.get_dict().keys())})


@app.get('/api/tanzania/<region>/<district>')
def districts(region: str, district: str) -> Dict:
    """
    Returns a list of all the wards in the given District and the district's post code
    """
    reg: str = region.lower().capitalize()
    temp: str = district.lower().capitalize()
    payload = tanzania.get_dict()[reg].districts.get_dict()[temp]
    return jsonify({"post_code": payload.district_post_code if hasattr(payload, 'district_post_code') else 'None', "wards": list(payload.wards.get_dict().keys())})


@app.get('/api/tanzania/<region>/<district>/<ward>')
def wards(region: str, district: str, ward: str) -> Dict:
    """
    Returns a list of all the streets in the given Ward and the ward's post code, if any
    """
    reg: str = region.lower().capitalize()
    dist: str = district.lower().capitalize()
    temp: str = ward.lower().capitalize()
    payload = tanzania.get_dict()[reg].districts.get_dict()[
        dist].wards.get_dict()[temp]
    return jsonify({"post_code": payload.ward_post_code if hasattr(payload, 'ward_post_code') else "None", "streets": list(payload.streets.get_dict().keys())})


@app.get('/api/tanzania/<region>/<district>/<ward>/<street>')
def streets(region: str, district: str, ward: str, street: str) -> Dict:
    reg: str = region.lower().capitalize()
    dist: str = district.lower().capitalize()
    ward: str = ward.lower().capitalize()
    temp: str = street.lower().capitalize()
    payload = tanzania.get_dict()[reg].districts.get_dict(
    )[dist].wards.get_dict()[ward].streets.get_dict()[temp]
    return jsonify({"more": payload})
