from cuber import *

class Color:
    GREEN = 0
    RED = 1
    BLUE = 2
    ORANGE = 3
    WHITE = 4
    YELLOW = 5
    CYAN = 6

class Side(object):
    F = 0
    R = 1
    B = 2
    L = 3
    U = 4
    D = 5

class Char:
    GREEN = 'g'
    RED = 'r'
    BLUE = 'b'
    ORANGE = 'o'
    WHITE = 'w'
    YELLOW = 'y'
    CYAN = 'x'

class Move:
    F = 'F'
    F_ = "F'"
    F2 = 'F2'
    B = 'B'
    B_ = "B'"
    B2 = 'B2'
    L = 'L'
    L_ = "L'"
    L2 = 'L2'
    R = 'R'
    R_ = "R'"
    R2 = 'R2'
    U = 'U'
    U_ = "U'"
    U2 = 'U2'
    D = 'D'
    D_ = "D'"
    D2 = 'D2'
    S = 'S'
    S_ = "S'"
    S2 = 'S2'
    M = 'M'
    M_ = "M'"
    M2 = 'M2'
    E = 'E'
    E_ = "E'"
    E2 = 'E2'
    X = 'X'
    X_ = "X'"
    X2 = 'X2'
    Y = 'Y'
    Y_ = "Y'"
    Y2 = 'Y2'
    Z = 'Z'
    Z_ = "Z'"
    Z2 = 'Z2'

class Arrow:
    F = '......rrr.........d..d..d..'
    F_ = '......lll.........u..u..u..'
    B = 'lll.................u..u..u'
    B_ = 'rrr.................d..d..d'
    L = 'd..d..d..d..d..d...........'
    L_ = 'u..u..u..u..u..u...........'
    R = '..u..u..u..u..u..u.........'
    R_ = '..d..d..d..d..d..d.........'
    U = '.........lll......lll......'
    U_ = '.........rrr......rrr......'
    D = '...............rrr......rrr'
    D_ = '...............lll......lll'
    S = '...rrr.............d..d..d.'
    S_ = '...lll.............u..u..u.'
    M = '.u..u..u..u..u..u..........'
    M_ = '.d..d..d..d..d..d..........'
    E = '............rrr......rrr...'
    E_ = '............lll......lll...'
    X = 'uuuuuuuuuuuuuuuuuu.........'
    X_ = 'dddddddddddddddddd.........'
    Y = '.........llllllllllllllllll'
    Y_ = '.........rrrrrrrrrrrrrrrrrr'
    Z = 'rrrrrrrrr.........ddddddddd'
    Z_ = 'lllllllll.........uuuuuuuuu'

class Icube(Cube):
    def __init__(self, size=3):
        super(Icube, self).__init__()
        self.scramble = ''

    def marrow(self, move):
        table = {
            Move.F: Arrow.F,
            Move.F_: Arrow.F_,
            Move.F2: Arrow.F,
            Move.B: Arrow.B,
            Move.B_: Arrow.B_,
            Move.B2: Arrow.B,
            Move.L: Arrow.L,
            Move.L_: Arrow.L_,
            Move.L2: Arrow.L,
            Move.R: Arrow.R,
            Move.R_: Arrow.R_,
            Move.R2: Arrow.R,
            Move.U: Arrow.U,
            Move.U_: Arrow.U_,
            Move.U2: Arrow.U,
            Move.D: Arrow.D,
            Move.D_: Arrow.D_,
            Move.D2: Arrow.D,
            Move.S: Arrow.S,
            Move.S_: Arrow.S_,
            Move.S2: Arrow.S,
            Move.M: Arrow.M,
            Move.M_: Arrow.M_,
            Move.M2: Arrow.M_,
            Move.E: Arrow.E,
            Move.E_: Arrow.E_,
            Move.E2: Arrow.E,
            Move.X: Arrow.X,
            Move.X_: Arrow.X_,
            Move.X2: Arrow.X,
            Move.Y: Arrow.Y,
            Move.Y_: Arrow.Y_,
            Move.Y2: Arrow.Y,
            Move.Z: Arrow.Z,
            Move.Z_: Arrow.Z_,
            Move.Z2: Arrow.Z
        }
        return table[move]

    def from_color_to_char(self, color):
        table = {
            Color.GREEN: Char.GREEN,
            Color.RED: Char.RED,
            Color.BLUE: Char.BLUE,
            Color.ORANGE: Char.ORANGE,
            Color.WHITE: Char.WHITE,
            Color.YELLOW: Char.YELLOW,
            Color.CYAN: Char.CYAN
        }
        return table[color]

    def from_char_to_color(self, char):
        table = {
            Char.GREEN: Color.GREEN,
            Char.RED: Color.RED,
            Char.BLUE: Color.BLUE,
            Char.ORANGE: Color.ORANGE,
            Char.WHITE: Color.WHITE,
            Char.YELLOW: Color.YELLOW,
            Char.CYAN: Color.CYAN
        }
        return table[char]

    def load(self, template, scramble='', size=200):
        self.scramble = scramble
        self.image_size = size
        tloading = list(template)
        for index, color in enumerate(self.colors):
            if len(tloading) > index and (tloading[index] == 'x' or tloading[index] != '.'):
                self.colors[index] = self.from_char_to_color(tloading[index])

    def cchar(self, c):
        table = {
                    Color.GREEN: Back.GREEN,
                    Color.RED: Back.RED,
                    Color.BLUE: Back.BLUE,
                    Color.ORANGE: Back.MAGENTA,
                    Color.WHITE: Back.WHITE,
                    Color.YELLOW: Back.YELLOW,
                    Color.CYAN: Back.CYAN
                }
        return table[c] + "  " + Back.RESET

    def execute(self, scramble, reset=False, display=False):
        self.scramble = scramble
        if scramble != '':
            super(Icube, self).execute(scramble, reset, display)
        else:
            if display:
                self.display()

    def cdisplay(self):
        indices = self.top_line(Side.U) + self.middle_line(Side.U) + self.bottom_line(Side.U)
        indices += self.top_line(Side.F) + self.middle_line(Side.F) + self.bottom_line(Side.F)
        indices += self.top_line(Side.R) + self.middle_line(Side.R) + self.bottom_line(Side.R)
        return "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}".format(*[self.from_color_to_char(self.colors[c]) for c in indices])

    def adisplay(self):
        items = self.scramble.split(' ')
        if len(items) > 0 and items[0] != '':
            return self.marrow(items[-1])

    def image(self, filename):
        url = 'http://software.rubikscube.info/icube/icubet.php?fl={}&al={}&size={}'.format(self.cdisplay(),self.adisplay(),self.image_size)
        print 'Loading {}'.format(url)
        # import urllib.request
        # urllib.request.urlretrieve(url, filename + '.png')
        import urllib2
        request = urllib2.Request(url)
        img = urllib2.urlopen(request).read()
        with open (filename + '.png', 'w') as f:
            f.write(img)
        print 'Saved image {}.png'.format(filename)
