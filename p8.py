class Robot:
    def __init__(self, grid):
       self.grid = grid
       self.rows = len(grid)
       self.cols = len(grid[0])

    def find_path(self):
        path = []
        if self._find_path(0,0,path):
            return path
        return None

    def _find_path(self, row, col, path):
        if row == self.rows - 1 and col == self.cols -1:
             path.append((row, col))
             return True
        if row >= self.rows or col >= self.cols or self.grid[row][col] == 1:
             return False
        if self._find_path(row+1, col, path) or self._find_path(row, col+1, path):
             path.append((row, col))
             return True
        return False

#Ejemplo de uso
grid = [
    [0,0,1,0],
    [1,0,0,0],
    [0,0,1,0],
    [0,0,0,0]
]

robot = Robot(grid)
path = robot.find_path()

if path:
   path.reverse() #Revertir el caamino para que vaya de la esquina superirior izquierda a la inferiror derecha
   print("Ruta encontrada:")
   for row, col in path:
       print(f"{row}, {col}")
else:
    print("No se encontro una ruta valida")

