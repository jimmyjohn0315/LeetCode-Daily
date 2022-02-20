class Solution {
    public int longestConsecutive(int[] nums) {
        Set<Integer> set = new HashSet<>();
        for(int i : nums){
            set.add(i);
        }
        int res = 0;
        for(int i : nums){
            if(!set.contains(i - 1)){
                int cur = i;
                int l = 1;
                while(set.contains(cur+1)){
                    cur++;
                    l++;
                }
                res = Math.max(res, l);
            }
        }
        return res;
    }
}
