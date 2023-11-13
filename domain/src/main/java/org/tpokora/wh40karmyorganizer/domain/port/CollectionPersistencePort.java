package org.tpokora.wh40karmyorganizer.domain.port;

import org.tpokora.wh40karmyorganizer.domain.model.Collection;

public interface CollectionPersistencePort {

    void save(Collection collection);
    Collection getByName(String name);
}
