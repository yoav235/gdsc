import Head, Calf, datetime


class Mom(Head):
    def __init__(self, offsprings: list, matriarch, seasons, pregnancies, miscarriages, tough_births,
                 weaned, udder_score, last_conception_date):
        self._offsprings = offsprings
        self._first_time = seasons <= 1
        self._matriarch = matriarch
        self._pregnancies = pregnancies
        self._seasons = seasons
        self._miscarriages = miscarriages
        self._tough_births = tough_births
        self._weaned = weaned
        self._udder_score = udder_score
        self._last_conception_date = last_conception_date
        self._conception_ratio = self._pregnancies / self._seasons
        self._birth_ratio = len(self._offsprings) / self._pregnancies
        self._weaning_ratio = self._weaned / len(self._offsprings)

    # getters:
    def get_offsprings(self):
        return self._offsprings

    def get_first_time(self):
        return self._first_time

    def get_matriarch(self):
        return self._matriarch

    def get_pregnancies(self):
        return self._pregnancies

    def get_seasons(self):
        return self._seasons

    def get_miscarriages(self):
        return self._miscarriages

    def get_tough_births(self):
        return self._tough_births

    def get_weaned(self):
        return self._weaned

    def get_udder_score(self):
        return self._udder_score

    def get_last_conception_date(self):
        return self._last_conception_date

    def get_birth_ratio(self):
        return self._birth_ratio

    def get_weaning_ratio(self):
        return self._weaning_ratio

    # setter:
    def add_offspring(self, calf: Calf):
        self._offsprings.append(calf)

    def set_weaned(self, weaned_num):
        self._weaned = weaned_num

    def set_udder_score(self, new_score):
        self._udder_score = new_score

    def set_matriarch(self, is_matriarch):
        self._matriarch = is_matriarch

    def set_conception_date(self, new_conception_date):
        self._last_conception_date = new_conception_date
        self._pregnancies += 1

    def set_miscarriages(self, new_miscarriages):
        self._miscarriages = new_miscarriages

    def set_tough_birth(self, new_tough):
        self._tough_births = new_tough

    def how_long_since_conception(self):
        return datetime.date.today() - self._last_conception_date






