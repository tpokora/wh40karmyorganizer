package org.tpokora.wh40karmyorganizer.outbound.persistence;

import jakarta.persistence.*;
import lombok.Getter;
import lombok.RequiredArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "army")
@RequiredArgsConstructor
@Getter
@Setter
class ArmyEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Integer id;

    @Column(unique = true)
    private String name;

    public ArmyEntity(String name) {
        this.name = name;
    }
}
