package wh40karmyorganizer.domain.usecase;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.service.ArmyService;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;
import wh40karmyorganizer.domain.inmemory.TestInMemoryPersistencePort;

import java.util.List;
import java.util.Optional;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

class ArmyUseCaseTest {

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
        Army testArmy = new Army("test_army");
        this.testInMemoryPersistencePort.save(testArmy);

        // when
        List<Army> allArmies = this.armyUseCase.getAllArmies();

        // then
        assertThat(allArmies.size()).isEqualTo(1);
        assertThat(allArmies.get(0).name()).isEqualTo(testArmy.name());
    }

    @Test
    void shouldSaveArmy() {
        // given
        Army testArmy = new Army("test_army");

        // when
        this.armyUseCase.save(testArmy);

        // then
        Optional<Army> army = this.testInMemoryPersistencePort.getArmy(testArmy.name());
        assertThat(army).isPresent();
        army.ifPresent(value -> assertThat(value.name()).isEqualTo(testArmy.name()));

    }
}