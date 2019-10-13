class Domino:
    "A single domino instance"\
    
    def __init__(self, id: int, value_1: str, value_2: str):
        self.id = id
        self.value_1 = value_1       
        self.value_2 = value_2
        self._dot_map = { 
            0 : "   ",             
            1 : " • ", 
            2 : " : ", 
            3 : "•••", 
            4 : ": :", 
            5 : ":•:", 
            6 : ":::", 
        }
        
    def __repr__(self) -> str:
        "to-string value of an object"
        return self.show()
           
    def get_value_1(self) -> int:
        "returns the first value on a domino"
        return self.value_1
        
    def get_value_2(self) -> int:
        "returns the second value on a domino"
        return self.value_2   
    
    def show(self) -> str:
        "shows a visual representation of a domino"
        return "[" + self._dot_map[self.value_1] + "|" + self._dot_map[self.value_2] + "]"
    