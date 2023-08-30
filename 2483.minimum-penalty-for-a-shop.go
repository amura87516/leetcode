/*
 * @lc app=leetcode id=2483 lang=golang
 *
 * [2483] Minimum Penalty for a Shop
 */

// @lc code=start
func bestClosingTime(customers string) int {
    right_y := make([]int, len(customers)+1);
	cnt := 0;
	for i:=len(customers)-1;i>=0;i--{
		if customers[i] == 'Y' {
			cnt++;
		}
		right_y[i] = cnt;
	}

	res := -1;
	minimum := math.MaxInt;
	cnt = 0;
	for i:=0;i<=len(customers);i++{
		penalty := cnt + right_y[i];
		if minimum > penalty {
			minimum = penalty;
			res = i;
		}
		if i<len(customers) && customers[i] == 'N'{
			cnt++;
		}
	}
	return res;
}
// @lc code=end

