package org.tpokora.wh40karmyorganizer.domain.usecase;

import org.tpokora.wh40karmyorganizer.domain.model.Collection;

import java.util.List;

public interface CollectionUseCase {

    List<Collection> getAll();
    void save(Collection collection);
    Collection getByName(String name);

    void delete(String name);

    Collection update(Collection existingCollection, Collection updatedCollection);

}
