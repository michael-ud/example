from grocer.sides.eggs import eggs


def spam_and_eggs():
    return 'spam and %s with %s' % (eggs(), secret_sauce())


def secret_sauce():
    return 'secret sauce'
