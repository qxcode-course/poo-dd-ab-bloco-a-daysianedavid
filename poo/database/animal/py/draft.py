class Animal:
    def __init__(self, species: str, sound: str):
        # Espécie do animal
        self.species = species
        # Som característico
        self.sound = sound
        # Idade/estágio de vida (0 = filhote)
        self.age = 0

    def makeSound(self) -> str:
        if self.age == 0:
            return "---"   # filhote
        if self.age == 4:
            return "RIP"   # morto
        return self.sound

    def ageBy(self, increment: int) -> None:
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            return
        self.age += increment
        if self.age >= 4:
            print(f"warning: {self.species} morreu")
            self.age = 4

    def toString(self) -> str:
        return f"{self.species}:{self.age}:{self.sound}"

    def __str__(self) -> str:
        return self.toString()


def main():
    animal = Animal("", "")
    try:
        while True:
            line = input().strip()
            if line == "":
                continue

            print("$" + line)  # echo do comando

            parts = line.split()
            cmd = parts[0]

            if cmd == "end":
                break

            elif cmd == "init":
                species, sound = parts[1], parts[2]
                animal = Animal(species, sound)

            elif cmd == "grow":
                inc = int(parts[1])
                animal.ageBy(inc)

            elif cmd == "noise":
                print(animal.makeSound())

            elif cmd == "show":
                print(animal.toString())

            else:
                print("fail: comando invalido")

    except EOFError:
        pass


if __name__ == "__main__":
    main()