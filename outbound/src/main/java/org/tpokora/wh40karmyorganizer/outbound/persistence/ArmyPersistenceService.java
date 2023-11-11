package org.tpokora.wh40karmyorganizer.outbound.persistence;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyAlreadyExistException;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyNotExistException;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.port.PersistencePort;

import java.util.List;

@Service
@RequiredArgsConstructor
public class ArmyPersistenceService implements PersistencePort {

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

    @Override
    public void delete(String name) {
        throw new UnsupportedOperationException();
    }

    public void save(Army army) {
        if (armyRepository.existsArmyEntityByName(army.name())) {
            throw new ArmyAlreadyExistException(army.name());
        }
        armyRepository.save(toEntity(army));
    }

    public void delete(Army army) {
        armyRepository.findByName(army.name())
                .ifPresentOrElse(
                        armyRepository::delete,
                        () -> {
                            throw new ArmyNotExistException(army.name());
                        });
    }

    private Army toArmy(ArmyEntity armyEntity) {
        return new Army(armyEntity.getName());
    }

    private ArmyEntity toEntity(Army army) {
        return new ArmyEntity(army.name());
    }
}
