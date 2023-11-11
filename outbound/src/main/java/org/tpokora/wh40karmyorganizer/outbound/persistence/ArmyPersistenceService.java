package org.tpokora.wh40karmyorganizer.outbound.persistence;

import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyAlreadyExistException;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyNotExistException;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.port.PersistencePort;

import java.util.List;
import java.util.Optional;

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
        if (checkIfArmyExists(army)) {
            throw new ArmyAlreadyExistException(army.name());
        }
        armyRepository.save(toEntity(army));
    }


    @Override
    public Army update(Army existingArmy, Army updatedArmy) {
        var armyByName = armyRepository.findByName(existingArmy.name())
                .orElseThrow(() -> new ArmyNotExistException(existingArmy.name()));
        if (checkIfArmyExists(updatedArmy)) {
            throw new ArmyAlreadyExistException(updatedArmy.name());
        }
        updateArmyEntity(armyByName, updatedArmy);
        this.armyRepository.save(armyByName);
        return toArmy(armyByName);
    }

    public void delete(Army army) {
        armyRepository.findByName(army.name())
                .ifPresentOrElse(
                        armyRepository::delete,
                        () -> {
                            throw new ArmyNotExistException(army.name());
                        });
    }

    private void updateArmyEntity(ArmyEntity existingArmy, Army updatedArmy) {
        existingArmy.setName(updatedArmy.name());
    }

    private boolean checkIfArmyExists(Army army) {
        return armyRepository.existsArmyEntityByName(army.name());
    }

    private Army toArmy(ArmyEntity armyEntity) {
        return new Army(armyEntity.getName());
    }

    private ArmyEntity toEntity(Army army) {
        return new ArmyEntity(army.name());
    }
}
