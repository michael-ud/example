from grocer.sides.eggs import eggs
from grocer.sides.bacon import bacon


def bacon_and_eggs():
    return '%s and %s' % (bacon(), eggs(),)
