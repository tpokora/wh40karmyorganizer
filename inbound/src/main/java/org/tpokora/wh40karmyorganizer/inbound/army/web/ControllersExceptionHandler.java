package org.tpokora.wh40karmyorganizer.inbound.army.web;


import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.ResponseStatus;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyAlreadyExistException;
import org.tpokora.wh40karmyorganizer.domain.exception.ArmyNotExistException;

import java.time.LocalDateTime;


@RestControllerAdvice
public class ControllersExceptionHandler  {

    private static final String ARMY_DOES_NOT_EXIST = "Army does not exist";
    private static final String ARMY_ALREADY_EXIST = "Army already exist";

    @ExceptionHandler(ArmyNotExistException.class)
    @ResponseStatus(value = HttpStatus.NOT_FOUND)
    public ErrorResponse handleArmyNotExistException() {
        return createErrorResponse(HttpStatus.NOT_FOUND, ARMY_DOES_NOT_EXIST);
    }

    @ExceptionHandler(ArmyAlreadyExistException.class)
    @ResponseStatus(value = HttpStatus.UNPROCESSABLE_ENTITY)
    public ErrorResponse handleArmyAlreadyExistException() {
        return createErrorResponse(HttpStatus.UNPROCESSABLE_ENTITY, ARMY_ALREADY_EXIST);
    }

    private ErrorResponse createErrorResponse(HttpStatus httpStatus, String errorMsg) {
        return new ErrorResponse(
                LocalDateTime.now(),
                httpStatus.value(),
                errorMsg);
    }
}