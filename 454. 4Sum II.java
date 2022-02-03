class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        int res = 0;
        Map<Integer, Integer> map = new HashMap<>();
        for(int i : nums1){
            for(int j : nums2){
                map.put(i+j, map.getOrDefault(i+j, 0) + 1);
            }
        }
        
        for(int k :nums3){
            for(int l : nums4){
                if(map.containsKey(-l-k)){
                    res += map.get(-l-k);
                }
            }
        }
        return res;
    }
}
