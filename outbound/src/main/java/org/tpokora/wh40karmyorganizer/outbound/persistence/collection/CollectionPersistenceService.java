package org.tpokora.wh40karmyorganizer.outbound.persistence.collection;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.stereotype.Service;
import org.tpokora.wh40karmyorganizer.domain.model.Collection;
import org.tpokora.wh40karmyorganizer.domain.port.CollectionPersistencePort;

import java.util.List;

@Slf4j
@Service
@RequiredArgsConstructor
public class CollectionPersistenceService implements CollectionPersistencePort {

    @Override
    public List<Collection> getAll() {
        throw new UnsupportedOperationException();
    }

    @Override
    public void save(Collection collection) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Collection getByName(String name) {
        throw new UnsupportedOperationException();
    }

    @Override
    public void deleteByName(String name) {
        throw new UnsupportedOperationException();
    }

    @Override
    public Collection update(Collection existingCollection, Collection updatedCollection) {
        throw new UnsupportedOperationException();
    }
}
