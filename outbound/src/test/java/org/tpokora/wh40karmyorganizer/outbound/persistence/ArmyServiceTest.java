package org.tpokora.wh40karmyorganizer.outbound.persistence;

import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.DynamicPropertyRegistry;
import org.springframework.test.context.DynamicPropertySource;
import org.testcontainers.containers.PostgreSQLContainer;
import org.tpokora.wh40karmyorganizer.outbound.persistence.entity.ArmyEntity;

import java.util.List;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

@SpringBootTest
class ArmyServiceTest {

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
    void getAllArmiesShouldReturnAllArmies() {
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
                .filter(armyEntity -> armyEntity.getName().equals(testArmy1.getName()))
                .findFirst()).isPresent();
        assertThat(allArmies.stream()
                .filter(armyEntity -> armyEntity.getName().equals(testArmy2.getName()))
                .findFirst()).isPresent();
    }
}