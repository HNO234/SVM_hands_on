from libsvm.svmutil import *
import matplotlib.pyplot as plt
import numpy as np

K, test = [], []

for k in [1, 2, 4, 8, 16]:
    K.append(k)

    ytr, xtr = svm_read_problem('satimage.scale.tr.norm')
    yt, xt = svm_read_problem('satimage.scale.t.norm')
    m = svm_train(ytr, xtr, "-q -t 1 -d 2 -c 1024 -w0 " + str(k))
    p_label, p_acc, p_val = svm_predict(yt, xt, m)
    test.append(p_acc[1])

plt.plot(K, test, color='g')
plt.xscale('log', base=2)
plt.savefig('h.png')
