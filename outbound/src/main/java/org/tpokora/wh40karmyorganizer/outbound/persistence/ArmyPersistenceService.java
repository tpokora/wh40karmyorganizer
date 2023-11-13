package org.tpokora.wh40karmyorganizer.outbound.persistence;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyAlreadyExistException;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyNotExistException;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.port.PersistencePort;

import java.util.List;

@Slf4j
@Service
@RequiredArgsConstructor
public class ArmyPersistenceService implements PersistencePort {

    private static final String ARMY_DOES_NOT_EXIST_ERROR_MSG = ">> Army {}, does not exist";
    private static final String ARMY_ALREADY_EXISTS_ERROR_MSG = ">> Army {}, already exists";

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
                .orElseThrow(() -> {
                    log.error(ARMY_DOES_NOT_EXIST_ERROR_MSG, name);
                    return new ArmyNotExistException(name);
                });
    }

    @Override
    public void delete(String name) {
        throw new UnsupportedOperationException();
    }

    public void save(Army army) {
        if (checkIfArmyExists(army)) {
            log.error(ARMY_ALREADY_EXISTS_ERROR_MSG, army.name());
            throw new ArmyAlreadyExistException(army.name());
        }
        armyRepository.save(toEntity(army));
    }


    @Override
    public Army update(Army existingArmy, Army updatedArmy) {
        var armyByName = armyRepository.findByName(existingArmy.name())
                .orElseThrow(() -> new ArmyNotExistException(existingArmy.name()));
        if (checkIfArmyExists(updatedArmy)) {
            log.error(ARMY_ALREADY_EXISTS_ERROR_MSG, updatedArmy.name());
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
                            log.error(ARMY_DOES_NOT_EXIST_ERROR_MSG, army.name());
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
