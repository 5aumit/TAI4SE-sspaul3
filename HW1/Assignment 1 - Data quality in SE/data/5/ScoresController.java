package com.koiwaLearning.api.controller;

import com.koiwaLearning.api.domain.ScoreDetail;
import com.koiwaLearning.api.domain.Scores;
import com.koiwaLearning.api.service.ScoresService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.ModelAndView;

import java.util.List;


@RestController
@RequestMapping("/scores")
public class ScoresController {

    @Autowired
    private ScoresService scoresService;


    //検索
    @RequestMapping(value = {"/getScores"}, method = RequestMethod.GET)
    public ModelAndView getScores(Model model) {
        model.addAttribute("scoresList",scoresService.getScores());
        model.addAttribute("title", "Scores信息");
        return new ModelAndView("scores/scoresSelect","scoresModel",model);
    }

    /**
     * 查询Score
     */
    @RequestMapping(value = "/getScore", method = RequestMethod.GET)
    public ScoreDetail getScore(@RequestParam("scoreId") String scoreId) {

        ScoreDetail score = scoresService.getScore(scoreId);

        return score;
    }

    //追加
    @RequestMapping(value = {"/scores/insert"},method = RequestMethod.GET)
    public int insertScores() {
        Scores scores = new Scores();
        scores.setSno("101");
        scores.setCno("1-234");
        scores.setDegree("85.0");
        return scoresService.insertScores(scores);
    }

    //更新
    @RequestMapping(value = {"/scores/update"},method = RequestMethod.GET)
    public int updateScores() {
        Scores scores = new Scores();
        scores.setSno("102");
        scores.setCno("1-101");
        scores.setDegree("86.0");
        return scoresService.updateScores(scores);
    }

    //削除
    @RequestMapping(value = {"/scores/delete"},method = RequestMethod.GET)
    public int deleteScores(){
        String sno = "101";
        return scoresService.deleteScores(sno);

    }
}
