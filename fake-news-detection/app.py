
from flask import Flask, render_template, request
import tensorflow as tf
import pickle
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load model and tokenizer
model = tf.keras.models.load_model("fake_news_model.h5")
with open('tokenizer.pickle', 'rb') as handle:
    tokenizer = pickle.load(handle)

# Constants
max_length = 54
padding_type = 'post'
trunc_type = 'post'

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html', prediction_text=None, news_text="")

@app.route('/predict', methods=['POST'])
def predict():
    news_text = request.form['news']
    seq = tokenizer.texts_to_sequences([news_text])
    padded = pad_sequences(seq, maxlen=max_length, padding=padding_type, truncating=trunc_type)
    prediction = model.predict(padded, verbose=0)[0][0]
    confidence = round(prediction * 100 if prediction >= 0.5 else (1 - prediction) * 100, 2)
    label = "REAL ✅" if prediction >= 0.5 else "FAKE ❌"
    result = f"This news is likely: {label} (Confidence: {confidence}%)"
    return render_template('index.html', prediction_text=result, news_text=news_text)

if __name__ == "__main__":
    app.run(debug=True)
