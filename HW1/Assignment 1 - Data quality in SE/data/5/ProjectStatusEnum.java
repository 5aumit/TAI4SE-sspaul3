package com.tracking.system.enums;

import java.util.Optional;
import java.util.Arrays;

public enum ProjectStatusEnum {

    NEW(1),
    OPEN(2),
    IN_PROGRESS(3),
    COMPLETED(4),
    ON_HOLD(5);

    private final int mValue;

    ProjectStatusEnum(int value) {
        mValue = value;
    }

    public int getValue() {
        return ordinal() + 1;
    }

    private static final ProjectStatusEnum[] allValues = values();

    public static ProjectStatusEnum fromOrdinal(int n) {
        return allValues[n];
    }

    public static Optional<ProjectStatusEnum> valueOf(int value) {
        return Arrays.stream(values())
                .filter(projectStatusEnum -> projectStatusEnum.mValue == value)
                .findFirst();
    }

}