import tensorflow as tf
from tensorflow.python.keras import Sequential
from tensorflow.python.keras.callbacks import EarlyStopping
from tensorflow.python.keras.layers import LSTM, Dropout, Dense, SpatialDropout1D, Embedding
import torch.nn as nn
from src.modules.data_loader import load_data


class LSTM(nn.Module):

    def __init__(self, vocabulary_size, output_size, embedding_size, hidden_size, n_layers, dropout_prob=0.5):
        super().__init__()
        self.output_size = output_size
        self.n_layers = n_layers
        self.hidden_size = hidden_size

        self.embedding = nn.Embedding(vocabulary_size, embedding_size)
        self.lstm = nn.LSTM(embedding_size, hidden_size, n_layers, dropout=dropout_prob, batch_first=True)

        self.dropout = nn.Dropout(0.3)

        self.fully_connected = nn.Linear(hidden_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x, hidden):
        batch_size = x.size(0)
        embed_out = self.embedding(x)
        lstm_out, hidden = self.lstm(embed_out, hidden)

        lstm_out = lstm_out.contiguous().view(-1, self.hidden_size)

        out = self.dropout(lstm_out)
        out = self.fully_connected(out)
        sigmoid_out = self.sigmoid(out)

        # reshape to be batch_size first
        sigmoid_out = sigmoid_out.view(batch_size, -1)
        sigmoid_out = sigmoid_out[:, -1]  # get last batch of labels

        return sigmoid_out, hidden

    def init_hidden(self, batch_size):
        # Create two new tensors with sizes n_layers x batch_size x hidden_size,
        # initialized to zero, for hidden state and cell state of LSTM
        weight = next(self.parameters()).data
        hidden_layer = (weight.new(self.n_layers, batch_size, self.hidden_size).zero_(),
                        weight.new(self.n_layers, batch_size, self.hidden_size).zero_())

        return hidden_layer






