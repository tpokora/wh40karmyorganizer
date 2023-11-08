package org.tpokora.wh40karmyorganizer.outbound.persistence;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.outbound.persistence.entity.ArmyEntity;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ArmyService {

    private final ArmyRepository armyRepository;

    public List<Army> getAllArmies() {
        return armyRepository.findAll()
                .stream()
                .map(this::toArmy)
                .toList();
    }

    public Army getArmyByName(String name) {
        return armyRepository.findByName(name)
                .map(this::toArmy)
                .orElseThrow(() -> new ArmyNotExistException(name));
    }

    public void save(Army army) {
        armyRepository.save(toEntity(army));
    }

    private Army toArmy(ArmyEntity armyEntity) {
        return new Army(armyEntity.getName());
    }

    private ArmyEntity toEntity(Army army) {
        return new ArmyEntity(army.name());
    }
}
