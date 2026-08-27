package business;

import data.Diagram;
import data.Sequences;

public class StringManager {
    public void split(String string, Diagram diagram) {
        int n=diagram.getNbChar();
        Sequences[] sequences = diagram.getSequences();

        for(int i=0; i<string.length()-n+1;i++) {
            String seq=string.substring(i,i+n);
            if(seq.contains(" "))
                continue;
            boolean flag=true;
            int j=0;
            while(flag && j<sequences.length) {
                if(seq.equals(sequences[j].getValue())) {
                    sequences[j].setCount(sequences[j].getCount()+1);
                    flag=false;
                }
                j++;
            }
            if(flag==true) {
                //Add Sequence
                int lastIndex=diagram.getLastIndex();
                sequences[lastIndex]=new Sequences(lastIndex,seq, diagram);
            }
        }
    }

    public void sort(Diagram diagram) {
        for(int i=0; i<diagram.getLastIndex();i++) {
            Sequences[] sequences=diagram.getSequences();
            int idMax=0;
            int countMax=0;
            String valueMax="";
            for(int j=i; j<diagram.getLastIndex();j++) {
                if(sequences[j].getCount()>countMax) {
                    idMax=j;
                    countMax=sequences[j].getCount();
                    valueMax=sequences[j].getValue();
                }
            }
            sequences[idMax].setValue(sequences[i].getValue());
            sequences[idMax].setCount(sequences[i].getCount());

            sequences[i].setValue(valueMax);
            sequences[i].setCount(countMax);
        }

    }
}
