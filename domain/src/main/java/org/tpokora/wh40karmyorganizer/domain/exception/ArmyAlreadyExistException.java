package org.tpokora.wh40karmyorganizer.domain.exception;

public class ArmyAlreadyExistException extends RuntimeException {

    private static final String EXCEPTION_MESSAGE_FORMAT = "Army %s already exist";

    public ArmyAlreadyExistException(String name) {
        super(String.format(EXCEPTION_MESSAGE_FORMAT, name));
    }
}
