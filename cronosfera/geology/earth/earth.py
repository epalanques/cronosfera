from cronosfera.geology.earth.litosphere import Litosphere
from cronosfera.geology.earth.atmosphere import Atmosphere

class Earth:
    def __init__(self):
        self.atmosphere = {}  # {year: Atmosphere}
        self.litosphere = {}  # {year: Litosphere}
        self.short_description = ''

    def update_status(self, layer, year):
        if layer == 'litosphere':
            self.litosphere[year] = Litosphere()
            return self.litosphere[year]
        elif layer == 'atmosphere':
            self.atmosphere[year] = Atmosphere()
            return self.litosphere[year]
        else:
            raise NameError('layer "%s"not found' % layer)

    def get_info(self):
        # Earth no te nom, representa TOTA la terra... hauria d'agafar ... hauria d'agaf
        pass

    def get_registry(self):
        # todo: agafa tots el registres d'una època determinada.
        # Per defecte els agafa TOTS perque així, quan l'usuari rep una instancia de la terra en un
        # moment determinat, pot fer directament get_registry() sense haver de tornar a especificar
        # els anys.
        pass