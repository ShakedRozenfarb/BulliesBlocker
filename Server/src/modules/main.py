import torch
import src.modules.globalVariables as globalVar
from src.modules.data_loader import load_data
from src.modules.lstm import LSTM
from src.modules.train import train


def main():
    train_loader, test_loader, vocabulary_size, batch_size = load_data()
    net = LSTM(vocabulary_size=vocabulary_size, output_size=1, embedding_size=200, hidden_size=10, n_layers=2)
    trainedNet = train(net, batch_size, train_loader, test_loader)
    torch.save(trainedNet, globalVar.modelFile)


if __name__ == "__main__":
    main()