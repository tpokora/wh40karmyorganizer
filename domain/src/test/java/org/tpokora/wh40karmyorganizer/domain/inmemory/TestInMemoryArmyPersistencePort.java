package org.tpokora.wh40karmyorganizer.domain.inmemory;

import org.tpokora.wh40karmyorganizer.domain.exception.ArmyAlreadyExistException;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyNotExistException;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.port.ArmyPersistencePort;

import java.util.LinkedList;
import java.util.List;

public class TestInMemoryArmyPersistencePort implements ArmyPersistencePort {
    private static final LinkedList<Army> STORAGE = new LinkedList<>();

    @Override
    public List<Army> getAll() {
        return STORAGE;
    }

    @Override
    public void save(Army army) {
        STORAGE.add(army);
    }

    @Override
    public Army getByName(String name) {
        return STORAGE.stream()
                .filter(army -> army.name().equals(name))
                    .findFirst()
                    .orElseThrow(() -> new ArmyNotExistException(name));
    }

    @Override
    public void delete(String name) {
        var armyByName = getByName(name);
        STORAGE.remove(armyByName);
    }

    @Override
    public Army update(Army existingArmy, Army updatedArmy) {
        getByName(existingArmy.name());
        if (STORAGE.stream()
                .anyMatch(army -> army.name().equals(updatedArmy.name()))) {
            throw new ArmyAlreadyExistException(updatedArmy.name());
        }
        delete(existingArmy.name());
        save(updatedArmy);
        return updatedArmy;
    }


    public void clearStorage() {
        STORAGE.clear();
    }
}
