package org.tpokora.wh40karmyorganizer.inbound.army;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RestController;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;

import java.util.List;

@Slf4j
@RestController
@RequiredArgsConstructor
public class ArmyController {

    private final ArmyUseCase armyUseCase;

    @GetMapping(value = "/api/army", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<List<Army>> getAllArmies() {
        log.info(">>> Retrieve all Armies");
        List<Army> allArmies = armyUseCase.getAll();
        return ResponseEntity.ok(allArmies);
    }

    @PostMapping(value = "/api/army", consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> saveArmy(@RequestBody Army army) {
        log.info(">>> Save army: {}", army);
        armyUseCase.save(army);
        return new ResponseEntity<>(HttpStatus.CREATED);
    }
}
