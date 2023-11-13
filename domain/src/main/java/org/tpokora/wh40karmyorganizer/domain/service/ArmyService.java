package org.tpokora.wh40karmyorganizer.domain.service;

import lombok.RequiredArgsConstructor;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.port.ArmyPersistencePort;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;

import java.util.List;

@RequiredArgsConstructor
public class ArmyService implements ArmyUseCase {

    private final ArmyPersistencePort armyPersistencePort;

    @Override
    public List<Army> getAll() {
        return armyPersistencePort.getAll();
    }

    @Override
    public void save(Army army) {
        armyPersistencePort.save(army);
    }

    @Override
    public Army getByName(String name) {
        return armyPersistencePort.getByName(name);
    }

    @Override
    public void delete(String name) {
        armyPersistencePort.delete(name);
    }

    @Override
    public Army update(Army existingArmy, Army updatedArmy) {
        return armyPersistencePort.update(existingArmy, updatedArmy);
    }
}
