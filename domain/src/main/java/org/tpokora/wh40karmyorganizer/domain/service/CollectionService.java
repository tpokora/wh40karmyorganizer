package org.tpokora.wh40karmyorganizer.domain.service;

import lombok.RequiredArgsConstructor;
import org.tpokora.wh40karmyorganizer.domain.model.Collection;
import org.tpokora.wh40karmyorganizer.domain.port.CollectionPersistencePort;
import org.tpokora.wh40karmyorganizer.domain.usecase.CollectionUseCase;

@RequiredArgsConstructor
public class CollectionService implements CollectionUseCase {

    private final CollectionPersistencePort collectionPersistencePort;

    @Override
    public void save(Collection collection) {
        collectionPersistencePort.save(collection);
    }

    @Override
    public Collection getByName(String name) {
        return collectionPersistencePort.getByName(name);
    }
}
