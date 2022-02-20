class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int start = 0, end = arr.length - 1;
        while(start + 1 < end){
            int mid = start + (end - start) / 2;
            if(arr[mid] > arr[mid-1]){
                start = mid;
            }
            else{
                end = mid;
            }
        }
        return arr[start] > arr[end] ? start : end;
    }
}
