package org.tpokora.wh40karmyorganizer.domain.usecase;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.tpokora.wh40karmyorganizer.domain.inmemory.TestInMemoryArmyPersistencePort;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.service.ArmyService;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

class ArmyUseCaseTest {

    private static final String TEST_ARMY_NAME = "test_army";
    private ArmyUseCase armyUseCase;
    private TestInMemoryArmyPersistencePort testInMemoryArmyPersistencePort;

    @BeforeEach
    void setup() {
        this.testInMemoryArmyPersistencePort = new TestInMemoryArmyPersistencePort();
        this.armyUseCase = new ArmyService(this.testInMemoryArmyPersistencePort);
    }

    @AfterEach
    void teardown() {
        this.testInMemoryArmyPersistencePort.clearStorage();
    }

    @Test
    void shouldReturnAllArmies() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);
        this.testInMemoryArmyPersistencePort.save(testArmy);

        // when
        var allArmies = this.armyUseCase.getAll();

        // then
        assertThat(allArmies.size()).isEqualTo(1);
        assertThat(allArmies.get(0).name()).isEqualTo(testArmy.name());
    }

    @Test
    void shouldSaveArmy() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);

        // when
        this.armyUseCase.save(testArmy);

        // then
        var army = this.testInMemoryArmyPersistencePort.getByName(testArmy.name());
        assertThat(army.name()).isEqualTo(testArmy.name());
    }

    @Test
    void shouldDeleteArmy() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);
        this.armyUseCase.save(testArmy);

        // when
        assertThat(this.armyUseCase.getAll().isEmpty()).isFalse();
        this.armyUseCase.delete(testArmy.name());

        // expected
        assertThat(this.armyUseCase.getAll().isEmpty()).isTrue();
    }

    @Test
    void shouldReturnArmyByName() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);
        this.testInMemoryArmyPersistencePort.save(testArmy);

        // when
        var expectedArmy = this.armyUseCase.getByName(TEST_ARMY_NAME);

        // then
        assertThat(expectedArmy).isNotNull();
        assertThat(expectedArmy.name()).isEqualTo(testArmy.name());
    }

    @Test
    void shouldUpdateArmy() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);
        this.testInMemoryArmyPersistencePort.save(testArmy);
        var updatedArmyName = new Army("updated_test_army");

        // when
        this.armyUseCase.update(testArmy, updatedArmyName);

        // then
        var expectedArmy = this.armyUseCase.getByName(updatedArmyName.name());
        assertThat(expectedArmy).isNotNull();
    }
}