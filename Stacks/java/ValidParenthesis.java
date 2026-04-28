import java.util.ArrayList;
import java.util.HashMap;
class ValidParenthesis {
    public boolean isValid(String s) {
        if(s.length() <= 1){
            return false;
        }
        ArrayList<Character> stack = new ArrayList<>();
        HashMap<Character, Character> bracketMap = new HashMap<>();
        bracketMap.put(']', '[');
        bracketMap.put('}', '{');
        bracketMap.put(')', '(');

        for(int i = 0; i < s.length(); i++){
            char curChar = s.charAt(i);

            // Open bracket
            if (!bracketMap.containsKey(curChar)){
                stack.add(curChar);
            } else{ 
                if (stack.size() == 0){return false;}
                // Does it match closing bracket?
                char topChar = stack.remove(stack.size() - 1);
                if(topChar != bracketMap.get(curChar)){
                    return false;
                }
            }
        }
        return stack.size() == 0 ? true : false;
    }
}