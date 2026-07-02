package solutions;

import java.util.ArrayList;
import java.util.List;

public class Ex06DeepClone {

    public static class Node implements Cloneable {
        String name;
        int value;
        List<Node> children;

        public Node(String name, int value) {
            this.name = name;
            this.value = value;
            this.children = new ArrayList<>();
        }

        @Override
        public Node clone() {
            try {
                Node copy = (Node) super.clone();
                copy.children = new ArrayList<>();
                for (Node child : this.children) {
                    copy.children.add(child.clone());
                }
                return copy;
            } catch (CloneNotSupportedException e) {
                throw new AssertionError(e);
            }
        }
    }
}
