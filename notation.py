from icuber import *

templates = {
#    'test':'...x.xxxx...x.xxxx...x.xxxx...x.xxxx...x...x.xxxxxxxxx',
    'neutral':'......................................................',
    'empty':'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx',
    'white':'wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww',
    'centers':'xxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxxxxxx.xxxx',
    'white_cross':'x.xx.xxxxx.xx.xxxxx.xx.xxxxx.xx.xxxxx.x...x.xxxxx.xxxx',
    'first_level':'...x.xxxx...x.xxxx...x.xxxx...x.xxxx.........xxxx.xxxx',
    'second_level':'......xxx......xxx......xxx......xxx.........xxxx.xxxx',
    'yellow_cross':'......x.x......x.x......x.x......x.x.........x.x...x.x',
}

scrambles = {
#    'test':"E2", #ok
#    'test':"S2", #ok
#    'test':"M' M'", #ok
#    'test':"M M", #ko
#    'test':"S' S'", #ko
    'empty':"",
    'neutral_r':"R' R",
    'neutral_r_':"R R'",
    'neutral_l':"L' L",
    'neutral_l_':"L L'",
    'neutral_f':"F' F",
    'neutral_f_':"F F'",
    'neutral_b':"B' B",
    'neutral_b_':"B B'",
    'neutral_u':"U' U",
    'neutral_u_':"U U'",
    'neutral_d':"D' D",
    'neutral_d_':"D D'",
    'neutral_s':"S' S",
    'neutral_s_':"S S'",
    'neutral_m':"M' M",
    'neutral_m_':"M M'",
    'neutral_e':"E' E",
    'neutral_e_':"E E'",
    'neutral_x':"X' X",
    'neutral_x_':"X X'",
    'neutral_y':"Y' Y",
    'neutral_y_':"Y Y'",
    'neutral_z':"Z' Z",
    'neutral_z_':"Z Z'"
}

def main(template):
    c = Icube()

    # scramble = scrambles['test']
    # c.load(templates['test'], scramble)
    # c.execute(scramble, display=True)
    # c.image('test')

    scramble = scrambles['empty']

    # cube colourful
    c.execute(scramble, display=False, reset=True)
    c.load(templates['neutral'], scramble)
    c.image('cube_up')
    c.execute("L2 R2 M' M'", display=False, reset=True)
    c.load(templates['neutral'], scramble)
    c.image('cube_down')
    c.execute("F' B S'", display=False)
    c.load(templates['neutral'], scramble)
    c.image('cube_down_0')

    # centers
    c.execute(scramble, display=False, reset=True)
    c.load(templates['centers'], scramble)
    c.image('centers_down_0')
    c.execute("F B' S", display=False)
    c.load(templates['neutral'], scramble)
    c.image('centers_down')
    c.execute("L2 R2 M' M'", display=False)
    c.load(templates['neutral'], scramble)
    c.image('centers_up')

    # rubik's cube notation
    c.execute(scramble, display=False, reset=True)
    c.load(templates[template], scramble)
    c.image(template)
    c.load(templates[template], scrambles['neutral_r'])
    c.image('neutral_r')
    c.load(templates[template], scrambles['neutral_r_'])
    c.image('neutral_r_')
    c.load(templates[template], scrambles['neutral_l'])
    c.image('neutral_l')
    c.load(templates[template], scrambles['neutral_l_'])
    c.image('neutral_l_')
    c.load(templates[template], scrambles['neutral_f'])
    c.image('neutral_f')
    c.load(templates[template], scrambles['neutral_f_'])
    c.image('neutral_f_')
    c.load(templates[template], scrambles['neutral_b'])
    c.image('neutral_b')
    c.load(templates[template], scrambles['neutral_b_'])
    c.image('neutral_b_')
    c.load(templates[template], scrambles['neutral_u'])
    c.image('neutral_u')
    c.load(templates[template], scrambles['neutral_u_'])
    c.image('neutral_u_')
    c.load(templates[template], scrambles['neutral_d'])
    c.image('neutral_d')
    c.load(templates[template], scrambles['neutral_d_'])
    c.image('neutral_d_')
    c.load(templates[template], scrambles['neutral_s'])
    c.image('neutral_s')
    c.load(templates[template], scrambles['neutral_s_'])
    c.image('neutral_s_')
    c.load(templates[template], scrambles['neutral_m'])
    c.image('neutral_m')
    c.load(templates[template], scrambles['neutral_m_'])
    c.image('neutral_m_')
    c.load(templates[template], scrambles['neutral_e'])
    c.image('neutral_e')
    c.load(templates[template], scrambles['neutral_e_'])
    c.image('neutral_e_')
    c.load(templates[template], scrambles['neutral_x'])
    c.image('neutral_x')
    c.load(templates[template], scrambles['neutral_x_'])
    c.image('neutral_x_')
    c.load(templates[template], scrambles['neutral_y'])
    c.image('neutral_y')
    c.load(templates[template], scrambles['neutral_y_'])
    c.image('neutral_y_')
    c.load(templates[template], scrambles['neutral_z'])
    c.image('neutral_z')
    c.load(templates[template], scrambles['neutral_z_'])
    c.image('neutral_z_')

if __name__ == '__main__':
    #main('empty')
    main('white')
