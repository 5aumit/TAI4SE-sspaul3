package com.eqworks.eqworkssdklib;

import java.util.concurrent.BlockingQueue;
import java.util.concurrent.LinkedBlockingQueue;
import java.util.concurrent.ThreadPoolExecutor;
import java.util.concurrent.TimeUnit;

/**
 * Class for putting multiple request into queue .
 */
public class GeoLocationTaskManager {

    private final ThreadPoolExecutor downloadThreadPool;
    private final BlockingQueue<Runnable> downaloadWorkQueue;

    private static final int CORE_POOL_SIZE = 5;
    private static final int MAX_POOL_SIZE = 5;
    private static final int KEEP_ALIVE_TIME = 50;

    private static GeoLocationTaskManager downloadManager = null;
    private static MainThreadExecutor handler;

    static {
        downloadManager = new GeoLocationTaskManager();
        handler = new MainThreadExecutor();
    }

    private GeoLocationTaskManager() {
        downaloadWorkQueue = new LinkedBlockingQueue<Runnable>();

        downloadThreadPool = new ThreadPoolExecutor(CORE_POOL_SIZE, MAX_POOL_SIZE,
                KEEP_ALIVE_TIME, TimeUnit.MILLISECONDS, downaloadWorkQueue);
    }

    public static GeoLocationTaskManager getManager() {
        return downloadManager;
    }

    public void run(Runnable task) {
        downloadThreadPool.execute(task);
    }

    //to runs task on main thread from background thread
    public MainThreadExecutor getHandler() {
        return handler;
    }
}
