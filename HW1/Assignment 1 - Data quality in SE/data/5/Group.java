public class Group {

    private String name;
    private Student[] students;

    public Group(String name) {
        this.name = name;
        students = new Student[10];
    }

    public void join(Student student) {
        int position = -1;
        for (int i = 0; i < students.length; i++) {
            if (students[i] == null) {
                students[i] = student;
                student.join(new RecordBook());
                position = i;
                break;
            }
        }
        if (position < 0) {
            throw new GroupOverflowException();
        }
    }

    public Student kick(RecordBook recordBook) {
        Student student = null;
        for (int i = 0; i < students.length; i++) {
            if (recordBook.equals(students[i].recordBook())) {
                student = students[i];
                student.kick();
                students[i] = null;
                break;
            }
        }
        return student;
    }

    public Student search(String lastName) {
        Student found = null;
        for (Student student : students) {
            if (student != null && student.identify(lastName)) {
                found = student;
                break;
            }
        }
        return found;
    }

    @Override
    public String toString() {
        sort();
        StringBuilder builder = new StringBuilder("Group '").append(name).append("' students:").append("\n");
        for (Student student : students) {
            builder.append(student).append("\n");
        }
        return builder.toString();
    }

    private Student[] sort() {
        for (int i = 0; i < students.length - 1; i++) {
            for (int j = i + 1; j < students.length; j++) {
                Student student1 = students[i];
                Student student2 = students[j];
                if (student1 == null && student2 != null) {
                    students[i] = student2;
                    students[j] = null;
                } else if (student1 != null && student2 != null &&
                        student1.lastName().compareToIgnoreCase(student2.lastName()) > 0) {
                    students[i] = student2;
                    students[j] = student1;
                }
            }
        }
        return students;
    }
}