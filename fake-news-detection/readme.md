

# Fake News Detection Using LSTM and GloVe Embeddings

## Overview

This project aims to classify news articles as **REAL** or **FAKE** using deep learning techniques. The model leverages pre-trained GloVe word embeddings 
and an LSTM-based neural network architecture to achieve accurate text classification.

---

## Screenshots

![Fake News Detection Screenshot](screenshots/fake%20news.png)



## Dataset

- The dataset (`news.csv`) contains news articles with the following columns:
  - `title`: The headline/title of the news article.
  - `text`: The body content of the news article.
  - `label`: The category indicating whether the news is `REAL` or `FAKE`.

- An extra unnamed column was removed during preprocessing.

---

## Preprocessing

- Dropped the unnamed column.
- Label encoding was applied to convert categorical labels (`REAL`, `FAKE`) into numeric values (`0` for REAL, `1` for FAKE).
- Titles were tokenized and converted to sequences.
- Sequences were padded to a fixed length (`max_length = 54`) using post-padding and post-truncating.
- Used only the first 3000 samples for training and validation.
- Split the data with 90% for training and 10% for testing.

---

## Word Embeddings

- Downloaded and extracted pre-trained GloVe embeddings (`glove.6B.50d.txt`).
- Created an embedding matrix to map the dataset's vocabulary to 50-dimensional GloVe vectors.
- The embedding layer in the model uses these pre-trained vectors (set as non-trainable).

---

## Model Architecture

- Embedding layer initialized with GloVe vectors.
- Dropout layer (rate = 0.2) for regularization.
- 1D Convolutional layer (`Conv1D`) with 64 filters and kernel size of 5 for feature extraction.
- MaxPooling layer to reduce dimensionality.
- LSTM layer with 64 units for capturing long-term dependencies.
- Dense output layer with sigmoid activation for binary classification.

---

## Training

- Model compiled with `binary_crossentropy` loss and `adam` optimizer.
- Trained for 50 epochs with validation on a 10% holdout set.
- Achieved validation accuracy around ~77-79%.

---

## Requirements

- Python 3.x
- TensorFlow
- NumPy
- Pandas
- scikit-learn

---

## How to Run

1. Clone the repository.
2. Download the `news.csv` dataset and place it in the project directory.
3. Run the Python script/notebook to preprocess data, build the model, and train.
4. Ensure you have internet connection for downloading GloVe embeddings (automatically downloaded if not present).

---

## Notes

- Currently, only the `title` field is used for tokenization and model input for simplicity and speed.
- Further improvements could involve combining title and full text, experimenting with hyperparameters, or using other pretrained embeddings.
- The embedding layer is frozen to leverage the knowledge from GloVe without fine-tuning.

---



