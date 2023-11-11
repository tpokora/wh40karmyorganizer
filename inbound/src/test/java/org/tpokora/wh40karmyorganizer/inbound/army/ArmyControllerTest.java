package org.tpokora.wh40karmyorganizer.inbound.army;

import com.fasterxml.jackson.databind.ObjectMapper;
import org.junit.jupiter.api.Test;
import org.mockito.Mockito;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.autoconfigure.web.servlet.AutoConfigureMockMvc;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.boot.test.mock.mockito.MockBean;
import org.springframework.http.MediaType;
import org.springframework.test.web.servlet.MockMvc;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;

import java.util.List;

import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.get;
import static org.springframework.test.web.servlet.request.MockMvcRequestBuilders.post;
import static org.springframework.test.web.servlet.result.MockMvcResultMatchers.status;

@SpringBootTest
@AutoConfigureMockMvc
class ArmyControllerTest {

    private static final String TEST_ARMY = "test_army";
    private static final String ARMY_API_URL = "/api/army";

    @Autowired
    private MockMvc mockMvc;

    @MockBean
    private ArmyUseCase armyService;

    @Test
    void shouldReturnAllArmiesWithStatusCode200() throws Exception {
        // given
        Army testArmy = new Army(TEST_ARMY);

        // when
        Mockito.when(armyService.getAll()).thenReturn(List.of(testArmy));

        // then
        mockMvc.perform(get(ARMY_API_URL).contentType(MediaType.APPLICATION_JSON))
                .andExpect(status().isOk());
    }

    @Test
    void shouldSaveArmyAndReturnWitStatusCode201() throws Exception {
        // given
        Army testArmy = new Army(TEST_ARMY);

        // then
        mockMvc.perform(post(ARMY_API_URL)
                .contentType(MediaType.APPLICATION_JSON)
                .content(new ObjectMapper().writeValueAsString(testArmy)))
                .andExpect(status().isCreated());
    }
}