import base64
import io

from PIL import ImageGrab, Image
from flask import Blueprint
from flask import Flask
from selenium import webdriver

sc = Blueprint('sc', __name__, url_prefix='/')


def create_app():
    app = Flask(__name__)
    app.register_blueprint(sc)
    return app


@sc.route("/dsc")
def driver_screen_capture():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--kiosk")
    options.add_experimental_option("excludeSwitches", ['enable-automation'])

    driver = webdriver.Chrome(options=options)
    driver.fullscreen_window()
    driver.get("http://www.python.org")

    image_data = driver.get_screenshot_as_png()
    my_screen = Image.open(io.BytesIO(image_data))
    my_screen.thumbnail((360, 360))

    buffer = io.BytesIO()
    my_screen.save(buffer, format="PNG")
    thumb = base64.b64encode(buffer.getvalue()).decode('ascii')

    driver.close()

    return f'<img src="data:image/png;base64,{thumb}">'


@sc.route("/sc")
@sc.route("/sc/<int:size>")
def screen_capture(size=360):
    my_screen = ImageGrab.grab()
    my_screen.thumbnail((size, size))

    buffer = io.BytesIO()
    my_screen.save(buffer, format="PNG")
    thumb = base64.b64encode(buffer.getvalue()).decode('ascii')

    return f'<img src="data:image/png;base64,{thumb}">'
