package org.tpokora.wh40karmyorganizer.outbound.persistence;

import org.springframework.data.jpa.repository.JpaRepository;

import java.util.Optional;

public interface ArmyRepository extends JpaRepository<ArmyEntity, Integer> {

    Optional<ArmyEntity> findByName(String name);
    boolean existsArmyEntityByName(String name);
}
