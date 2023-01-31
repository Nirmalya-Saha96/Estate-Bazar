from EstateBazar import create_app

import numpy as np
from keras.models import load_model

app = create_app()
model_loaded = load_model('model.h5')

if __name__ == '__main__':
    app.run(debug=True)
