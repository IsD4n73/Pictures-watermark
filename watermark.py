import os
from PIL import Image, ImageDraw, ImageFont




if __name__ == '__main__':
    text = input('[#] Inserisci il watermark: ').strip()
    font_size = int(input('[#] Inserisci la grandezza del font: [def:20] ') or '20')
    font_opacity = int(input('[#] Inserisci l\'opacità: [def:50] ') or '50')

    print(''' 
    
    1: top left 
    2: top center 
    3: top right
    4: middle left
    5: middle center
    6: middle right
    7: bottom left
    8: bottom center
    9: bottom right
    ''')

    position_id = int(input('[#] Inserisci la posizione: [def:9] ') or '9')
