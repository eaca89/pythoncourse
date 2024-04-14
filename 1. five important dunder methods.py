# method 1

class Fruit:
    def __init__(self, *, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams   

    def __eq__(self, other: object) -> bool:
        # return self.grams == other.grams 
        return self.__dict__ == other.__dict__


def main() -> None:
    f1: Fruit = Fruit(name='Apple', grams=200)
    f2: Fruit = Fruit(name='Orange', grams=150)
    f3: Fruit = Fruit(name='Apple', grams=200)

    print(f1 == f2)
    print(f1 == f3)



if __name__ == '__main__':
    main()





# method 2

class Fruit:
    def __init__(self, *, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams    

    def __format__(self, format_spec: str) -> str:
        match format_spec:
            case 'kg':
                return f'{self.grams / 1000:.2f} kg'
            case 'lb':
                return f'{self.grams / 453.5924:.2f} lb'
            case 'desc':
                return f'{self.grams}g of {self.name}'
            case _:
                raise ValueError('Unknown format specifier...')
        

def main() -> None:
    apple: Fruit = Fruit(name='Apple', grams=2500)
    print(f'{apple:kg}')    
    print(f'{apple:lb}')
    print(f'{apple:desc}')
    print(f'{apple}')



if __name__ == '__main__':
    main()




# method 3

from types import UnionType

class Fruit:
    def __init__(self, *, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams

    def __or__(self, other: object) -> UnionType:
        new_name: str = f'{self.name} & {other.name}'
        new_grams: float = self.grams + other.grams

        return Fruit(name=new_name, grams= new_grams)
    
    def __repr__(self) -> str:
        return f'Fruit(name="{self.name}", grams={self.grams})'


def main() -> None:

    apple: Fruit = Fruit(name='Apple', grams=2500)
    orange: Fruit = Fruit(name='Orange', grams=1000)
    banana: Fruit = Fruit(name='Banana', grams=1500)

    combined: Fruit = apple | orange | banana
    print(combined)

    # d1: dict = {1: 'a', 2: 'b'}
    # d2: dict = {3: 'c', 4: 'd'}
    # print(d1 | d2)

    # s1: set = {1, 2}
    # s2: set = {3, 4}
    # print(s1 | s2)


if __name__ == '__main__':
    main()




# method 4

class Fruit:
    def __init__(self, *, name: str, grams: float) -> None:
        self.name = name
        self.grams = grams

    def __str__(self) -> str:
        return f'{self.name} ({self.grams}g)'
    
    def __repr__(self) -> str:
        return f'Fruit(name="{self.name}", grams={self.grams})'


def main() -> None:
    fruits: list[Fruit] = [Fruit(name='Apple', grams=2500),
                           Fruit(name='Orange', grams=1000),
                           Fruit(name='Banana', grams=1500)]    

    for fruit in fruits:
        print(f'str: {fruit}')
        print(f'repr: {repr(fruit)}')

if __name__ == '__main__':
    main()




# method 5
from dataclasses import dataclass

@dataclass(kw_only=True)
class Fruit:
    name: str
    grams: float

class Basket:
    def __init__(self, *, fruits: list[Fruit]) -> None:
        self.fruits = fruits

    def __getitem__(self, item: str) -> list[Fruit]:
        return [fruit for fruit in self.fruits if fruit.name.lower() == item]

def main() -> None:
    fruits: list[Fruit] = [Fruit(name='Apple', grams=2500),
                            Fruit(name='Apple', grams=50),
                           Fruit(name='Orange', grams=1000),
                           Fruit(name='Orange', grams=9001),                      
                           Fruit(name='Banana', grams=1500)] 

    basket: Basket = Basket(fruits=fruits)
    matches: list[Fruit] = basket['applea']
    
    print(f'Matches: {matches}')
    print(f'total: {len(matches)}')

    # print(basket['orange'])

if __name__ == '__main__':
    main()
