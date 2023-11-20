package org.tpokora.wh40karmyorganizer.domain.port;

import org.tpokora.wh40karmyorganizer.domain.model.Collection;

import java.util.List;

public interface CollectionPersistencePort {

    List<Collection> getAll();
    void save(Collection collection);
    Collection getByName(String name);
    void deleteByName(String name);

    Collection update(Collection existingCollection, Collection updatedCollection);

}
