package com.sweeper.clean.control;

import com.sweeper.clean.AbsDecision;
import com.sweeper.clean.HardwareInterfacePack;
import com.sweeper.clean.control.exceptions.ControllerException;
import com.sweeper.clean.control.memory.FloorCell;
import com.sweeper.clean.control.memory.FloorCellState;
import com.sweeper.clean.control.memory.State;
import com.sweeper.hardware.enumerations.Direction;
import com.sweeper.hardware.enumerations.ObstacleType;

import java.awt.*;
import java.util.Iterator;

/**
 * Determines if the clean cycle is completed.
 */
public class IsEndOfCleanCycle extends AbsDecision {

    @Override
    protected boolean decideImpl(HardwareInterfacePack sensors, State state) throws ControllerException {

        if (state == null) {
            throw new ControllerException("State is unavailable unable to process");
        }

        if (state.floorPlanSize() == 0) {
            return false;
        }

        Iterator<Point> floorPlan = state.getFloorPlanKeyIterator();
        while (floorPlan.hasNext()) {
            Point point = floorPlan.next();
            FloorCell floorCell = state.getFloorCell(point);

            if (FloorCellState.DIRTY.equals(floorCell.getState())) {
                return false;
            }

            for ( Direction direction : Direction.values() ) {
                if ( floorCell.getObstacle(direction) == ObstacleType.OPEN && state.getSurroundingFloorCell(floorCell, direction) == null ) {
                    return false;
                }
            }
        }

        return true;
    }

    @Override
    protected String getActivityLogMsg() {
        return "Check for End of Cleaning Cycle";
    }


}
