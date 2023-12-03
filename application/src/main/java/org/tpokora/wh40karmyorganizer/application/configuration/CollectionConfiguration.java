package org.tpokora.wh40karmyorganizer.application.configuration;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.tpokora.wh40karmyorganizer.domain.port.CollectionPersistencePort;
import org.tpokora.wh40karmyorganizer.domain.service.CollectionService;
import org.tpokora.wh40karmyorganizer.domain.usecase.CollectionUseCase;

@Configuration
public class CollectionConfiguration {

    @Bean
    public CollectionUseCase collectionService(final CollectionPersistencePort collectionPersistencePort) {
        return new CollectionService(collectionPersistencePort);
    }
}
