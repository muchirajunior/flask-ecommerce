#type: ignore
from flask import current_app
from .models import Product,  OrderProduct
from PIL import Image
from werkzeug.utils import secure_filename
import shortuuid

def uploadFile(file):
    image=Image.open(file)
    image=image.resize((480,320))
    filename = secure_filename(file.filename)
    ext=filename.rsplit('.',1)[1]
    name=shortuuid.uuid()
    filename=name+'.'+ext
    folder=current_app.config['UPLOAD_FOLDER']

    image.save(str(folder)+str(filename))

    return str(filename)