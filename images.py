from PIL import Image as PI
from PIL import ImageTk


images = {}


# Returns a dictionary of images (key/value pair)
def getImages():
    global images

    # Singleton lazy load all the images
    if images == {}:
        images = __loadImages()

    return images


# Returns the image that goes at the row and colum in Pente
def getImage(row, column):
    global images

    # Singleton lazy load all the images
    if images == {}:
        images = __loadImages()

    return images[__getKey(row, column)]


# Returns the image that goes at the row and colum in Pente
# with a bead played in that location
def getBeadImage(row, column, currentPlayer):
    global images

    # Singleton lazy load all the images
    if images == {}:
        images = __loadImages()

    if currentPlayer == 0:
        return images[__getKey(row, column) + "Blue"]
    return images[__getKey(row, column) + "Red"]


def __getKey(row, column):
    global images

    # Center
    if row == 9 and column == 9:
        return 'center'

    # Handle the corners (outer corners)
    if row == 0 and column == 0:
        return 'cornerNorthwest'
    if row == 0 and column == 18:
        return 'cornerNortheast'
    if row == 18 and column == 0:
        return 'cornerSouthwest'
    if row == 18 and column == 18:
        return 'cornerSoutheast'

    # Bold T's (outer edge)
    if row == 0 and column == 9:
        return 'tNorthBold'
    if row == 9 and column == 0:
        return 'tWestBold'
    if row == 9 and column == 18:
        return 'tEastBold'
    if row == 18 and column == 9:
        return 'tSouthBold'

    # T's (outer edge)
    if row == 0:
        return 'tNorth'
    if column == 0:
        return 'tWest'
    if column == 18:
        return 'tEast'
    if row == 18:
        return 'tSouth'

    # Diamonds
    if (row == 6 and column == 6) or (row == 6 and column == 12) or (row == 12 and column == 6) or (row == 12 and column == 12):
        return 'diamond'
    if (row == 3 and column == 3) or (row == 3 and column == 15) or (row == 15 and column == 3) or (row == 15 and column == 15):
        return 'diamond'
    if (row == 3 and column == 9) or (row == 15 and column == 9):
        return 'diamondVertical'
    if (row == 9 and column == 3) or (row == 9 and column == 15):
        return 'diamondHorizontal'

    # Bold midway vertical and horizontal lines
    if column == 9:
        return 'vertical'
    if row == 9:
        return 'horizontal'

    # Default plus
    return 'plus'


