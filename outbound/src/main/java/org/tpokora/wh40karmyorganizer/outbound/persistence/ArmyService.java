package org.tpokora.wh40karmyorganizer.outbound.persistence;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.tpokora.wh40karmyorganizer.outbound.persistence.entity.ArmyEntity;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ArmyService {

    private final ArmyRepository armyRepository;

    public List<ArmyEntity> getAllArmies() {
        return armyRepository.findAll();
    }
}
