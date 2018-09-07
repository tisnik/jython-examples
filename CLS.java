public class CLS {
    int v;

    public void setValue(int value) {
        this.v = value;
    }

    public int getValue() {
        return this.v;
    }

    public static void main(String[] args) {
        CLS cls = new CLS();
        cls.setValue(42);
        System.out.println(cls.getValue());
    }
}

