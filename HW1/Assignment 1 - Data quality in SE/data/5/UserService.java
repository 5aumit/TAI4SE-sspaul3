package com.supershop.service;

import android.content.Context;
import android.text.TextUtils;

import com.supershop.model.User;
import com.supershop.repository.UserDatabase;
import com.supershop.utils.SaveSharedPreference;

import java.util.List;

public class UserService implements IUserService {



    @Override
    public void insertData(Context mContext, User user) {
        UserDatabase.getInstance(mContext).userDao().inserUser(user);
    }

    @Override
    public void updateData(Context mContext, User user) {
        UserDatabase.getInstance(mContext).userDao().inserUser(user);
    }

    @Override
    public void deleteById(Context mContext, User user) {
        UserDatabase.getInstance(mContext).userDao().deleteUser(user);
    }

    @Override
    public User getById(Context mContext, User user) {

        return UserDatabase.getInstance(mContext).userDao().getUserById(user.getId());
    }

    @Override
    public List<User> getAll(Context mContext) {
        return UserDatabase.getInstance(mContext).userDao().getAllUsers();
    }

    @Override
    public boolean isLogin(User user, Context mContext) {
        String uName = user.getUsername();
        String uPass = user.getPassword();
        if (TextUtils.isEmpty(uName) || TextUtils.isEmpty(uPass))
            return false;

        User dUser = UserDatabase.getInstance(mContext).userDao().getUserByUsername(uName);
        if (dUser != null){
            SaveSharedPreference.setLoggedIn(mContext, true);
            return true;
        }else {
            SaveSharedPreference.setLoggedIn(mContext, false);
            return false;
        }

    }

    private boolean validUsername(String username){
        boolean isValid = !TextUtils.isEmpty(username);
        return isValid;
    }

    private boolean validPassword(String password){
        boolean isValid = !TextUtils.isEmpty(password);
        return isValid;
    }

}
