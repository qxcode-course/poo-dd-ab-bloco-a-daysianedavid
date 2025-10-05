class Car:
    def __init__(self):
        self.passengers = 0
        self.km = 0
        self.passMax = 2
        self.gas = 0
        self.gasMax = 100

    def toString(self):
        return "pass: " + str(self.passengers) + ", gas: " + str(self.gas) + ", km: " + str(self.km)

    def enter(self):
        if self.passengers < self.passMax:
            self.passengers += 1
        else:
            print("fail: limite de pessoas atingido")

    def leave(self):
        if self.passengers > 0:
            self.passengers -= 1
        else:
            print("fail: nao ha ninguem no carro")

    def fuel(self, amount):
        if amount < 0:
            return
        self.gas += amount
        if self.gas > self.gasMax:
            self.gas = self.gasMax
    def drive(self, distance):
        if self.passengers == 0:
            print("fail: nao ha ninguem no carro")
            return

        if self.gas == 0:
            print("fail: tanque vazio")
            return

        if self.gas >= distance:
            self.km += distance
            self.gas -= distance
        else:
            went = self.gas
            self.km += went
            self.gas = 0
            print("fail: tanque vazio apos andar " + str(went) + " km")


def main():
    car = Car()
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

            elif cmd == "show":
                print(car.toString())

            elif cmd == "enter":
                car.enter()

            elif cmd == "leave":
                car.leave()

            elif cmd == "fuel":
                if len(parts) >= 2:
                    try:
                        amount = int(parts[1])
                    except:
                        continue
                    car.fuel(amount)

            elif cmd == "drive":
                if len(parts) >= 2:
                    try:
                        dist = int(parts[1])
                    except:
                        continue
                    car.drive(dist)

            else:
                print("fail: comando invalido")

    except EOFError:
        pass


if __name__ == "__main__":
    main()