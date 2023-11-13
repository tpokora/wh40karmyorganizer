package org.tpokora.wh40karmyorganizer.domain.exception;

public class ArmyNotExistException extends RuntimeException {

    private static final String EXCEPTION_MESSAGE_FORMAT = "Army %s does not exist";
    public ArmyNotExistException(String name) {
        super(String.format(EXCEPTION_MESSAGE_FORMAT, name));
    }
}
