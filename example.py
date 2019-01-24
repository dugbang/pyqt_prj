

if __name__ == '__main__':

    names = ['Cls', 'Bck', '', 'Close',
             '7', '8', '9', '/',
             '4', '5', '6', '*',
             '1', '2', '3', '-',
             '0', '.', '=', '+']

    positions = [(i, j, 0) for i in range(5) for j in range(4)]

    for position, name in zip(positions, names):
        print(*position[:2], name)

