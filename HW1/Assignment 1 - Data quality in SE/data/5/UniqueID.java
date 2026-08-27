package pl.gajewski.michal.java.app.bankaccount.dao;

import pl.gajewski.michal.java.app.bankaccount.utils.DbPropertySourceUtils;

import java.io.InputStream;
import java.io.InputStreamReader;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.Arrays;
import java.util.logging.Logger;

public class UniqueID {
    private static final Logger LOGGER = Logger.getLogger(UniqueID.class.getName());

    public static int uniqueIdClean() {
        ClassLoader classLoader = Thread.currentThread().getContextClassLoader();
        int id = 0;

        try (InputStream inputStream = classLoader.getResourceAsStream("ID.txt");
             InputStreamReader fileReader = new InputStreamReader(inputStream)) {

            char[] buffer = new char[8];
            int read;
            while ((read = fileReader.read(buffer)) != -1) {
                LOGGER.info("Buffor: " + Arrays.toString(buffer));
                LOGGER.info("Ilość odczytanych znaków: " + read);
            }
            String idString = String.valueOf(buffer);
            id = Integer.parseInt(idString.trim());

            int incrementedId = ++id;
            LOGGER.info("IncrementedId: " + incrementedId);

            Files.write(
                    Paths.get(DbPropertySourceUtils.getProperty("db.id.name")),
                    Integer.toString(incrementedId).getBytes());

        } catch (Exception e) {
            e.printStackTrace();
        }
        return id;
    }
}

