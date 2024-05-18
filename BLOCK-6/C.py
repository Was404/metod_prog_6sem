# -*- coding: utf-8 -*-
class WebMarket:
    def __init__(self):
        self.securities = {}

    def issue_security(self, code):
        if code in self.securities:
            print(f"EXISTS {self.securities[code][0]} {self.securities[code][1]}")
        else:
            id = len(self.securities)
            self.securities[code] = (id, 0)
            print(f"CREATED {id} 0")

    def delete_security(self, code):
        if code in self.securities:
            id, reliability = self.securities[code]
            del self.securities[code]
            print(f"OK {id} {reliability}")
        else:
            print("BAD REQUEST")

    def reliability_change(self, code, reliability):
        if code in self.securities:
            self.securities[code] = (self.securities[code][0], reliability)
            print(f"OK {self.securities[code][0]} {self.securities[code][1]}")
        else:
            print("BAD REQUEST")

    def find_security(self, n):
        if len(self.securities) == 0:
            print("EMPTY")
            return
        sorted_securities = sorted(self.securities.items(), key=lambda x: (-x[1][1], x[1][0]))
        if n >= len(sorted_securities):
            n = len(sorted_securities) - 1
        code, (id, reliability) = sorted_securities[n]
        print(f"OK {code} {id} {reliability}")


# Основная часть программы
web_market = WebMarket()

N = int(input())
for _ in range(N):
    query = input().split()
    if query[0] == "ISSUE":
        web_market.issue_security(query[1])
    elif query[0] == "DELETE":
        web_market.delete_security(query[1])
    elif query[0] == "RELIABILITY":
        web_market.reliability_change(query[1], int(query[2]))
    elif query[0] == "FIND":
        web_market.find_security(int(query[1]))
