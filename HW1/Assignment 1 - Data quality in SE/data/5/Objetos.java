
package examen1_jarodzuniga_11911160;


public class Objetos {
    protected String color, descripción, marca, Tamaño, calidad, persona_ingreso;

    public Objetos() {
    }

    public Objetos(String color, String descripción, String marca, String Tamaño, String calidad, String persona_ingreso) {
        this.color = color;
        this.descripción = descripción;
        this.marca = marca;
        this.Tamaño = Tamaño;
        this.calidad = calidad;
        this.persona_ingreso = persona_ingreso;
    }

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public String getDescripción() {
        return descripción;
    }

    public void setDescripción(String descripción) {
        this.descripción = descripción;
    }

    public String getMarca() {
        return marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public String getTamaño() {
        return Tamaño;
    }

    public void setTamaño(String Tamaño) {
        this.Tamaño = Tamaño;
    }

    public String getCalidad() {
        return calidad;
    }

    public void setCalidad(String calidad) {
        this.calidad = calidad;
    }

    public String getPersona_ingreso() {
        return persona_ingreso;
    }

    public void setPersona_ingreso(String persona_ingreso) {
        this.persona_ingreso = persona_ingreso;
    }

    @Override
    public String toString() {
        return "color=" + color + ", descripci\u00f3n=" + descripción + ", marca=" + marca + ", Tama\u00f1o=" + Tamaño + ", calidad=" + calidad + ", persona_ingreso=" + persona_ingreso ;
    }
    
}
