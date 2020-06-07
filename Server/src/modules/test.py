import torch


class Test(object):
    test_loss = []

    def test(self, batch_size, net, test_loader, epoch, criterion):
        correct = 0
        total = 0
        epoch_loss = 0
        with torch.no_grad():
            hidden = net.init_hidden(batch_size)
            i = 0

            for inputs, labels in test_loader:
                hidden = tuple([each.data for each in hidden])
                inputs = inputs.type(torch.LongTensor)

                outputs, hidden = net(inputs, hidden)
                predicted = torch.round(outputs)
                total += labels.size(0)
                correct += (predicted == labels.flatten()).sum().item()

                loss = criterion(outputs, labels.float().flatten())
                epoch_loss += loss.item()
                i += 1

        print('test epoch [%d] loss: %.3f' % (epoch + 1, epoch_loss / i))
        print("Accuracy of the test epoch: %d %%" % (100 * correct / total))

        Test.test_loss.append(epoch_loss / i)
