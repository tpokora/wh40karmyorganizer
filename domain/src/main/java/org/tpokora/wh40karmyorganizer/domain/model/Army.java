package org.tpokora.wh40karmyorganizer.domain.model;

public record Army(String name) {
    @Override
    public String toString() {
        return "Army{" +
                "name='" + name + '\'' +
                '}';
    }
}
