class Calculator:
    def __init__(self, batteryMax):
        self.display = 0.0
        self.battery = 0
        self.batteryMax = batteryMax

    def toString(self):
        # display com 2 casas e battery inteiro
        return "display = {:.2f}, battery = {}".format(self.display, self.battery)

    def charge(self, amount):
        self.battery += amount
        if self.battery > self.batteryMax:
            self.battery = self.batteryMax

    def sum(self, a, b):
        # precisa de bateria
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        self.display = a + b
        self.battery -= 1

    def div(self, den, num):
        # precisa de bateria
        if self.battery <= 0:
            print("fail: bateria insuficiente")
            return
        # divide por zero gasta bateria e mostra erro
        if num == 0:
            self.battery -= 1
            print("fail: divisao por zero")
            return
        self.display = den / num
        self.battery -= 1


def main():
    calc = None
    try:
        while True:
            line = input().strip()
            if line == "":
                continue

            # ecoa comando
            print("$" + line)

            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break

            elif cmd == "init":
                # init batteryMax
                if len(parts) >= 2:
                    maxb = int(parts[1])
                    calc = Calculator(maxb)

            elif cmd == "show":
                if calc is not None:
                    print(calc.toString())

            elif cmd == "charge":
                if calc is not None and len(parts) >= 2:
                    amt = int(parts[1])
                    calc.charge(amt)

            elif cmd == "sum":
                if calc is not None and len(parts) >= 3:
                    a = float(parts[1])
                    b = float(parts[2])
                    calc.sum(a, b)

            elif cmd == "div":
                if calc is not None and len(parts) >= 3:
                    den = float(parts[1])
                    num = float(parts[2])
                    # note: division by zero check uses num == 0.0
                    if num == 0.0:
                        # follow spec: consumes battery and prints error in div()
                        calc.div(den, num)
                    else:
                        calc.div(den, num)

            else:
                print("fail: comando invalido")

    except EOFError:
        pass


if __name__ == "__main__":
    main()