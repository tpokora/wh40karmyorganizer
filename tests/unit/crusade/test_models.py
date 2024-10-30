from app.crusade.crusade import Crusade


def test_new_crusade_force():
    # give
    crusade_force = "Crusade Force"
    faction = "Faction"
    supply_limit = 1000

    # when
    crusade = Crusade(crusade_force, faction, supply_limit)

    # then
    assert crusade.crusade_force == crusade_force
    assert crusade.faction == faction
    assert crusade.supply_limit == 1000
    assert crusade.supply_used == 0