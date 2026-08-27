package AutomatoPilha;


public class Vertice {

    private String next;
    private String simboloDest;
    private String simboloEmpilhar;
    private String simbolotopo;
    private boolean isFinal;
    
    public String getSimbolotopo() {
        return simbolotopo;
    }

    public void setSimbolotopo(String simbolotopo) {
        this.simbolotopo = simbolotopo;
    }

    public String getNext() {
        return next;
    }

    public void setNext(String next) {
        this.next = next;
    }

    public boolean isFinal() {
        return isFinal;
    }

    public void setIsFinal(boolean isFinal) {
        this.isFinal = isFinal;
    }

    public String getSimboloDest() {
        return simboloDest;
    }

    public void setSimboloDest(String simboloDest) {
        this.simboloDest = simboloDest;
    }

    public String getSimboloEmpilhar() {
        return simboloEmpilhar;
    }

    public void setSimboloEmpilhar(String simboloEmpilhar) {
        this.simboloEmpilhar = simboloEmpilhar;
     
    }

}
