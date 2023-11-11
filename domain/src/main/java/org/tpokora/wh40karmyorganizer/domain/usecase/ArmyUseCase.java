package org.tpokora.wh40karmyorganizer.domain.usecase;


import org.tpokora.wh40karmyorganizer.domain.model.Army;

import java.util.List;

public interface ArmyUseCase {

    List<Army> getAll();

    void save(Army army);
    
    Army getByName(String name);
    
    void delete(String name);
}
