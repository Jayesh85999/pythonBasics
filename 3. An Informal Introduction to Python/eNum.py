from enum import Enum
class ColorByJay(Enum):
    RED = 'redd'
    GREEN = 'greeen'
    BLUE = 'bluue'

color = ColorByJay(input("Enter your choice of 'red', 'blue' or 'green': "))

match color:
    case ColorByJay.RED:
        print("I see red!")
    case ColorByJay.GREEN:
        print("Grass is green")
    case ColorByJay.BLUE:
        print("I'm feeling the blues :(")
