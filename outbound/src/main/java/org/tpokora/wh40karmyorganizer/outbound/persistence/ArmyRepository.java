package org.tpokora.wh40karmyorganizer.outbound.persistence;

import org.springframework.data.jpa.repository.JpaRepository;
import org.tpokora.wh40karmyorganizer.outbound.persistence.entity.ArmyEntity;

import java.util.Optional;

interface ArmyRepository extends JpaRepository<ArmyEntity, Integer> {

    Optional<ArmyEntity> findByName(String name);
}
