# import markdown
# from os import getcwd, path
from flask import current_app as app
from flask import jsonify, render_template
from mtaa import tanzania
# from pygments.formatters import HtmlFormatter
# import markdown.extensions.fenced_code
# import markdown.extensions.codehilite

from typing import Dict

@app.route('/', methods=['GET'])
def home():
    # readme_file = open(path.join(getcwd(), "README.md"), "r")
    # md_template_string = markdown.markdown(
    #     readme_file.read(), extensions=["fenced_code" ,"codehilite"]
    # )

    # Generate Css for syntax highlighting
    # formatter = HtmlFormatter(style="monokai", full=True, cssclass="codehilite")
    # css_string = formatter.get_style_defs()
    # md_css_string = "<style>" + css_string + "</style>"
    
    # md_template = "<hmtl><body><head><title>Mtaa API</title>" + md_css_string + "</head>" + md_template_string + "</body></hmtl>"

    # return md_template
    return render_template('README.html')

@app.route('/api', methods=['GET'])
def api():
    return render_template('index.html')

@app.route('/api/tanzania', methods=['GET'])
def tanzan():
    """
    Returns a list of all the regions in Tanzania
    """
    return jsonify({ "regions": list(tanzania.get_dict().keys()) })

@app.route('/api/tanzania/<region>', methods=['GET'])
def regions(region: str) -> Dict:
    """
    Returns a list of all the districts in the given Region and the region's post code
    """
    temp: str = region.lower().capitalize()
    payload = tanzania.get_dict()[temp]
    return jsonify({ "post_code": payload.post_code if hasattr(payload, 'post_code') else 'None', "districts": list(payload.districts.get_dict().keys()) })

@app.route('/api/tanzania/<region>/<district>', methods=['GET'])
def districts(region: str, district: str) -> Dict:
    """
    Returns a list of all the wards in the given District and the district's post code
    """
    reg: str = region.lower().capitalize()
    temp: str = district.lower().capitalize()
    payload = tanzania.get_dict()[reg].districts.get_dict()[temp]
    return jsonify({ "post_code": payload.district_post_code if hasattr(payload, 'district_post_code') else 'None', "wards": list(payload.wards.get_dict().keys()) })


@app.route('/api/tanzania/<region>/<district>/<ward>', methods=['GET'])
def wards(region: str, district: str, ward: str) -> Dict:
    """
    Returns a list of all the streets in the given Ward and the ward's post code, if any
    """
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
