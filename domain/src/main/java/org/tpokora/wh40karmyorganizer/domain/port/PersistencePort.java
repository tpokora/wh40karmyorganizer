package org.tpokora.wh40karmyorganizer.domain.port;

import org.tpokora.wh40karmyorganizer.domain.model.Army;

import java.util.List;
import java.util.Optional;

public interface PersistencePort {

    List<Army> getAllArmies();

    void save(Army army);

    Optional<Army> getArmy(String name);
}
