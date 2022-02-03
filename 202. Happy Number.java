class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        while(true){
            if(n == 1){
                return true;
            }
            if(set.contains(n)){
                return false;
            }
            set.add(n);
            n = getNext(n);
        }
    }
    
    private int getNext(int n){
        int sum = 0;
        while(n != 0){
            sum += Math.pow(n % 10, 2);
            n /= 10;
        }
        return sum;
    }
}
