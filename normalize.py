def normalize(file):
    f = open(file, 'r')
    res = open(file + '.norm', 'w')
    line = f.readline()
    while line:
        para = line.strip().split()
        if para[1].startswith('1:'):
            sum = 0
            for i, v in enumerate(para):
                if i > 0:
                    id, idv = v.split(':')
                    idv = float(idv)
                    sum += idv * idv
            sum = sum ** 0.5
            for i, v in enumerate(para):
                if i > 0:
                    id, idv = v.split(':')
                    id = int(id)
                    idv = float(idv)
                    idv /= sum
                    res.write(' ' + str(id) + ':' + str(idv))
                else:
                    v = int(v)
                    v = (1 if v == 6 else 0)
                    res.write(str(v))
            res.write('\n')
        line = f.readline()

if __name__ == '__main__':
    normalize('satimage.scale.t')
    normalize('satimage.scale.tr')
