package edu.byu.cs.autism.minigame;

import edu.byu.cs.autism.friend.FriendMiniGameHistory;

import java.util.HashMap;
import java.util.Map;

public class Minigames {

    public static final String GAME_LAVA_BRIDGE = "lava";
    public static final String GAME_T_BRIDGE = "T";
    public static final String GAME_TEAM_TUNNEL = "team";

    private static final Map<String, Integer> BASE_SCORES = new HashMap<>();
    static {
        BASE_SCORES.put(GAME_LAVA_BRIDGE, 0);
        BASE_SCORES.put(GAME_T_BRIDGE, 5);
        BASE_SCORES.put(GAME_TEAM_TUNNEL, 2);
    }
    private static final Map<String, Integer> NEW_PARTNER_BONUSES = new HashMap<>();
    static {
        NEW_PARTNER_BONUSES.put(GAME_LAVA_BRIDGE, 1);
        NEW_PARTNER_BONUSES.put(GAME_T_BRIDGE, 5);
        NEW_PARTNER_BONUSES.put(GAME_TEAM_TUNNEL, 3);
    }
    private static final int[] CONTINUED_PARTNER_BONUSES = {5, 10};
    private static final Map<String, Integer> FIRST_TIME_BONUSES = new HashMap<>();
    static {
        FIRST_TIME_BONUSES.put(GAME_LAVA_BRIDGE, 5);
        FIRST_TIME_BONUSES.put(GAME_T_BRIDGE, 10);
        FIRST_TIME_BONUSES.put(GAME_TEAM_TUNNEL, 7);
    }

    /**
     * Check whether the game name is valid.
     * @param game Name of the mini-game.
     * @return `true` if the mini-game name is valid; otherwise, `false`.
     */
    public static boolean isValid(String game) {
        return BASE_SCORES.containsKey(game);
    }

    /**
     * Calculate the score for two players playing a mini-game.
     * @param history Of games played.
     * @param game Name of mini-game.
     * @param p1 UUID of player 1.
     * @param p2 UUID of player 2.
     * @return Integer score.
     */
    public static int getScore(FriendMiniGameHistory history, String game, String p1, String p2) {
        int score = BASE_SCORES.get(game);
        score += getNewPartnerBonus(history, game, p1, p2);
        score += getContinuedPartnerBonus(history, game, p1, p2);
        score += getFirstTimeBonus(history, game, p1);
        return score;
    }

    private static int getNewPartnerBonus(FriendMiniGameHistory history, String game, String p1, String p2) {
        //check if players have played this mini-game before
        final int timesPlayed = history.getGamesPlayed(game, p1, p2);
        boolean newgame = timesPlayed == 0;
        if (newgame) {
            //calculate bonus from minigame
            return NEW_PARTNER_BONUSES.get(game);
        }
        return 0;
    }

    private static int getContinuedPartnerBonus(FriendMiniGameHistory history, String game, String p1, String p2) {
        //see if players have played this mini-game before
        final int gameCount = history.getGamesPlayed(game, p1, p2);
        if (gameCount > 0) {
            return 0;
        }
        // At this point, this is definitely a new game.
        final int uniqueCount = history.getTotalGamesPlayed(p1, p2, true);
        if (uniqueCount == 0) {
            // Not a CONTINUED partner, since they have never played any game together before.
            return 0;
        }
        // Minus 1 just so we can start the bonuses array at index 0.
        return CONTINUED_PARTNER_BONUSES[uniqueCount - 1];
    }

    private static int getFirstTimeBonus(FriendMiniGameHistory history, String game, String p1) {
        //check if this mini-game contains the player
        final boolean firstTime = history.getGamesPlayed(game, p1) == 0;
        if (firstTime){
            //calculate bonus from mini-game
            return FIRST_TIME_BONUSES.get(game);
        }
        return 0;
    }
}
