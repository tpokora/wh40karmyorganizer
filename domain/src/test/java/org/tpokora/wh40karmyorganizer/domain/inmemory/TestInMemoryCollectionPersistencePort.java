package org.tpokora.wh40karmyorganizer.domain.inmemory;

import org.tpokora.wh40karmyorganizer.domain.exception.CollectionNotExistException;
import org.tpokora.wh40karmyorganizer.domain.model.Collection;
import org.tpokora.wh40karmyorganizer.domain.port.CollectionPersistencePort;

import java.util.LinkedList;

public class TestInMemoryCollectionPersistencePort implements CollectionPersistencePort {

    private static final LinkedList<Collection> STORAGE = new LinkedList<>();

    @Override
    public void save(Collection collection) {
        STORAGE.add(collection);
    }

    @Override
    public Collection getByName(String name) {
        return STORAGE.stream()
                .filter(collection -> collection.name().equals(name))
                .findFirst()
                .orElseThrow(() -> new CollectionNotExistException(name));
    }

    public void clearStorage() {
        STORAGE.clear();
    }
}
