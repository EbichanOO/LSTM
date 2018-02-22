#This lstm is from book("深層学習").
import numpy as np

class LSTM_B:
    def __init__(self, long):
        self.input_gate = 1 #np.one(long)
        self.forget_gate = 1 #np.ones(long)
        self.inW = [list(np.random.rand(long)) for i in ['in', 'inI', 'inF', 'inO']]
        self.W = [list(np.random.rand(long)) for i in ['in', 'I', 'F', 'O']]
        self.b = [list(np.zeros(long))]
        self.log = {0}
        self.logS = 0

    def mainLSTM(self, inputdata, t):
        F = np.sum(self.inW*inputdata)
        B = np.sum(self.inW*self.logS)

    def Igate(self, x, z, s):
        SUMs = np.sum(self.W['inI']*x) + np.sum(z) + np.sum(s)

    def sigmoid(self, x):
        return 1/(1+np.exp(-x))

    def tanh(self, x):
        return (np.exp(x)-np.exp(-x))/(np.exp(x)+np.exp(-x))