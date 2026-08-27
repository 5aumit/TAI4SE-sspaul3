
public class MapHashCodeImpl<K, V> implements Map<K, V> {
    private static final int DEFAULT_SIZE = 16;
    MapEntry<K, V> entries[];

    public MapHashCodeImpl() {
        entries = new MapEntry[DEFAULT_SIZE];
    }

    @Override
    public V get(K key) {
        int hashCode = key.hashCode();
        int position = hashCode & (entries.length - 1);
        return entries[position] != null ? entries[position].value : null; //11:00 тернарный оператор: ? - возвращаем, в противном случае - null
    }

    @Override
    public void put(K key, V value) {
        MapEntry<K, V> newMapEntry = new MapEntry<>(key, value);
        int hashCode = key.hashCode();
        int position = hashCode & (entries.length - 1);
        this.entries[position] = newMapEntry;
    }

    static class MapEntry<K, V> {
        K key;
        V value;

        public MapEntry(K key, V value) {
            this.key = key;
            this.value = value;
        }
    }
}