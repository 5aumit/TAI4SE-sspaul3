package controllers;

import java.util.Comparator;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

import models.Player;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Qualifier;
import org.springframework.stereotype.Component;

import com.google.inject.Inject;

import play.Logger;
import play.cache.Cache;
import dao.TourDao;

@Component
public class DataFetcher implements Runnable {

	@Inject
	private TourDao tourDao;

	public void run() {
		long startTime = System.currentTimeMillis();
		List<Player> result = tourDao.getToursForActivePlayersOnAllMaps();
		/*
		 * jdbcTemplate.query(
		 * "select alt_class, favorite_class, ideal_team, map_id, reputation, steam_id, tour, xp from ranks, orderby map_id, tour"
		 * , new RowMapper<Player>() {
		 * 
		 * @Override public Player mapRow(ResultSet rs, int row) throws
		 * SQLException { Player item = new Player();
		 * item.setAltClass(rs.getInt("alt_class")); item
		 * .setFavoriteClass(rs.getInt("favorite_class" ));
		 * item.setIdealTeam(rs.getLong("ideal_team"));
		 * item.setMapId(rs.getInt("map_id")); item.setReputation
		 * (rs.getBigDecimal("reputation"));
		 * item.setSteamId(rs.getString("steam_id"));
		 * item.setTour(rs.getInt("tour")); item.setXp(rs.getInt("xp")); return
		 * item; } });
		 */

		result.stream()
				.map(f -> f.getMapId())
				.distinct()
				.forEach(
						(mapId) -> IntStream.range(0, 201).forEach(
								(tour) -> populateCache(result, mapId, tour)));
		Logger.info("Cache refreshed in {}ms", System.currentTimeMillis()-startTime);

	}

	private void populateCache(List<Player> result, Integer mapId, int tour) {
		Cache.set(
				mapId + "+" + tour,
				result.stream()
						.filter(x -> x.getMapId() == mapId
								&& x.getTour() <= tour)
						.sorted(Comparator.comparing(Player::getTour))
						.collect(Collectors.toList()));
	}

	public TourDao getTourDao() {
		return tourDao;
	}

	public void setTourDao(TourDao tourDao) {
		this.tourDao = tourDao;
	}

}
