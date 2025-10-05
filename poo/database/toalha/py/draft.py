class Towel:
    #contrutor
    def __init__ (self, color: str, size: str):
        self.color: str = color
        self.size: str = size
        self.wetness: int = 0

    def getMaxWetness (self) -> int: 
        if self.size == "P":
            return 10
        elif self.size == "M":
            return 20
        elif self.size == "G":
            return 30
        else:
            return 0

    def dry (self, amount: int) -> None:
        self.wetness += amount
        max_wetness = self.getMaxWetness()
        if self.wetness > max_wetness:
            return ("toalha encharcada")
        else:
            return ("toalha seca")
        
    def wring (self) -> None:
        self.wetness = 0

    def __str__ (self) -> str:
        return f"cor: {self.color}, tamanho: {self.size}, umidade: {self.wetness}"
    
vermelha = Towel ("red", "M")
azul = Towel ("blue", "G")

print (vermelha.color)
print (vermelha.size)
print (vermelha.wetness)

vermelha.dry(30)
print (vermelha)
