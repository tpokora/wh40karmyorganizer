package org.tpokora.wh40karmyorganizer.domain.exception;

public class CollectionAlreadyExistException extends RuntimeException {

    private static final String EXCEPTION_MESSAGE_FORMAT = "Collection %s already exist";

    public CollectionAlreadyExistException(String name) {
        super(String.format(EXCEPTION_MESSAGE_FORMAT, name));
    }
}
