from flask import Flask
import numpy as np
import pickle
from keras.models import load_model

app = Flask(__name__)


@app.route('/')
def helloWorld():
    model_loaded = load_model('model.h5')
    test_data = np.array([2014, 36, 4.0, 2.50, 2820, 8408])
    return str(model_loaded.predict(test_data.reshape(1,6), batch_size=1))

if __name__ == '__main__':
    app.run(debug=True)