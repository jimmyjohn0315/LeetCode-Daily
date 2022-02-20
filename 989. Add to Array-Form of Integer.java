class Solution {
    public List<Integer> addToArrayForm(int[] num, int k) {
        List<Integer> res = new ArrayList<>();
        int n = num.length;
        for(int i = n - 1; i >= 0; i--){
            int tot = num[i] + k % 10;
            k /= 10;
            if(tot >= 10){
                k++;
            }
            res.add(tot % 10);
        }
        for(; k > 0; k /= 10){
            res.add(k % 10);
        }
        Collections.reverse(res);
        return res;
    }
}
