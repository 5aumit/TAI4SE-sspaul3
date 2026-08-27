/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.example.beans;

import com.example.ejb.ArticlesFacade;
import com.example.entities.Articles;
import java.io.Serializable;
import java.util.List;
import javax.ejb.EJB;
import javax.enterprise.context.SessionScoped;
import javax.inject.Inject;
import javax.inject.Named;

/**
 *
 * @author mkolvane81
 */
@Named(value = "articlesController")
@SessionScoped

public class ArticlesController implements Serializable {

    @EJB
    ArticlesFacade articlesFacade;

    @Inject
    ArticlesBean articleBean;

    /**
     * Creates a new instance of itemController
     *
     * @return
     */
    // public itemController() {
    // }
    public List<Articles> getAll() {

        return articlesFacade.findAll();
    }

    public int count() {

        return articlesFacade.count();
    }

    public String delete(Articles x) {

        articlesFacade.remove(x);

        return null;

    }

    public String add() {

        Articles y = new Articles();
        y.setIdArticle(Integer.SIZE);
        y.setDescription(articleBean.getDescription());
        y.setInventory(articleBean.getInventory());
        y.setPrice(articleBean.getPrice());
       // y.setOwner(articleBean.getOwner());
        
//        y.setCategory(articleBean.getCategory());
//        y.setSubCategory(articleBean.getSubcategory());


        articlesFacade.create(y);

        return "index";
    }

    public String edit(Articles i) {
        articleBean.setIdArticle(i.getIdArticle());
        articleBean.setDescription(i.getDescription());
        articleBean.setInventory(i.getInventory());
        articleBean.setPrice(i.getPrice());

        return "update";
    }

    public String save() {

        Articles i = new Articles(articleBean.getIdArticle());

        i.setDescription(articleBean.getDescription());
        i.setInventory(articleBean.getIdArticle());
        i.setPrice(articleBean.getPrice());

        articlesFacade.edit(i);

        return "index";

    }
}
