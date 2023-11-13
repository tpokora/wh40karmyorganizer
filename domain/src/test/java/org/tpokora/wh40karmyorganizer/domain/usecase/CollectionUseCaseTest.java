package org.tpokora.wh40karmyorganizer.domain.usecase;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import org.tpokora.wh40karmyorganizer.domain.inmemory.TestInMemoryCollectionPersistencePort;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.model.Collection;
import org.tpokora.wh40karmyorganizer.domain.service.CollectionService;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;

class CollectionUseCaseTest {

    private static final String TEST_ARMY_NAME = "test_army";
    private static final Army TEST_ARMY = new Army(TEST_ARMY_NAME);
    private static final String TEST_COLLECTION_NAME = "test_collection";

    private CollectionUseCase collectionUseCase;
    private TestInMemoryCollectionPersistencePort testInMemoryCollectionPersistencePort;

    @BeforeEach
    void setup() {
        this.testInMemoryCollectionPersistencePort = new TestInMemoryCollectionPersistencePort();
        this.collectionUseCase = new CollectionService(this.testInMemoryCollectionPersistencePort);
    }

    @AfterEach
    void teardown() {
        this.testInMemoryCollectionPersistencePort.clearStorage();
    }

    @Test
    void shouldSaveCollection() {
        // given
        var collection = new Collection(TEST_COLLECTION_NAME, TEST_ARMY);

        // when
        this.collectionUseCase.save(collection);

        // then
        var expectedCollection = this.testInMemoryCollectionPersistencePort.getByName(TEST_COLLECTION_NAME);
        assertThat(expectedCollection.name()).isEqualTo(collection.name());
    }

    @Test
    void shouldReturnCollectionByName() {
        // given
        var collection = new Collection(TEST_COLLECTION_NAME, TEST_ARMY);
        this.testInMemoryCollectionPersistencePort.save(collection);

        // when
        var expectedCollection = this.collectionUseCase.getByName(TEST_COLLECTION_NAME);

        // then
        assertThat(expectedCollection).isNotNull();
        assertThat(expectedCollection.name()).isEqualTo(collection.name());
    }
}