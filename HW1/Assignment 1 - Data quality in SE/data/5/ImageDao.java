package ru.geekbrains.android3_6.mvp.model.entity.room.dao;

import android.arch.persistence.room.Dao;
import android.arch.persistence.room.Delete;
import android.arch.persistence.room.Insert;
import android.arch.persistence.room.Query;
import android.arch.persistence.room.Update;

import java.util.List;

import ru.geekbrains.android3_6.mvp.model.entity.room.RoomImage;

import static android.arch.persistence.room.OnConflictStrategy.REPLACE;

@Dao
public interface ImageDao {

    @Insert(onConflict = REPLACE)
    void insert(RoomImage image);

    @Insert(onConflict =  REPLACE)
    void insert(RoomImage... images);

    @Insert(onConflict = REPLACE)
    void insert(List<RoomImage> images);

    @Update
    void update(RoomImage image);

    @Update
    void update(RoomImage... images);

    @Update
    void update(List<RoomImage> images);

    @Delete
    void delete(RoomImage image);

    @Delete
    void delete(RoomImage... images);

    @Delete
    void delete(List<RoomImage> images);

    @Query("SELECT * FROM roomimage")
    List<RoomImage> getAll();

    @Query("SELECT * FROM roomimage WHERE url = :url LIMIT 1")
    RoomImage findByUrl(String url);
}
