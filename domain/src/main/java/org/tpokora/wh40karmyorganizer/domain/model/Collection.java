package org.tpokora.wh40karmyorganizer.domain.model;

public record Collection(String name, Army army) {

    @Override
    public String toString() {
        return "Collection{" +
                "name='" + name + '\'' +
                ", army=" + army +
                '}';
    }
}
