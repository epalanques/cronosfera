from .manager import Manager
def main_script():

    earth = Manager()

    # todo: canviar lo del tipus de periode. fer que el retorni.
    # exemple:
    # >>> precambrico = time.add("precambrico", 2000,1000);
    # >>> precambrico.add("hadeico", 2000, 2800)
    # detecta automàticament si crea un eo o una era.

    earth.add('supereon', "Precámbrico", 4570000000, 542000000)

    earth.add_time("eon", "Hadeico", 4570000000, 3800000000)

    earth.add_geology("theia", "Earth and Theia collide", 4500000100)
    earth.add_geology("moon", "Moon formation", 4500000000)
    # todo: pensar manera d'incoporar eventos de l'espai (moon formation, pluja de meteorits...)

    zircon = earth.add_register("zircon", 4404000000)
    zircon.remarks = "Oldest found zircon"

    lith = earth.update_status("lithosphere", 4404000000)
    lith.ocean = "First oceans"

    earth.add("life", "earliest life on earth", 4280000000)

    # ----------------- EOARCHEAN --------------------- #

    earth.add_time("era", "eoarchean", 4000000000, 3600000000)

    lith = earth.update_status("litosphere", 4000000000)
    lith.status = "fully solid"
    lith.composition = ["maphic", "ultrampahic", "tonalite", "trondhjemite", "grandodiotie",
                        "chert", "BIF", "Subordinate clastic sedimentary rocks"]

    atm = earth.update_status("atmosphere", 4000000000)
    atm.pression = "10-100bars"
    atm.composition = "No O2"

    acasta = earth.add_register("Crustal Fragment", "Acasta Gneisses", 4000000000)
    acasta.composition = ["tonalite", "trondhjemite", "granodiorite", "amphibolite", "ultramaphic",
                          "pink granites"]
    acasta.location = "Canada"
    #todo: escriure la seva info file

    nap_com = earth.add_register("Crustal Fragment", "Napier Complex", 3900000000)
    nap_com.composition = ["tonalite", "trondhjemite", "granodiorite", "sedimentary protoliths"]
    nap_com.location = "Antartica"
    #todo: escriure la seva info file

    igc = earth.add_register("Crustal Fragment", "Itsaq Gneiss Complex", 3850000000)
    igc.composition = ["tonalite", "trondhjemite", "granodiorite"]
    igc.location = "Greenland"
    igc.remarks = "largest and best preserved eoarchean continental crust fragment"
    #todo: escriure la seva info file

    nsb = earth.add_register("Crustal Fragment", "Saglek-Hebron block", 3800000000)
    nsb.composition = ["supracrustal assemblage"]
    nsb.location = "Canada"
    #todo: escriure la seva info file

    nsb = earth.add_register("Crustal Fragment", "Nuvvuagittuq Supracrustal Belt", 3800000000)
    nsb.composition = ["Garnet paragneisses", "chemical sedmentary rocks", "volcanic rocks",
                       "magic tuff", "intermediate tuff"]
    nsb.location = "Canada"
    #todo: escriure la seva info file

    earth.add_time("eon", "Arcaico", 3800000000, 2500000000)
    earth.update_status("")

    earth.add_geology("craton", "Craton de Kaapval", 3800000000)
    earth.add_geology("craton", "Craton de Pilbara", 3800000000)
    earth.add_geology("craton", "Craton de Pilbara", 3800000000)

    earth.add_time("eon", "Proteozoico", 2500000000, 542000000)

    return earth
