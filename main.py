import abc

class AbstractVector2D(abc.ABC):
    @abc.abstractmethod
    def __init__(self):
        self._x: int
        self._y: int
        pass

    @abc.abstractmethod
    def len(self):
        pass

    @abc.abstractmethod
    def __len__(self):
        pass

    @abc.abstractmethod
    def __add__(self, other):
        pass

    @abc.abstractmethod
    def __str__(self):
        pass

    @abc.abstractmethod
    def __mul__(self, other):
        pass

    @abc.abstractmethod
    def __sub__(self, other):
        pass

    @abc.abstractmethod
    def normalized(self):
        pass

    @abc.abstractmethod
    def normalize(self):
        pass

    @abc.abstractmethod
    def project(self, other):
        pass

class AbstractVector3D(abc.ABC):
    @abc.abstractmethod
    def __init__(self) -> None:
        super().__init__()

    @abc.abstractmethod
    def __add__(self):
        pass

    @abc.abstractmethod
    def __sub__(self, other):
        pass

    @abc.abstractmethod
    def __mul__(self, other:int|Vector3D):
        """What am i even supposed to do here, huh?
        There are multiple ways to multiple vectors yo"""
        pass

class Vector2D(AbstractVector2D):
    def __init__(self, x:int, y:int ):
        self._x = x
        self._y = y
        super().__init__()

    def len(self):
        return (self._x**2+self._y**2)**0.5
    
    def __len__(self):
        return self.len()
    
    def __add__(self, other: 'Vector2D'):
        return Vector2D(self._x+other._x, self._y+other._y)
    
    def __str__(self):
        return "{"+str(self._x)+"; "+str(self._y)+"}"
    
    def __mul__(self, other):
        othertype = type(other)
        if othertype==Vector2D:
            return self._x*other._x + self._y*other._y
        elif othertype==int or othertype==float:
            return Vector2D(self._x*other, self._y*other)
    
    def __sub__(self, other):
        return Vector2D(self._x-other._x, self._y-other._y)
    
    def normalize(self):
        x = self._x
        y = self._y
        ln = self.len()
        self._x = x/ln
        self._y = y/ln
        return None

    def normalized(self):
        x = self._x
        y = self._y
        ln = self.len()
        normalizedVector = Vector2D(x/ln, y/ln)
        return normalizedVector

    def project(self, other):
        return other*((self*other)/(other*other))

class Vector3D(AbstractVector3D):
    def __init__(self, x:int|float, y:int|float, z:int|float) -> None:
        super().__init__()
        self._x = x
        self._y = y
        self._z = z
    def __add__(self, other):
        return Vector3D(self._x+other._x,self._y+other._y,self._z+other._z)
    def __sub__(self, other):
        return Vector3D(self._x-other._x,self._y-other._y,self._z-other._z)
    def __mul__(self, other:int|Vector3D):
        '''
        # Scary stuff may happen here!
        # Different kinds of vector multiplication
        # Wow so undefined :3
        if type(other) == int:
            return Vector3D(self._x*other, self._y*other, self._z*other)
        elif type(other) == Vector3D:
        '''


def main():
    v1 = Vector2D(3,4)
    v2 = Vector2D(12,5)
    v3 = v1.normalized()
    print(v3, v1.len())

if __name__ == "__main__":
    main()
