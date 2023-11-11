package org.tpokora.wh40karmyorganizer.domain.port;

import org.tpokora.wh40karmyorganizer.domain.model.Army;

import java.util.List;

public interface PersistencePort {

    List<Army> getAllArmies();

    void save(Army army);

    Army getArmyByName(String name);

    void delete(String name);
}
