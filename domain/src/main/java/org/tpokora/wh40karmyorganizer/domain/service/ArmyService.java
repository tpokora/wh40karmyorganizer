package org.tpokora.wh40karmyorganizer.domain.service;

import lombok.RequiredArgsConstructor;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.port.PersistencePort;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;

import java.util.List;

@RequiredArgsConstructor
public class ArmyService implements ArmyUseCase {

    private final PersistencePort persistencePort;

    @Override
    public List<Army> getAll() {
        return persistencePort.getAllArmies();
    }

    @Override
    public void save(Army army) {
        persistencePort.save(army);
    }

    @Override
    public Army getByName(String name) {
        return persistencePort.getArmyByName(name);
    }

    @Override
    public void delete(String name) {
        persistencePort.delete(name);
    }

    @Override
    public Army update(Army existingArmy, Army updatedArmy) {
        return persistencePort.update(existingArmy, updatedArmy);
    }
}
