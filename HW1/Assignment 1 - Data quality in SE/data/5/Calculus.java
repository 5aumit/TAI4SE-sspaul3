package utils;

import java.util.Random;

public class Calculus {

	/* standard deviation relative to average */
	public static Double getGaussian(final Double average, final Double relStdDeviation){
		Double absStdDeviation = average * relStdDeviation;
		return new Random().nextGaussian() * absStdDeviation + average; 
	}
	
	public static Double getGaussianCloseMin(final Double average, final Double relStdDeviation, final Double min){
		Double gaussian;
		do{
			gaussian = getGaussian(average, relStdDeviation);
		} while (gaussian < min);
		return gaussian;
	}
	
	public static Double getGaussianOpenMin(final Double average, final Double relStdDeviation, final Double min){
		Double gaussian;
		do{
			gaussian = getGaussian(average, relStdDeviation);
		} while (gaussian <= min);
		return gaussian;
	}
	
	public static StatisticalSample getGaussianSampleOpenMin(final Double average, final Double relStdDeviation, final Double min, final Long count){
		StatisticalSample sample = new StatisticalSample();
		for (int i = 0; i <= count; i++){
			sample.addValue(getGaussianOpenMin(average, relStdDeviation, min));
		}
		return sample;
	}

}
