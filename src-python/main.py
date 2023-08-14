from Board import Board
from Find import Find

if __name__ == '__main__':
    m, n = map(int, input().split(' '))
    b = []
    for i in range(m):
        b.append(input().split(' '))
    bb = Board(m, n, b)
    F = Find(bb)

    F.bfs_search()
    print('#######################################################################################')
    F.bidi_search()
    print('#######################################################################################')
    F.IDDFS()
    print('#######################################################################################')
    F.A_star()
    print('#######################################################################################')
    F.IDA_star()
