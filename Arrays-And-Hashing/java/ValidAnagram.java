import java.util.HashMap;
public class ValidAnagram {
    public boolean isAnagram(String s, String t) {
        // Will never be an anagram if they are different sizes.
        if(s.length() != t.length()){return false;}

        // Create char frequency count for both strings
        HashMap<Character, Integer> sCharFreqCount = new HashMap<>();
        HashMap<Character, Integer> tCharFreqCount = new HashMap<>();
        for(int i = 0; i < s.length(); i++){
            sCharFreqCount.put(s.charAt(i), sCharFreqCount.getOrDefault(s.charAt(i), 0) + 1);
            tCharFreqCount.put(t.charAt(i), tCharFreqCount.getOrDefault(t.charAt(i), 0) + 1);
        }
        return sCharFreqCount.equals(tCharFreqCount) ? true : false;
    }   
}