class Solution {
    public int[] searchRange(int[] nums, int target) {
        int first = binarySearch(nums, target, true);
        int last = binarySearch(nums, target, false);
        if(first <= last && last < nums.length && nums[first] == target && nums[last] == target){
            return new int[]{first, last};
        }
        return new int[]{-1,-1};
    }
    
    public int binarySearch(int[] nums, int target, boolean lower){
        int start = 0, end = nums.length - 1;
        while(start <= end){
            int mid = start + (end - start) / 2;
            if(nums[mid] > target || nums[mid] == target && lower){
                end = mid - 1;
            }
            else{
                start = mid + 1;
            }
        }
        return lower?start:end;
    }
}
