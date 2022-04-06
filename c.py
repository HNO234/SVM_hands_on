from libsvm.svmutil import *
import matplotlib.pyplot as plt
import numpy as np
for d in range(1,5):
    C, avg, avg_pstd, avg_mstd = [], [], [], []

    for c in range(-10, 11):
        C.append(2 ** c)
        error = np.array([])
        for i in range(10):
            ytrain, xtrain = svm_read_problem('train_' + str(i))
            ytest, xtest = svm_read_problem('validate_' + str(i))
            m = svm_train(ytrain, xtrain, "-q -t 1 -d " + str(d) + " -c " + str(2 ** c))
            p_label, p_acc, p_val = svm_predict(ytest, xtest, m)
            error = np.append(error, [p_acc[1]])
        avg_c, std_c = np.average(error), np.std(error)
        avg += [avg_c]
        avg_pstd += [avg_c + std_c]
        avg_mstd += [avg_c - std_c]
    plt.plot(C, avg, color='b')
    plt.plot(C, avg_pstd, color='g')
    plt.plot(C, avg_mstd, color='r')
    plt.xscale('log', base=2)
    plt.savefig("c_" + str(d) + ".png")
    plt.clf()
