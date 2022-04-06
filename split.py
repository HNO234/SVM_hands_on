import random
def split(file):
    f = open(file, 'r')
    # res = open(file + '.norm', 'w')
    lines = f.readlines()
    random.shuffle(lines)
    for i in range(10):
        res = open('train_' + str(i), 'w')
        for id, idv in enumerate(lines):
            if id % 10 != i:
                res.write(idv)
    for i in range(10):
        res = open('validate_' + str(i), 'w')
        for id, idv in enumerate(lines):
            if id % 10 == i:
                res.write(idv)


if __name__ == '__main__':
    split('satimage.scale.tr.norm')
