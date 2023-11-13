package org.tpokora.wh40karmyorganizer.domain.usecase;

import org.tpokora.wh40karmyorganizer.domain.model.Collection;

public interface CollectionUseCase {

    void save(Collection collection);
    Collection getByName(String name);


}
