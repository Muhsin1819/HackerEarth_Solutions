t = int(input())
for i in range(t):
    num = int(input())
    dict = {
            1: f"{num + 11} WS",
            2: f"{num + 9} MS",
            3: f"{num + 7} AS",
            4: f"{num + 5} AS",
            5: f"{num + 3} MS",
            6: f"{num + 1} WS",
            7: f"{num - 1} WS",
            8: f"{num - 3} MS",
            9: f"{num - 5} AS",
            10: f"{num -7} AS",
            11: f"{num - 9} MS",
            0: f"{num - 11} WS"
    }
    out = dict.get((num % 12), 0)
    print(out)
