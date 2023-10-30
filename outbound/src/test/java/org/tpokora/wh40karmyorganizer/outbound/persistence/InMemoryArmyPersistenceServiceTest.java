package org.tpokora.wh40karmyorganizer.outbound.persistence;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.tpokora.wh40karmyorganizer.domain.model.Army;

import java.util.List;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;


class InMemoryArmyPersistenceServiceTest {

    private InMemoryArmyPersistenceService inMemoryArmyPersistenceService;

    @BeforeEach
    void setup() {
        this.inMemoryArmyPersistenceService = new InMemoryArmyPersistenceService();
    }

    @AfterEach
    void teardown() {
        this.inMemoryArmyPersistenceService.clearStorage();
    }


    @Test
    void shouldReturnAllArmies() {
        // given
        var testArmy = new Army("test_army");
        this.inMemoryArmyPersistenceService.save(testArmy);

        // when
        var allArmies = this.inMemoryArmyPersistenceService.getAllArmies();

        // then
        assertThat(allArmies.size()).isEqualTo(1);
        assertThat(allArmies.stream()
                .anyMatch(army -> army.name().equals(testArmy.name()))).isTrue();
    }

    @Test
    void shouldReturnArmyByName() {
        // given
        var testArmy = new Army("test_army");
        this.inMemoryArmyPersistenceService.save(testArmy);

        // when
        var army = this.inMemoryArmyPersistenceService.getArmy(testArmy.name());

        // then
        assertThat(army).isPresent();
        army.ifPresent(value -> assertThat(value.name()).isEqualTo(testArmy.name()));
    }

}