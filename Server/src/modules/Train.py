import itertools
import tensorflow as tf
import torch.nn as nn
import torch
from src.Test import Test


def train(net, batch_size, train_loader, test_loader):
    # define loss function and optimizer

    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(net.parameters())
    train_loss = []

    for epoch in range(10):

        hidden = net.init_hidden(batch_size)
        running_loss = epoch_loss = 0.0
        i = 0
        for inputs, labels in train_loader:

            inputs = inputs.type(torch.LongTensor)
            hidden = tuple([each.data for each in hidden])

            # zero the parameter gradients
            optimizer.zero_grad()

            # forward + backward + optimize
            outputs, hidden = net(inputs, hidden)

            loss = criterion(outputs, labels.float().flatten())
            loss.backward()
            optimizer.step()

            running_loss += loss.item()
            epoch_loss += loss.item()
            if (i + 1) % 100 == 0:
                print('[%d, %5d] loss: %.3f' %
                      (epoch + 1, i + 1, running_loss / 100))
                running_loss = 0.0
            i += 1
        Test.test(batch_size=batch_size, net=net, test_loader=test_loader, epoch=epoch, criterion=criterion)
        train_loss.append(epoch_loss / i)

    print('\nFinished Training')