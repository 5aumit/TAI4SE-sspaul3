package com.example.coursekai.viewModel.course;

import android.app.Application;

import androidx.annotation.NonNull;
import androidx.lifecycle.AndroidViewModel;
import androidx.lifecycle.LiveData;
import androidx.lifecycle.ViewModel;
import androidx.lifecycle.ViewModelProvider;

import com.example.coursekai.BasicApp;
import com.example.coursekai.data.db.entity.CourseEntity;

public class CourseViewModel extends AndroidViewModel {

    private LiveData<CourseEntity> course;

    public CourseViewModel(@NonNull Application application, CourseRepository courseRepository, final long id){
        super(application);

        course = courseRepository.getCourse(id);
    }

    public LiveData<CourseEntity> getCourse(){
        return course;
    }

    public static class CourseFactory extends ViewModelProvider.NewInstanceFactory{

        @NonNull
        private final Application application;
        private final long courseId;
        private final CourseRepository repository;

        public CourseFactory(@NonNull Application application, long courseId){
            this.application = application;
            this.courseId = courseId;
            this.repository = ((BasicApp)application).getCourseRepository();
        }

        @SuppressWarnings("unchecked")
        @Override
        @NonNull
        public <T extends ViewModel> T create(@NonNull Class<T> modelClass){
            return (T) new CourseViewModel(application, repository, courseId);
        }
    }

}
