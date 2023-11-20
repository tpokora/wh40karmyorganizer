package org.tpokora.wh40karmyorganizer.domain.inmemory;

import org.tpokora.wh40karmyorganizer.domain.exception.CollectionAlreadyExistException;
import org.tpokora.wh40karmyorganizer.domain.exception.CollectionNotExistException;
import org.tpokora.wh40karmyorganizer.domain.model.Collection;
import org.tpokora.wh40karmyorganizer.domain.port.CollectionPersistencePort;

import java.util.LinkedList;
import java.util.List;

public class TestInMemoryCollectionPersistencePort implements CollectionPersistencePort {

    private static final LinkedList<Collection> STORAGE = new LinkedList<>();

    @Override
    public List<Collection> getAll() {
        return STORAGE;
    }

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

    @Override
    public void deleteByName(String name) {
        var collection = getByName(name);
        STORAGE.remove(collection);
    }

    public void clearStorage() {
        STORAGE.clear();
    }

    @Override
    public Collection update(Collection existingCollection, Collection updatedCollection) {
        getByName(existingCollection.name());
        if (STORAGE.stream()
                .anyMatch(collection ->
                        collection.name().equals(updatedCollection.name()))) {
            throw new CollectionAlreadyExistException(updatedCollection.name());
        }
        deleteByName(existingCollection.name());
        save(updatedCollection);
        return updatedCollection;
    }
}
