from datetime import date


class Head:
    def __init__(self, num, sex, speceis, general, sector, medical_records, alive, age, birth_date, death_date):
        self._num = num
        self._sex = sex
        self._speceis = speceis
        self._general = general
        self._sector = sector
        self._medical_records = medical_records
        self._alive = alive
        self._age = age
        self._birth_date = birth_date
        self._death_date = death_date

    # getters:

    def get_num(self):
        return self._num

    def get_sex(self):
        return self._sex

    def get_speceis(self):
        return self._speceis

    def get_general(self):
        return self._general

    def get_sector(self):
        return self._sector

    def get_medical_records(self):
        return self._medical_records

    def get_alive(self):
        return self._alive

    def get_age(self):
        return self._age

    def get_birth_date(self):
        return self._birth_date

    def get_death_date(self):
        return self._death_date

    # setters:

    def set_num(self, new_num):
        self._num = new_num

    def set_sex(self, new_sex):
        self._sex = new_sex

    def set_speceis(self, new_speceis):
        self._speceis = new_speceis

    def set_general(self):
        self._general += "\n" + input()

    def set_sector(self, new_sector):
        self._sector = new_sector

    def set_medical_records(self):
        self._medical_records.update()

    def set_alive(self, alive_or_dead):
        self._alive = alive_or_dead

    def set_age(self):
        self._age = date.today() - self._birth_date

    def set_birth_date(self, birthday):
        self._birth_date = birthday

    def set_death_date(self, sweet_realse):
        self._death_date = sweet_realse
