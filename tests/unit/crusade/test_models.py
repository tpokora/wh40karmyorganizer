from app.crusade.crusade import Crusade


def test_new_faction():
    # give
    crusade_force = "Crusade Force"
    faction = "Faction"

    # when
    crusade = Crusade(crusade_force, faction)

    # then
    assert crusade.name == crusade_force
    assert crusade.faction == faction