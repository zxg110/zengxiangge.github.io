import numpy as np


def markov_chain():
    matrix = np.matrix([[0.9, 0.075, 0.025], [0.15, 0.8, 0.05],
                        [0.25, 0.25, 0.5]], dtype=float)
    current = np.matrix([[0.3, 0.4, 0.3]], dtype=float)
    pi = []
    for i in range(100):
        current = current * matrix
        print "Current round:", i + 1
        print current



if __name__ == '__main__':
    markov_chain()
