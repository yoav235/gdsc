import Head, typing, Mom


class Calf(Head):
    def __init__(self, dad, mom: Mom, pic, weaned):
        self._dad = dad
        self._mom = mom
        self._pic = pic
        self._is_weaned = weaned

    def get_dad(self):
        return self._dad

    def get_mom(self):
        return self._mom

    def get_pic(self):
        return self._pic

    def get_weaned(self):
        return self._weaned

    def calf_weaned(self):
        self._is_weaned = True
        self._mom.set_weaned(self._mom.get_weaned() + 1)

