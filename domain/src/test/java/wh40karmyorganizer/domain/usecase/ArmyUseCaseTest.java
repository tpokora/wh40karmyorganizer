package wh40karmyorganizer.domain.usecase;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.service.ArmyService;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;
import wh40karmyorganizer.domain.inmemory.TestInMemoryPersistencePort;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

class ArmyUseCaseTest {

    public static final String TEST_ARMY_NAME = "test_army";
    private ArmyUseCase armyUseCase;
    private TestInMemoryPersistencePort testInMemoryPersistencePort;

    @BeforeEach
    void setup() {
        this.testInMemoryPersistencePort = new TestInMemoryPersistencePort();
        this.armyUseCase = new ArmyService(this.testInMemoryPersistencePort);
    }

    @AfterEach
    void teardown() {
        this.testInMemoryPersistencePort.clearStorage();
    }

    @Test
    void shouldReturnAllArmies() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);
        this.testInMemoryPersistencePort.save(testArmy);

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
        var army = this.testInMemoryPersistencePort.getArmyByName(testArmy.name());
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
        this.testInMemoryPersistencePort.save(testArmy);

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
        this.testInMemoryPersistencePort.save(testArmy);
        var updatedArmyName = new Army("updated_test_army");

        // when
        this.armyUseCase.update(testArmy, updatedArmyName);

        // then
        var expectedArmy = this.armyUseCase.getByName(updatedArmyName.name());
        assertThat(expectedArmy).isNotNull();
    }
}