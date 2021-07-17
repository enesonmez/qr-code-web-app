import os
from datetime import datetime

from flask import Blueprint, Response, render_template, url_for, request, send_from_directory, send_file
import qrcode

from ..helpers.random_hash import uniqueFileName


dashBoard = Blueprint('dashboard', __name__)

now = datetime.now()
date_time = now.strftime("%d.%m.%Y - %H:%M:%S")

@dashBoard.route('/', methods=['GET'])
def index():
    return render_template("dashboard/index.html", active='home')


@dashBoard.route('/qr-code-create', methods=['GET', 'POST'])
def getQrCodeCreate():
    if request.method == 'GET':
        return render_template("dashboard/create_qr_code.html", active='create')
    
    elif request.method == 'POST':
        formData = request.form
        data = formData['data']
        fill = formData['fill']
        back = formData['back']

        code = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=50,
            border=2,
        )
        code.add_data(data)
        code.make(fit=True)
        img = code.make_image(fill_color=fill, back_color=back)
        fileName = uniqueFileName("enesonmez")
        locate = os.path.abspath('app/static/upload')
        img.save(locate + '\\' + fileName + '.png')
        return render_template("dashboard/create_qr_code.html", active='create', isImage=True, fileUrl = fileName) 


@dashBoard.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):    
    upload = os.path.abspath('app/static/upload')
    print(upload)
    print(filename)
    resp = send_file(upload + '\\' + filename, attachment_filename=filename, as_attachment=True)
    os.remove(upload + '\\' + filename)
    return resp #send_from_directory(upload, filename)


@dashBoard.route('/qr-code-scan', methods=['GET'])
def qrCodeScan():
    return render_template("dashboard/scan_qr_code.html", active='scan')

