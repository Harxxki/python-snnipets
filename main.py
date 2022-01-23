from sys import stdin

if __name__ == '__main__':
    # inputの高速化
    input = stdin.readline

    # 参考: https://qiita.com/ell/items/1f519aff0cdc3cf16284

    # 【1行】1文字
    s = input()  # sはstr型

    # 【1行】1数字
    n = int(input())  # nはint型

    # 【1行】n文字
    a, b, c = input().split()  # 3個の文字列の入力を受け取る
    str_list = list(input().split())  # n個の文字列がリストに格納される

    # 【1行】n数字
    a, b, c = map(int, input().split())  # 3個の数字の入力を受け取る
    num_list = list(map(int, input().split()))  # n個の数字がリストに格納される

    # 【n行】1文字
    n = int(input())  # nは入力回数
    str_list = [input() for _ in range(n)]
    print(str_list)  # 出力を確認

    # 【n行】1数字
    n = int(input())  # nは入力回数
    num_list = [int(input()) for _ in range(n)]
    print(num_list)  # 出力を確認

    # 【n行】n文字
    n = int(input())  # nは入力回数
    str_list = []
    for i in range(n):
        str_list.append(list(input().split()))
    print(str_list)

    # 内包表記
    n = int(input())  # nは入力回数
    str_list = [list(input().split()) for _ in range(n)]
    print(str_list)

    # 【n行】n数字
    n = int(input())  # nは入力回数
    num_list = []
    for i in range(n):
        num_list.append(list(map(int, input().split())))
    print(num_list)

    # 内包表記
    n = int(input())  # nは入力回数
    num_list = [list(map(int, input().split())) for _ in range(n)]
    print(num_list)
