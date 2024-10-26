from app.crusade.crusade import Crusade


def test_new_faction():
    # give
    name = "ArmyName"
    faction = "Faction"

    # when
    crusade = Crusade(name, faction)

    # then
    assert crusade.name == name
    assert crusade.faction == faction