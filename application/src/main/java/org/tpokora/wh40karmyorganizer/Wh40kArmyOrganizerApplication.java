package org.tpokora.wh40karmyorganizer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication(scanBasePackages = "org.tpokora.wh40karmyorganizer")
public class Wh40kArmyOrganizerApplication {

    public static void main(String[] args) {
        SpringApplication.run(Wh40kArmyOrganizerApplication.class, args);
    }

}
