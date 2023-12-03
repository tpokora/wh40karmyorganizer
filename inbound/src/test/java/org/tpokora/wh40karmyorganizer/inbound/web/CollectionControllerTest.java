package org.tpokora.wh40karmyorganizer.inbound.web;

import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.model.Collection;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;
import org.tpokora.wh40karmyorganizer.domain.usecase.CollectionUseCase;


import java.util.List;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.*;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;
import static org.tpokora.wh40karmyorganizer.inbound.web.CollectionController.COLLECTION_API;

@SpringBootTest
@AutoConfigureMockMvc
class CollectionControllerTest {

    private static final String TEST_ARMY = "test_army";
    private static final String TEST_COLLECTION = "test_collection";

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private ArmyUseCase armyUseCase;

    @MockBean
    private CollectionUseCase collectionUseCase;

    @Test
    void shouldReturnAllCollectionsWithStatusCode200() throws Exception {
        // given
        var testArmy = new Army(TEST_ARMY);
        var testCollection = new Collection(TEST_COLLECTION, testArmy);

        // when
        Mockito.when(collectionUseCase.getAll()).thenReturn(List.of(testCollection));

        mockMvc.perform(get(COLLECTION_API).contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk());
    }
}