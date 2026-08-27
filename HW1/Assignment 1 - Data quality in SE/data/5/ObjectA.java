package tasks.fourthtask;

class ObjectA implements Comparable<ObjectA>{

    private int id;

    private String field;

    private String fieldValue;

    ObjectA(String field, String fieldValue) {
        this.id = (int) (Math.random() * System.identityHashCode(this));
        this.field = field;
        this.fieldValue = fieldValue;
    }

    ObjectA(ObjectA object, String field, String fieldValue) {
        this.id = object.getId();
        this.field = field;
        this.fieldValue = fieldValue;
    }

    int getId() {
        return id;
    }

    String getField() {
        return field;
    }

    String getFieldValue() {
        return fieldValue;
    }


    @Override
    public int compareTo(ObjectA object) {
        boolean idMatch = this.id == object.getId();
        boolean filesMatch = this.field.equals(object.getField());
        boolean fieldsValuesMatch = this.fieldValue.equals(object.getFieldValue());

        if (idMatch && filesMatch && fieldsValuesMatch) return 0;

        if (!filesMatch) {
            System.out.println(String.format("Для id %s не совпало: Поле field. Ожидалось %s, текущее %s",
                    this.getId(),
                    this.getField(),
                    object.getField()
            ));

            return 1;
        }

        if (!fieldsValuesMatch) {
            System.out.println(String.format("Для id %s не совпало: Поле fieldValue. Ожидалось %s, текущее %s",
                    this.getId(),
                    this.getFieldValue(),
                    object.getFieldValue()
            ));

            return 2;
        }

        return 3;
    }

}
