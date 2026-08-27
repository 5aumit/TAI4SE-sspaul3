import javax.swing.JOptionPane;

public class Java
{
  public static void main(String args[])
  {
    String=contarDigitos();
    String=ordenarLista();
  }
  
  public static String contarDigitos()
  {
    int numero, digitos=1;
    numero=Integer.parseInt(JOptionPane.showInputDialog("Ingrese un número"));
    
    while(numero!=0)
    {
      numero;
      digitos++;
    }
    return JOptionPane.showMessageDialog(null,"La cantidad de digitos del número es: "+digitos);
  }
  
  public static String ordenarLista()
  {
    int lista[], listaTemp[];
    int tamanio, valor;
    String valores;
    tamanio=Integer.parseInt(JOptionPane.showInputDialog("Ingrese el tamaño de la lista"));
    lista=new int[tamanio];
    listaTemp=new int[1];
    
    for(int conta=0;conta<lista.length;conta++)
    {
      valor=Integer.parseInt(JOptionPane.showInputDialog("Ingrese los valores de la lista uno a la vez"));
      lista[conta]=valor;
    }
    
    for(int indice=0;indice<lista.length;indice++)
    {
      if(lista[indice]<lista[indice+1])
      {
        lista;
      }
      if(lista[indice]>lista[indice+1])
      {
        listaTemp[0]=lista[indice];
        lista[indice]=lista[indice+1];
        lista[indice+1]=listaTemp[0];
      }
    }
    for(int contador=0;contador<=lista.length;contador++)
    {
      valores+=" "+lista[contador];
    }
    return JOptionPane.showMessageDialog(null,"La lista ordenada es: "+valores);
  }
}