def __loadImages():
    images = {}

    images['center'] = __load('center.gif')
    images['centerBlue'] = __load('centerBlue.gif')
    images['centerRed'] = __load('centerRed.gif')

    images['diamond'] = __load('diamond.gif')
    images['diamondBlue'] = __load('plusblue.gif')
    images['diamondRed'] = __load('plusred.gif')

    images['diamondVertical'] = __load('diamondvertical.gif')
    images['diamondVerticalBlue'] = __load('verticalblue.gif')
    images['diamondVerticalRed'] = __load('verticalred.gif')

    images['diamondHorizontal'] = __loadTransposed('diamondvertical.gif', PI.ROTATE_90)
    images['diamondHorizontalBlue'] = __loadTransposed('verticalblue.gif', PI.ROTATE_90)
    images['diamondHorizontalRed'] = __loadTransposed('verticalred.gif', PI.ROTATE_90)

    images['plus'] = __load('plus.gif')
    images['plusBlue'] = __load('plusblue.gif')
    images['plusRed'] = __load('plusred.gif')

    images['vertical'] = __load('vertical.gif')
    images['verticalBlue'] = __load('verticalblue.gif')
    images['verticalRed'] = __load('verticalred.gif')

    images['horizontal'] = __loadTransposed('vertical.gif', PI.ROTATE_90)
    images['horizontalBlue'] = __loadTransposed('verticalblue.gif', PI.ROTATE_90)
    images['horizontalRed'] = __loadTransposed('verticalred.gif', PI.ROTATE_90)

    images['tNorth'] = __load('t.gif')
    images['tNorthBlue'] = __load('tblue.gif')
    images['tNorthRed'] = __load('tred.gif')

    images['tSouth'] = __loadTransposed('t.gif', PI.FLIP_TOP_BOTTOM)
    images['tSouthBlue'] = __loadTransposed('tblue.gif', PI.FLIP_TOP_BOTTOM)
    images['tSouthRed'] = __loadTransposed('tred.gif', PI.FLIP_TOP_BOTTOM)

    images['tEast'] = __loadTransposed('t.gif', PI.ROTATE_270)
    images['tEastBlue'] = __loadTransposed('tblue.gif', PI.ROTATE_270)
    images['tEastRed'] = __loadTransposed('tred.gif', PI.ROTATE_270)

    images['tWest'] = __loadTransposed('t.gif', PI.ROTATE_90)
    images['tWestBlue'] = __loadTransposed('tblue.gif', PI.ROTATE_90)
    images['tWestRed'] = __loadTransposed('tred.gif', PI.ROTATE_90)

    images['tNorthBold'] = __load('tbold.gif')
    images['tNorthBoldBlue'] = __load('tboldblue.gif')
    images['tNorthBoldRed'] = __load('tboldred.gif')

    images['tSouthBold'] = __loadTransposed('tbold.gif', PI.FLIP_TOP_BOTTOM)
    images['tSouthBoldBlue'] = __loadTransposed('tboldblue.gif', PI.FLIP_TOP_BOTTOM)
    images['tSouthBoldRed'] = __loadTransposed('tboldred.gif', PI.FLIP_TOP_BOTTOM)

    images['tEastBold'] = __loadTransposed('tbold.gif', PI.ROTATE_270)
    images['tEastBoldBlue'] = __loadTransposed('tboldblue.gif', PI.ROTATE_270)
    images['tEastBoldRed'] = __loadTransposed('tboldred.gif', PI.ROTATE_270)

    images['tWestBold'] = __loadTransposed('tbold.gif', PI.ROTATE_90)
    images['tWestBoldBlue'] = __loadTransposed('tboldblue.gif', PI.ROTATE_90)
    images['tWestBoldRed'] = __loadTransposed('tboldred.gif', PI.ROTATE_90)

    images['cornerNorthwest'] = __load('corner.gif')
    images['cornerNorthwestBlue'] = __load('cornerBlue.gif')
    images['cornerNorthwestRed'] = __load('cornerRed.gif')

    images['cornerNortheast'] = __loadTransposed('corner.gif', PI.FLIP_LEFT_RIGHT)
    images['cornerNortheastBlue'] = __loadTransposed('cornerBlue.gif', PI.FLIP_LEFT_RIGHT)
    images['cornerNortheastRed'] = __loadTransposed('cornerRed.gif', PI.FLIP_LEFT_RIGHT)

    images['cornerSouthwest'] = __loadTransposed('corner.gif', PI.FLIP_TOP_BOTTOM)
    images['cornerSouthwestBlue'] = __loadTransposed('cornerBlue.gif', PI.FLIP_TOP_BOTTOM)
    images['cornerSouthwestRed'] = __loadTransposed('cornerRed.gif', PI.FLIP_TOP_BOTTOM)

    images['cornerSoutheast'] = __loadTransposed('corner.gif', PI.ROTATE_180)
    images['cornerSoutheastBlue'] = __loadTransposed('cornerBlue.gif', PI.ROTATE_180)
    images['cornerSoutheastRed'] = __loadTransposed('cornerRed.gif', PI.ROTATE_180)

    return images


def __load(gif):
    image = PI.open(gif)
    return ImageTk.PhotoImage(image)


def __loadTransposed(gif, transposition):
    image = PI.open(gif)
    return ImageTk.PhotoImage(image.transpose(transposition))
