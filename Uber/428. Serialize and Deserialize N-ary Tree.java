/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val,List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/
class Codec {

    // Encodes a tree to a single string.
    public String serialize(Node root) {
        StringBuilder sb = new StringBuilder();
        serializeHelper(root, sb);
        return sb.toString();
    }
    
    private void serializeHelper(Node root, StringBuilder sb){
        if(root==null){
            return;
        }else{
            sb.append("[");
            sb.append(String.valueOf(root.val));
            sb.append(":");
            for(Node child: root.children){
                serializeHelper(child, sb);
            }
            sb.append("]");
        }
    }

    // Decodes your encoded data to tree.
    public Node deserialize(String data) {
        Node r = new Node();
        int n = data.length();
        char[] da = data.toCharArray();
        Stack<Node> sNode = new Stack<Node>();
        ArrayList<Node> children = new ArrayList<Node>();
        
        if(data.isEmpty())
            return null;
        
        for(int i=1; i<n-1; i++){
            int value = 0;
            Node root = new Node();
            Node parent = new Node();
            if(da[i]!='[' && da[i]!=']'){
                while(da[i]!=':'){
                    value = value * 10 + Character.getNumericValue(da[i]);
                    i++;
                }
                root.val = value;
                //value = "";
                root.children = new ArrayList<Node>();
                sNode.push(root);
            }
            else if(da[i]==']'){
                root = sNode.pop();
                parent = sNode.pop();
                parent.children.add(root);
                sNode.push(parent);
            }// "]"
            else{
                continue;
            }
            
        }
        
        r = sNode.pop();
        
        return r;
    }
}

// Your Codec object will be instantiated and called as such:
// Codec codec = new Codec();
// codec.deserialize(codec.serialize(root));