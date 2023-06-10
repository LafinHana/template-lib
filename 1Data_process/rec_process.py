def print_data(target, path):
    with open(path, 'w') as f:
        for i in target:
            f.write(i+', ')

def mian(tar):
    with open('rec_data\\film.txt', 'r') as f:
        content = f.readlines()
    f.close()
    res_rmse = []
    res_mae = []
    res_acc = []
    for i in content:
        if(i[0]!='r' or i[1]!='m'):
            continue
        temp = i.split(' ')
        res_rmse.append(temp[2][:-2])
        res_mae.append(temp[5][:-2])
        res_acc.append(temp[8][:-2])

    if tar == 'rmse':
        print_data(res_rmse, 'out0.txt')
    if tar == 'mae':
        print_data(res_mae, 'out0.txt')
    if tar == 'acc':
        print_data(res_acc, 'out0.txt')

    with open('fed_data\\film.txt', 'r') as f:
        content = f.readlines()
    res_rmse = []
    res_mae = []
    res_acc = []
    for i in content:
        if(i[0]!='v' or len(i)<=6):
            continue
        temp = i.split(' ')
        res_mae.append(temp[2][:-2])
        res_rmse.append(temp[4][5:-2])
        res_acc.append(temp[6][4:-2])
    if tar == 'rmse':
        print_data(res_rmse, 'out1.txt')
    if tar == 'mae':
        print_data(res_mae, 'out1.txt')
    if tar == 'acc':
        print_data(res_acc, 'out1.txt')


