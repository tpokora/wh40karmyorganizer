from app.army.army import Army


def test_new_army():
    # give
    name = "ArmyName"
    faction = "Faction"

    # when
    army = Army(name, faction)

    # then
    assert army.name == name
    assert army.faction == faction