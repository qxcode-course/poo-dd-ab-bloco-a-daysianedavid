class Towel:
    def __init__(self, color, size):
        self.color = color
        self.size = size
        self.wetness = 0

    def getMaxWetness(self):
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        else:
            return 0

    def dry(self, amount):
        self.wetness = self.wetness + amount
        max_w = self.getMaxWetness()
        if self.wetness >= max_w:
            print("toalha encharcada")
            self.wetness = max_w

    def wringOut(self):
        self.wetness = 0

    def isDry(self):
        return self.wetness == 0

    def show(self):
        print("Cor: " + self.color + ", Tamanho: " + self.size + ", Umidade: " + str(self.wetness))


def main():
    towel = None
    try:
        while True:
            line = input()
            if line is None:
                break
            line = line.strip()
            if line == "":
                continue

            print("$" + line)

            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break

            elif cmd == "criar":
                if len(parts) >= 3:
                    color = parts[1]
                    size = parts[2]
                    towel = Towel(color, size)

            elif cmd == "mostrar":
                if towel is not None:
                    towel.show()

            elif cmd == "seca":
                if towel is not None:
                    if towel.isDry():
                        print("sim")
                    else:
                        print("nao")

            elif cmd == "enxugar":
                if towel is not None and len(parts) >= 2:
                    try:
                        amount = int(parts[1])
                    except:
                        continue
                    towel.dry(amount)

            elif cmd == "torcer":
                if towel is not None:
                    towel.wringOut()

            else:
                print("fail: comando invalido")

    except EOFError:
        pass


if __name__ == "__main__":
    main()