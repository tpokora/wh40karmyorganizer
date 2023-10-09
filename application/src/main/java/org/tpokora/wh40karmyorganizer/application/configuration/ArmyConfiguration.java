package org.tpokora.wh40karmyorganizer.application.configuration;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.tpokora.wh40karmyorganizer.domain.service.ArmyService;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;

@Configuration
public class ArmyConfiguration {

    @Bean
    public ArmyUseCase armyService() {
        return new ArmyService();
    }
}
