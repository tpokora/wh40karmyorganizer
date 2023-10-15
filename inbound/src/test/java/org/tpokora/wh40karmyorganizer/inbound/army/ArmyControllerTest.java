package org.tpokora.wh40karmyorganizer.inbound.army;

import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.test.web.servlet.MockMvc;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;
import org.tpokora.wh40karmyorganizer.inbound.army.army.ArmyController;

import java.util.ArrayList;

import static org.springframework.http.MediaType.APPLICATION_JSON_VALUE;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.content;

@SpringBootTest(classes = ArmyController.class)
@AutoConfigureMockMvc
class ArmyControllerTest {

    private static final String TEST_ARMY = "test_army";
    private static final String ARMY_API_URL = "/api/army";

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private ArmyUseCase armyService;

    // #TODO: fix test
//    @Test
//    void shouldReturnAllArmiesWithStatusCode200() throws Exception {
//        // given
//        Army testArmy = new Army(TEST_ARMY);
//        ArrayList<Army> armies = new ArrayList<>();
//        armies.add(testArmy);
//
//        // when
//        Mockito.when(armyService.getAllArmies()).thenReturn(armies);
//
//        // then
//        mockMvc.perform(get(ARMY_API_URL)
//                        .contentType(APPLICATION_JSON_VALUE))
//                .andExpect(content().contentType(APPLICATION_JSON_VALUE));
////                .andExpect(status().isOk());
//    }
}