package org.tpokora.wh40karmyorganizer.inbound.army;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;

import java.util.List;

@Slf4j
@RestController
@RequiredArgsConstructor
public class ArmyController {

    private final ArmyUseCase armyUseCase;

    @GetMapping(value = "/api/army", produces = "application/json")
    public ResponseEntity<List<Army>> getAllArmies() {
        log.info("Retrieve all Armies");
        List<Army> allArmies = armyUseCase.getAllArmies();
        return new ResponseEntity<>(allArmies, HttpStatus.OK);
    }
}
