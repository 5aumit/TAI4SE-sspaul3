package com.orm.hibernate.jta.concurrency.locking;

import com.orm.hibernate.jta.model.Item;
import com.orm.hibernate.jta.utils.QueryProcessor;

import javax.persistence.LockModeType;
import java.util.UUID;
import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;
import java.util.concurrent.atomic.AtomicBoolean;

public class DeadLockExample {
    private static AtomicBoolean start = new AtomicBoolean(false);

    private static Item createItem() {
        return QueryProcessor.process(em -> {
            final Item itm = new Item(UUID.randomUUID().toString());
            em.persist(itm);
            return itm;
        });
    }

    public static void main(String[] args) {
        Item createdItem1 = createItem();
        Item createdItem2 = createItem();

        final AtomicBoolean flag = new AtomicBoolean(false);
        final ExecutorService executorService = Executors.newFixedThreadPool(2);
        executorService.execute(() -> {
            while (true) {
                if (flag.get()) {
                    QueryProcessor.process(em -> {
                        Item itemOne = em.find(Item.class, createdItem1.getId(), LockModeType.PESSIMISTIC_READ);
                        itemOne.setName("[thread-1] First new name");

                        Item itemTwo = em.find(Item.class, createdItem2.getId(), LockModeType.PESSIMISTIC_WRITE);
                        itemTwo.setName("[thread-1] Second new name");
                    });
                    break;
                }
            }
        });

        executorService.execute(() -> {
            while (true) {
                if (flag.get()) {
                    QueryProcessor.process(em -> {
                        Item itemOne = em.find(Item.class, createdItem2.getId(), LockModeType.PESSIMISTIC_READ);
                        itemOne.setName("[thread-2] First new name");

                        Item itemTwo = em.find(Item.class, createdItem1.getId(), LockModeType.PESSIMISTIC_WRITE);
                        itemTwo.setName("[thread-2] Second new name");
                    });
                    break;
                }
            }
        });
        executorService.shutdown();

        flag.set(true);
    }
}
