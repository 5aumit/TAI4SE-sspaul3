package week5.day5;

public class GenericDynamicArray <T>{
    private Object[] array;
    private int count;
    private int length;
    GenericDynamicArray(){
        length=10;
        count=0;
        array = new Object[length];
    }
    public void remove(int index){
        if(index<count){
            for (int i = index; i < count; i++) {
                array[i]=array[i+1];
            }
            count--;
        }
    }
    public int indexOf(T obj){
        for (int i = 0; i < count; i++) {
            if(((T)array[i]).equals(obj))
                return i;
        }
        return -1;
    }
    public boolean contain(T obj){
        if(indexOf(obj)!=-1)
            return true;
        return  false;
    }
    public void remove(T obj){
       if(indexOf(obj)!=-1){
           remove(indexOf(obj));
       }
    }

    public void add(T obj){
        if(count==length/2){
            Object arr[] = new Object[2*length];
            for (int i = 0; i < count; i++) {
                arr[i] = array[i];
            }
            array = arr;
        }
        array[count]=obj;
        count++;
    }
    @SuppressWarnings("unchecked")
    public  T getElement(int index){
        if(index<count){
            return (T)array[index];
        }
        else return null;
    }

    public int getCount() {
        return count;
    }

    public int getLength() {
        return length;
    }
    public void print(){
        for (int i = 0; i < count; i++) {
            System.out.println(array[i]);
        }
    }
}
