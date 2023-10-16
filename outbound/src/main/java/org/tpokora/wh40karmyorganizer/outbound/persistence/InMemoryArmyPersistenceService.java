package org.tpokora.wh40karmyorganizer.outbound.persistence;

import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.port.PersistencePort;

import java.util.LinkedList;
import java.util.List;
import java.util.Optional;

@Slf4j
@Service
public class InMemoryArmyPersistenceService implements PersistencePort {

    private static final LinkedList<Army> STORAGE = new LinkedList<>();

    @Override
    public List<Army> getAllArmies() {
        return STORAGE;
    }

    @Override
    public void save(Army army) {
        STORAGE.add(army);
    }

    @Override
    public Optional<Army> getArmy(String name) {
        return STORAGE.stream()
                .filter(army -> army.name().equals(name))
                .findFirst();
    }

    public void clearStorage() {
        STORAGE.clear();
    }
}
