package org.tpokora.wh40karmyorganizer.inbound.web;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.HttpStatus;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.tpokora.wh40karmyorganizer.domain.model.Army;
import org.tpokora.wh40karmyorganizer.domain.usecase.ArmyUseCase;

import java.util.List;

@Slf4j
@RestController
@RequiredArgsConstructor
public class ArmyController {

    public static final String ARMY_API = "/api/army";

    private final ArmyUseCase armyUseCase;

    @GetMapping(value = ARMY_API)
    public ResponseEntity<List<Army>> getAllArmies() {
        log.info(">>> Retrieve all Armies");
        return ResponseEntity.ok(armyUseCase.getAll());
    }

    @GetMapping(value = ARMY_API, params="name", produces = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Army> getArmyByName(@RequestParam("name") String name) {
        log.info(">>> Retrieve Army: {}", name);
        return ResponseEntity.ok(armyUseCase.getByName(name));
    }

    @PostMapping(value = ARMY_API, consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> saveArmy(@RequestBody Army army) {
        log.info(">>> Save army: {}", army);
        armyUseCase.save(army);
        return new ResponseEntity<>(HttpStatus.CREATED);
    }

    @DeleteMapping(value = ARMY_API, consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Void> deleteArmy(@RequestBody Army army) {
        log.info(">>> Delete army: {}", army);
        armyUseCase.delete(army.name());
        return new ResponseEntity<>(HttpStatus.OK);
    }

    @PutMapping(value = ARMY_API, consumes = MediaType.APPLICATION_JSON_VALUE)
    public ResponseEntity<Army> updateArmy(@RequestParam("name") String name, @RequestBody Army updatedArmy) {
        log.info(">>> Update army: {}", name);
        var existingArmy = armyUseCase.getByName(name);
        var updated = armyUseCase.update(existingArmy, updatedArmy);
        return ResponseEntity.ok(updated);
    }
}
