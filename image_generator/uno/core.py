import PIL.Image
import PIL.ImageDraw
import PTS

from image_generator.utils import calculatePositionFullCenter, getPilData


DIRECTORY = '/'.join(__file__.replace('\\', '/').split('/')[:-1] + [''])
UNO_BASE = DIRECTORY + 'uno_base.jpg'

def createUno(cardText, faceText = '', color = (0, 0, 0), cardColor = None, faceColor = None, font = 'consolas', cardFont = None, faceFont = None):
    """
    Creates an UNO meme image.
    :param cardText:  The text to put on the card.
    :param faceText:  The text to put on the face, if any.
    :param color:     The color to use for all text, should a specific section
                      not be specified.
    :param cardColor: The color of the text to put on the card.
    :param faceColor: The color of the test to put on the face.
    :param font:      The font to use for all text, should a specifc section not
                      be specified.
    :param cardFont:  The font to use for the card text.
    :param faceFont:  The font to use for the face text.
    """
    # Get the colors.
    cardColor = cardColor or color
    faceColor = faceColor or color

    # Get the fonts.
    cardFont = cardFont or font
    faceFont = faceFont or font

    # Get the formtted text.
    cardTextFinal = PTS.fitText(cardText, 145, 84, cardFont, fast = True)
    faceTextFinal = PTS.fitText(faceText, 243, 64, faceFont, fast = True) if faceText else None

    # Load the image and prepare for drawing.
    im = PIL.Image.open(UNO_BASE)
    draw = PIL.ImageDraw.ImageDraw(im)

    cardTextSize = cardTextFinal[1].getsize_multiline(cardTextFinal[0])
    posCard = calculatePositionFullCenter(84, 164, 145, cardTextSize[0], 84, cardTextSize[1])

    if faceText:
        faceTextSize = faceTextFinal[1].getsize_multiline(faceTextFinal[0])
        posFace = calculatePositionFullCenter(254, 2, 243, faceTextSize[0], 64, faceTextSize[1])

    # Draw the text.
    draw.text(posCard, cardTextFinal[0], cardColor, cardTextFinal[1])
    if faceText:
        draw.text(posFace, faceTextFinal[0], faceColor, faceTextFinal[1], align = 'center')

    # Save the data and return it as a png image.
    out = getPilData(im)
    im.close()
    return out
