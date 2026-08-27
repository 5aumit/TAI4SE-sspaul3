import processing.core.PImage;
import java.util.List;

public class Quake extends Actionable{

    private static final int QUAKE_ANIMATION_REPEAT_COUNT = 10;

    public void scheduleActions(EventScheduler scheduler,
                                WorldModel world, ImageStore imageStore) {
        scheduler.scheduleEvent(this,
                new Activity(this, world, imageStore),
                this.getActionPeriod());
        scheduler.scheduleEvent(this,
                new Animation(this, QUAKE_ANIMATION_REPEAT_COUNT),
                getAnimationPeriod());
    }

    public void executeActivity(WorldModel world,
                                     ImageStore imageStore, EventScheduler scheduler) {
        scheduler.unscheduleAllEvents(this);
        world.removeEntity(this);
    }

    public  Quake(String id, Point position,
                 List<PImage> images,
                 int actionPeriod, int animationPeriod) {
        super( id, position,images,actionPeriod, animationPeriod);
    }
}
