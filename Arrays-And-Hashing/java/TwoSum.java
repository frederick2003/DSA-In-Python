import java.util.HashMap;
public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> deltaMapping = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int delta = target - nums[i];
            if(deltaMapping.containsKey(delta)){
                return new int[]{deltaMapping.get(delta),i};
            }
            deltaMapping.put(nums[i], i);
        }
        return new int[]{};
    }
}