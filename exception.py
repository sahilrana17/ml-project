from flask import Flask
from src.logger import logging
from src.exception import CustomException
import os, sys

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    try:
        raise Exception("we are testing our Exception file")  # Error we will display
    except Exception as e:
        CE = CustomException(e, sys)
        logging.info(CE.error_message)

        logging.info("We are testing our logging file")

        return "This Is Our project"


if __name__ == "__main__":
    app.run(debug=True)