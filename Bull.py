class Bull:
    def __init__(self, flux, test_size):
        self._flux = flux
        self._test_size = test_size

    def get_flux(self):
        return self._flux

    def get_size(self):
        return self._test_size

    def set_flux(self, new_flux):
        self._flux = new_flux

    def set_size(self, new_size):
        self._test_size = new_size