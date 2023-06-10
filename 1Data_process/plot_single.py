
import torch
import matplotlib.pyplot as plt


def open_and_get(path, interval=1):
    file = open(path)
    s = file.readline()
    s = s.split(', ')
    s.pop()
    temp = []
    for i,x in enumerate(s):
        x = float(x)
        if i%interval == 0 or i == len(s) - 1:
            temp.append(x)
    t = torch.tensor(temp)
    return t


def generate_plot(x, names, ylabel, volume, intervals, title=""):
    for index in range(x):
        t = open_and_get('out' + str(index) + '.txt', intervals[index])
        plt.plot([i for i in range(volume + 1) if i%intervals[index] == 0], t, label=names[index])

    plt.title(title)
    plt.xlabel('communication round')
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.show()


generate_plot(2, ['FedMF', 'FedSoMF'], 'ACC', 400, [10, 10])