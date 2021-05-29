import mtaa
from flask import current_app as app
from flask import jsonify, render_template
from mtaa import tanzania
from typing import Dict


LEVELS = {
    'regions': mtaa.regions,
    'districts': mtaa.districts,
    "wards": mtaa.wards,
    "streets": mtaa.streets
}


def get_postcode(payload, level):
    return getattr(payload, level, "")


@app.get('/')
def home():
    return render_template('README.html')


@app.get('/api')
def api():
    return render_template('index.html')


@app.get('/api/all/<level>')
def get_all(level):
    return jsonify(LEVELS.get(level, {}))


@app.get('/api/tanzania')
def tanzan():
    """
    Returns a list of all the regions in Tanzania
    """
    return jsonify({"regions": list(tanzania)})


@app.get('/api/tanzania/<region>')
def regions(region: str) -> Dict:
    """
    Returns a list of all the districts in the given Region and the region's post code
    """
    region: str = region.lower().capitalize()
    payload = tanzania.get(region)
    postcode = get_postcode(payload, 'post_code')
    return jsonify({"post_code": postcode, "districts": list(payload.districts)})


@ app.get('/api/tanzania/<region>/<district>')
def districts(region: str, district: str) -> Dict:
    """
    Returns a list of all the wards in the given District and the district's post code
    """
    reg: str = region.lower().capitalize()
    dist: str = district.lower().capitalize()
    payload = tanzania.get(reg).districts.get(dist)
    postcode = get_postcode(payload, 'district_post_code')
    wards = list(payload.wards)
    wards.remove('ward_post_code')
    return jsonify({"post_code": postcode, "wards": wards})


@app.get('/api/tanzania/<region>/<district>/<ward>')
def wards(region: str, district: str, ward: str) -> Dict:
    """
    Returns a list of all the streets in the given Ward and the ward's post code, if any
    """
    reg: str = region.lower().capitalize()
    dist: str = district.lower().capitalize()
    ward: str = ward.lower().capitalize()
    payload = tanzania.get(reg).districts.get(dist).wards.get(ward)
    post_code = get_postcode(payload, 'ward_post_code')
    streets = list(payload.streets)
    return jsonify({"post_code": post_code, "streets": streets})


@app.get('/api/tanzania/<region>/<district>/<ward>/<street>')
def streets(region: str, district: str, ward: str, street: str) -> Dict:
    reg: str = region.lower().capitalize()
    dist: str = district.lower().capitalize()
    ward: str = ward.lower().capitalize()
    temp: str = street.lower().capitalize()
    payload = tanzania.get(reg).districts.get(
        dist).wards.get(ward).streets.get(temp)
    return jsonify({"more": payload})
