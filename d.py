from libsvm.svmutil import *
import matplotlib.pyplot as plt
import numpy as np

para = [(1, 2 ** 10), (2, 2 ** 10), (3, 2 ** 10), (4, 2 ** 10)]
D, val, test, sv = [], [], [], []

for i, v in enumerate(para):
    D.append(v[0])
    error = np.array([])
    for j in range(10):
        ytrain, xtrain = svm_read_problem('train_' + str(j))
        ytest, xtest = svm_read_problem('validate_' + str(j))
        m = svm_train(ytrain, xtrain, "-q -t 1 -d " + str(v[0]) + " -c " + str(v[1]))
        p_label, p_acc, p_val = svm_predict(ytest, xtest, m)
        error = np.append(error, [p_acc[1]])

    ytr, xtr = svm_read_problem('satimage.scale.tr.norm')
    yt, xt = svm_read_problem('satimage.scale.t.norm')
    m = svm_train(ytr, xtr, "-q -t 1 -d " + str(v[0]) + " -c " + str(v[1]))
    p_label, p_acc, p_val = svm_predict(yt, xt, m)

    val.append(np.average(error))
    test.append(p_acc[1])
    sv.append(len(m.get_SV()))

plt.plot(D, val, color='b')
plt.plot(D, test, color='g')
plt.savefig("d_1.png")
plt.clf()
plt.plot(D, sv, color='b')
plt.savefig("d_2.png")
