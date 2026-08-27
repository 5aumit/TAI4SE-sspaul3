public abstract class Agent {
    //Position
    int x;
    int y;
    //Range
    int power;
    //Couleur agent
    ColorAgent color;
    //life
    int life = 3;
    //Number of maximum bomb
    int max_bomb = 1;
    //score
    int score = 0;
    int id;

    static int cpt=0;
    
    public Agent(int x, int y, ColorAgent c) {
        this.x=x;
        this.y=y;
        this.power = 1;
        this.color = c;
        this.id = cpt;
        cpt++;
    }

    public int getX() {
        return x;
    }

    public int getY() {
        return y;
    }

    public void setX(int x) {
        this.x = x;
    }

    public void setY(int y) {
        this.y = y;
    }

    public int getPower() {
        return power;
    }

    public void upgrade() {
        power++;
    }

    public ColorAgent getColor() {
        return color;
    }

    public int getId(){
        return id;
    }

    public int getLife() {
        return life;
    }

    public void hitted() {
        --life;
    }

    public void break_wall() {
        score+=10;
    }
    public void hit() {
        score +=20;
    }

    public void kill() {
        score +=50;
    }

    public void fireUp() {
        ++power;
    }

    public void fireDown() {
        if (power > 1 ) {
            --power;
        }
    }

    public void bombUp() {
        ++max_bomb;
    }

    public void bombDown() {
        if (max_bomb > 1) {
            --max_bomb;
        }
    }

    public void fireSuit() {

    }

    public void getIll() {
        
    }

}