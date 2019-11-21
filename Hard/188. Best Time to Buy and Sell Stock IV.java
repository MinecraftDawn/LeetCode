class Solution {
    public int maxProfit(int k, int[] prices) {
        k = Math.min(k, (prices.length) / 2);
        int[] buy = new int[k + 1];
        int[] sell = new int[k + 1];
        for (int i = 0; i < buy.length; i++) buy[i] = Integer.MIN_VALUE;

        for (int price : prices) {
            for (int j = 1; j < k + 1; j++) {
                buy[j] = Math.max(buy[j], sell[j - 1] - price);
                sell[j] = Math.max(sell[j], buy[j] + price);
            }
        }
        return sell[k];

    }
}