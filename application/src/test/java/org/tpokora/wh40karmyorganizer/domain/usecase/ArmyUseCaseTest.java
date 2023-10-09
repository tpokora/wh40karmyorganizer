package org.tpokora.wh40karmyorganizer.domain.usecase;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.service.ArmyService;

import java.util.List;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

class ArmyUseCaseTest {

    private ArmyUseCase armyUseCase;

    @BeforeEach
    void setup() {
        this.armyUseCase = new ArmyService();
    }

    @Test
    void shouldReturnAllArmies() {
        // given

        // when
        List<Army> allArmies = this.armyUseCase.getAllArmies();

        // then
        assertThat(allArmies.size()).isEqualTo(1);
        assertThat(allArmies.get(0).name()).isEqualTo("romper");
    }
}