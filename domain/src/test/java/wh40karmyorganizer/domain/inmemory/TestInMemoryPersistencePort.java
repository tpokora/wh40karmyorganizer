package wh40karmyorganizer.domain.inmemory;

import org.tpokora.wh40karmyorganizer.domain.exception.ArmyNotExistException;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.port.PersistencePort;

import java.util.LinkedList;
import java.util.List;

public class TestInMemoryPersistencePort implements PersistencePort {
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
    public Army getArmyByName(String name) {
        return STORAGE.stream()
                .filter(army -> army.name().equals(name))
                    .findFirst()
                    .orElseThrow(() -> new ArmyNotExistException(name));
    }

    @Override
    public void delete(String name) {

    }

    public void clearStorage() {
        STORAGE.clear();
    }
}
