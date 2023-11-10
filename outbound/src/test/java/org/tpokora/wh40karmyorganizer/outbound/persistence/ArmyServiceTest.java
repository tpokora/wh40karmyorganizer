package org.tpokora.wh40karmyorganizer.outbound.persistence;

import org.junit.jupiter.api.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.PostgreSQLContainer;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.outbound.persistence.entity.ArmyEntity;

import java.util.List;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

@SpringBootTest
class ArmyServiceTest {

    private static final String TEST_ARMY_NAME = "test_army";
    private static final String NOT_EXISTING_ARMY = "NOT_EXISTING_ARMY";
    static PostgreSQLContainer<?> postgres = new PostgreSQLContainer<>(
            "postgres:15-alpine"
    );

    @DynamicPropertySource
    static void configureProperties(DynamicPropertyRegistry registry) {
        registry.add("spring.datasource.url", () -> postgres.getJdbcUrl().replaceFirst("jdbc", "jdbc:tc"));
        registry.add("spring.datasource.username", postgres::getUsername);
        registry.add("spring.datasource.password", postgres::getPassword);
    }

    @Autowired
    private ArmyRepository armyRepository;

    private ArmyService armyService;

    @BeforeAll
    static void beforeAll() {
        postgres.start();
    }

    @AfterAll
    static void afterAll() {
        postgres.stop();
    }

    @BeforeEach
    void setUp() {
        armyRepository.deleteAll();
        armyService = new ArmyService(armyRepository);
    }

    @Test
    void shouldReturnAllArmies() {
        // given
        var testArmy1 = new ArmyEntity("test_army1");
        var testArmy2 = new ArmyEntity("test_army2");
        var armies = List.of(
                testArmy1,
                testArmy2);
        this.armyRepository.saveAll(armies);

        // when
        var allArmies = armyService.getAllArmies();

        // then
        assertThat(allArmies.size()).isEqualTo(2);
        assertThat(allArmies.stream()
                .filter(army -> army.name().equals(testArmy1.getName()))
                .findFirst()).isPresent();
        assertThat(allArmies.stream()
                .filter(army -> army.name().equals(testArmy2.getName()))
                .findFirst()).isPresent();
    }

    @Test
    void shouldReturnArmyByName() {
        // given
        var testArmy = new ArmyEntity(TEST_ARMY_NAME);
        this.armyRepository.save(testArmy);

        // when
        var expectedArmy = this.armyService.getArmyByName(testArmy.getName());

        // then
        assertThat(expectedArmy.name()).isEqualTo(testArmy.getName());
    }

    @Test
    void shouldThrowExceptionIfArmyDoesNotExist() {
        // expect
        Assertions.assertThrows(ArmyNotExistException.class, () -> this.armyService.getArmyByName(NOT_EXISTING_ARMY));
    }

    @Test
    void shouldSaveArmy() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);

        // when
        this.armyService.save(testArmy);
        var expectedArmy = this.armyService.getArmyByName(testArmy.name());

        // then
        assertThat(expectedArmy.name()).isEqualTo(testArmy.name());
    }

    @Test
    void shouldThrowExceptionIfArmyAlreadyExists() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);
        this.armyRepository.save(toEntity(testArmy));

        // expect
        Assertions.assertThrows(ArmyAlreadyExistException.class, () -> this.armyService.save(testArmy));
    }

    @Test
    void shouldDeleteArmy() {
        // given
        var testArmy = new Army(TEST_ARMY_NAME);
        this.armyRepository.save(toEntity(testArmy));

        // when
        this.armyService.delete(testArmy);

        // then
        Assertions.assertThrows(ArmyNotExistException.class, () -> this.armyService.getArmyByName(TEST_ARMY_NAME));
    }

    @Test
    void shouldThrowExceptionIfArmyToDeleteDoesNotExist() {
        // given
        var testArmy = new Army(NOT_EXISTING_ARMY);

        // expect
        Assertions.assertThrows(ArmyNotExistException.class, () -> this.armyService.delete(testArmy));
    }

    private ArmyEntity toEntity(Army army) {
        return new ArmyEntity(army.name());
    }
}