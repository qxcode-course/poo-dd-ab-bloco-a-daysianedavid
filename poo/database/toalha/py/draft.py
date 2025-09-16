class Towel:
    #contrutor
    def __init__ (self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0
    
    def dry (self, amount: int) -> None:
        self.wetness += amount

    def __str__ (self) -> str:
        return f"cor: {self.color}, tamanho: {self.size}, umidade: {self.wetness}"
    
vermelha = Towel ("red", "M")
azul = Towel ("blue", "G")

print (vermelha.color)
print (vermelha.size)
print (vermelha.wetness)
