package interview;


/**
 * 单例模式
 * 实现线程安全的单例（双重检查锁 + 静态内部类两种方式）
 */
public class Ex02Singleton {

    // TODO: 在这里实现
    private static volatile Singleton instance;

    private Singleton() {}

    public static Singleton getInstance() {
        if(instance == null){
            synchronized(Singleton.class) {
                if(instance == null) {
                    instance = new Singleton();
                }
            }
        }
        return instance;
    }
}
