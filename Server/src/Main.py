from src.dataLoader import load_data
from src.lstm import LSTM
from src.Test import Test
from src.Train import train

def main():
    train_loader, test_loader, vocabulary_size, batch_size = load_data()
    output_size = 1
    embedding_size = 200
    hidden_size = 10
    n_layers = 2
    net = LSTM(vocabulary_size, output_size, embedding_size, hidden_size, n_layers)
    testRes = train(net, batch_size, train_loader, test_loader)
if __name__ == "__main__":
    main()