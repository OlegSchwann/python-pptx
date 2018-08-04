# This data is needed to convert the color name to rgb
# in function pptx.dml.color._PrstColor.rgb

# The correspondence of names and colors is taken from the standard
# ECMA-376, Part 1 Fundamentals And Markup Language Reference,
# 20.1.10.48 ST_PresetColorVal (Preset Color Value)
# https://www.ecma-international.org/publications/standards/Ecma-376.htm
# Ecma Office Open XML Part 1 - Fundamentals And Markup Language Reference.pdf
# (I hope no one else will dig into it. 😣)

NAMES_OF_COLOR = {
    'aliceBlue': 'f0f8ff',
    'antiqueWhite': 'faebd7',
    'aqua': '00ffff',
    'aquamarine': '7fffd4',
    'azure': 'f0ffff',
    'beige': 'f5f5dc',
    'bisque': 'ffe4c4',
    'black': '000000',
    'blanchedAlmond': 'ffebcd',
    'blue': '0000ff',
    'blueViolet': '8a2be2',
    'brown': 'a52a2a',
    'burlyWood': 'deb887',
    'cadetBlue': '5f9ea0',
    'chartreuse': '7fff00',
    'chocolate': 'd2691e',
    'coral': 'ff7f50',
    'cornflowerBlue': '6495ed',
    'cornsilk': 'fff8dc',
    'crimson': 'dc143c',
    'cyan': '00ffff',
    'darkBlue': '00008b',
    'darkCyan': '008b8b',
    'darkGoldenrod': 'b8860b',
    'darkGray': 'a9a9a9',
    'darkGreen': '006400',
    'darkGrey': 'a9a9a9',
    'darkKhaki': 'bdb76b',
    'darkMagenta': '8b008b',
    'darkOliveGreen': '556b2f',
    'darkOrange': 'ff8c00',
    'darkOrchid': '9932cc',
    'darkRed': '8b0000',
    'darkSalmon': 'e9967a',
    'darkSeaGreen': '8fbc8f',
    'darkSlateBlue': '483d8b',
    'darkSlateGray': '2f4f4f',
    'darkSlateGrey': '2f4f4f',
    'darkTurquoise': '00ced1',
    'darkViolet': '9400d3',
    'deepPink': 'ff1493',
    'deepSkyBlue': '00bfff',
    'dimGray': '696969',
    'dimGrey': '696969',
    'dkBlue': '00008b',
    'dkCyan': '008b8b',
    'dkGoldenrod': 'b8860b',
    'dkGray': 'a9a9a9',
    'dkGreen': '006400',
    'dkGrey': 'a9a9a9',
    'dkKhaki': 'bdb76b',
    'dkMagenta': '8b008b',
    'dkOliveGreen': '556b2f',
    'dkOrange': 'ff8c00',
    'dkOrchid': '9932cc',
    'dkRed': '8b0000',
    'dkSalmon': 'e9967a',
    'dkSeaGreen': '8fbc8b',
    'dkSlateBlue': '483d8b',
    'dkSlateGray': '2f4f4f',
    'dkSlateGrey': '2f4f4f',
    'dkTurquoise': '00ced1',
    'dkViolet': '9400d3',
    'dodgerBlue': '1e90ff',
    'firebrick': 'b22222',
    'floralWhite': 'fffaf0',
    'forestGreen': '228b22',
    'fuchsia': 'ff00ff',
    'gainsboro': 'dcdcdc',
    'ghostWhite': 'f8f8ff',
    'gold': 'ffd700',
    'goldenrod': 'daa520',
    'gray': '808080',
    'green': '008000',
    'greenYellow': 'adff2f',
    'grey': '808080',
    'honeydew': 'f0fff0',
    'hotPink': 'ff69b4',
    'indianRed': 'cd5c5c',
    'indigo': '4b0082',
    'ivory': 'fffff0',
    'khaki': 'f0e68c',
    'lavender': 'e6e6fa',
    'lavenderBlush': 'fff0f5',
    'lawnGreen': '7cfc00',
    'lemonChiffon': 'fffacd',
    'lightBlue': 'add8e6',
    'lightCoral': 'f08080',
    'lightCyan': 'e0ffff',
    'lightGoldenrodYellow': 'fafad2',
    'lightGray': 'd3d3d3',
    'lightGreen': '90ee90',
    'lightGrey': 'd3d3d3',
    'lightPink': 'ffb6c1',
    'lightSalmon': 'ffa07a',
    'lightSeaGreen': '20b2aa',
    'lightSkyBlue': '87cefa',
    'lightSlateGray': '778899',
    'lightSlateGrey': '778899',
    'lightSteelBlue': 'b0c4de',
    'lightYellow': 'ffffe0',
    'lime': '00ff00',
    'limeGreen': '32cd32',
    'linen': 'faf0e6',
    'ltBlue': 'add8e6',
    'ltCoral': 'f08080',
    'ltCyan': 'e0ffff',
    'ltGoldenrodYellow': 'fafa78',
    'ltGray': 'd3d3d3',
    'ltGreen': '90ee90',
    'ltGrey': 'd3d3d3',
    'ltPink': 'ffb6c1',
    'ltSalmon': 'ffa07a',
    'ltSeaGreen': '20b2aa',
    'ltSkyBlue': '87cefa',
    'ltSlateGray': '778899',
    'ltSlateGrey': '778899',
    'ltSteelBlue': 'b0c4de',
    'ltYellow': 'ffffe0',
    'magenta': 'ff00ff',
    'maroon': '800000',
    'medAquamarine': '66cdaa',
    'medBlue': '0000cd',
    'mediumAquamarine': '66cdaa',
    'mediumBlue': '0000cd',
    'mediumOrchid': 'ba55d3',
    'mediumPurple': '9370db',
    'mediumSeaGreen': '3cb371',
    'mediumSlateBlue': '7b68ee',
    'mediumSpringGreen': '00fa9a',
    'mediumTurquoise': '48d1cc',
    'mediumVioletRed': 'c71585',
    'medOrchid': 'ba55d3',
    'medPurple': '9370db',
    'medSeaGreen': '3cb371',
    'medSlateBlue': '7b68ee',
    'medSpringGreen': '00fa9a',
    'medTurquoise': '48d1cc',
    'medVioletRed': 'c71585',
    'midnightBlue': '191970',
    'mintCream': 'f5fffa',
    'mistyRose': 'ffe4e1',
    'moccasin': 'ffe4b5',
    'navajoWhite': 'ffdead',
    'navy': '000080',
    'oldLace': 'fdf5e6',
    'olive': '808000',
    'oliveDrab': '6b8e23',
    'orange': 'ffa500',
    'orangeRed': 'ff4500',
    'orchid': 'da70d6',
    'paleGoldenrod': 'eee8aa',
    'paleGreen': '98fb98',
    'paleTurquoise': 'afeeee',
    'paleVioletRed': 'db7093',
    'papayaWhip': 'ffefd5',
    'peachPuff': 'ffdab9',
    'peru': 'cd853f',
    'pink': 'ffc0cb',
    'plum': 'dda0dd',
    'powderBlue': 'b0e0e6',
    'purple': '800080',
    'red': 'ff0000',
    'rosyBrown': 'bc8f8f',
    'royalBlue': '4169e1',
    'saddleBrown': '8b4513',
    'salmon': 'fa8072',
    'sandyBrown': 'f4a460',
    'seaGreen': '2e8b57',
    'seaShell': 'fff5ee',
    'sienna': 'a0522d',
    'silver': 'c0c0c0',
    'skyBlue': '87ceeb',
    'slateBlue': '6a5acd',
    'slateGray': '708090',
    'slateGrey': '708090',
    'snow': 'fffafa',
    'springGreen': '00ff7f',
    'steelBlue': '4682b4',
    'tan': 'd2b48c',
    'teal': '008080',
    'thistle': 'd8bfd8',
    'tomato': 'ff6347',
    'turquoise': '40e0d0',
    'violet': 'ee82ee',
    'wheat': 'f5deb3',
    'white': 'ffffff',
    'whiteSmoke': 'f5f5f5',
    'yellow': 'ffff00',
    'yellowGreen': '9acd32'
}
