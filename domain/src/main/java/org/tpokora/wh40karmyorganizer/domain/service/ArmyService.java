package org.tpokora.wh40karmyorganizer.domain.service;

import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;

import java.util.Arrays;
import java.util.List;

public class ArmyService implements ArmyUseCase {

    @Override
    public List<Army> getAllArmies() {
        return Arrays.asList(new Army("romper"));
    }
}
