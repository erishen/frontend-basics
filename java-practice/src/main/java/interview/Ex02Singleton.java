package interview;


/**
 * 单例模式
 * 实现线程安全的单例（双重检查锁 + 静态内部类两种方式）
 */
public class Ex02Singleton {

    // TODO: 在这里实现
    private static volatile Ex02Singleton instance;

    private Ex02Singleton() {}

    public static Ex02Singleton getInstance() {
        if(instance == null){
            synchronized(Ex02Singleton.class) {
                if(instance == null) {
                    instance = new Ex02Singleton();
                }
            }
        }
        return instance;
    }
}
