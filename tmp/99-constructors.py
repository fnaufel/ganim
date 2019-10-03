
class A(object):

    def __init__(self):

        print('Initializing A...')
        print('x =', self.x)
        print('Done initializing A.')


class B(A):

    def __init__(self):

        print('Initializing B...')

        self.x = 1

        super(B, self).__init__()

        print('Done initializing B.')


b = B()
