from app.crusade.crusade import Crusade

import hashlib

def test_new_crusade_force():
    # give
    crusade_id = hashlib.md5("crusade_force2".encode('utf-8')).hexdigest()
    crusade_force = "Crusade Force"
    faction = "Faction"
    supply_limit = 1000

    # when
    crusade = Crusade(crusade_id, crusade_force, faction, supply_limit)

    # then
    assert crusade.crusade_id == crusade_id
    assert crusade.crusade_force == crusade_force
    assert crusade.faction == faction
    assert crusade.supply_limit == 1000
    assert crusade.supply_used == 0
