package org.tpokora.wh40karmyorganizer.domain.port;

import org.tpokora.wh40karmyorganizer.domain.model.Army;

import java.util.List;

public interface ArmyPersistencePort {

    List<Army> getAll();

    void save(Army army);

    Army getByName(String name);

    void delete(String name);

    Army update(Army existingArmy, Army updatedArmy);
}
