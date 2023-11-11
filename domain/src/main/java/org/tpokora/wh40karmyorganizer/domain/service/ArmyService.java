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
        return null;
    }

    @Override
    public void delete(String name) {
        throw new UnsupportedOperationException();
    }
}
