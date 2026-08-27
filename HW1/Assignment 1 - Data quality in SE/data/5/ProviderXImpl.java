package com.etz.replay.unit.targets;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class ProviderXImpl implements ProviderX {
    private static final Logger LOGGER = LoggerFactory.getLogger(ProviderXImpl.class);

    @Override
    public DataX makeX(String fieldFromX, String dataFromX, int retry) {

        //new Exception().printStackTrace();
      /*  if (retry > 0) {
            return this.makeX(fieldFromX, dataFromX, retry - 1);
        }*/
        DataX dataX = new DataX();
        dataX.dataFromX = dataFromX;
        dataX.fieldFromX = fieldFromX;
        dataX.dataY = new DataY();
        dataX.dataY.dataZArr = new DataZ[]{
                new DataZ(),
                new DataZ(),
                new DataZ()
        };
        return dataX;
    }
}
