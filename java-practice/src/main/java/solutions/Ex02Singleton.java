package solutions;

public class Ex02Singleton {

    // 方式1：双重检查锁
    public static class DCLSingleton {
        private static volatile DCLSingleton instance;

        private DCLSingleton() {}

        public static DCLSingleton getInstance() {
            if (instance == null) {
                synchronized (DCLSingleton.class) {
                    if (instance == null) {
                        instance = new DCLSingleton();
                    }
                }
            }
            return instance;
        }
    }

    // 方式2：静态内部类（推荐）
    public static class HolderSingleton {
        private HolderSingleton() {}

        private static class Holder {
            static final HolderSingleton INSTANCE = new HolderSingleton();
        }

        public static HolderSingleton getInstance() {
            return Holder.INSTANCE;
        }
    }
}
