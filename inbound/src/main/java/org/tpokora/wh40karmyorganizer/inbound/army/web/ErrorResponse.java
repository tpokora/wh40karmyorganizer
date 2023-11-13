package org.tpokora.wh40karmyorganizer.inbound.army.web;

import com.fasterxml.jackson.annotation.JsonFormat;

import java.time.LocalDateTime;

record ErrorResponse(
        @JsonFormat(shape = JsonFormat.Shape.STRING, pattern = "yyyy-MM-dd hh:mm:ss") LocalDateTime timestamp,
        int status,
        String error) {

}
