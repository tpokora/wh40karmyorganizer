package org.tpokora.wh40karmyorganizer.domain.exception;

public class CollectionNotExistException extends RuntimeException {

    private static final String EXCEPTION_MESSAGE_FORMAT = "Collection %s does not exist";

    public CollectionNotExistException(String name) {
        super(String.format(EXCEPTION_MESSAGE_FORMAT, name));
    }
}