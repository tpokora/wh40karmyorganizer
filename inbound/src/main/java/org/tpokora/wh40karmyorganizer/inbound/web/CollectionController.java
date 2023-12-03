package org.tpokora.wh40karmyorganizer.inbound.web;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.tpokora.wh40karmyorganizer.domain.model.Collection;
import org.tpokora.wh40karmyorganizer.domain.usecase.CollectionUseCase;

import java.util.List;

@Slf4j
@RestController
@RequiredArgsConstructor
public class CollectionController {

    public static final String COLLECTION_API = "/api/collection";

    private final CollectionUseCase collectionUseCase;

    @GetMapping(value = COLLECTION_API)
    public ResponseEntity<List<Collection>> getAllCollections() {
        log.info(">>> Retrieve all Collections");
        return ResponseEntity.ok(collectionUseCase.getAll());
    }
}
