/*
 * @lc app=leetcode id=2369 lang=golang
 *
 * [2369] Check if There is a Valid Partition For The Array
 */

// @lc code=start
func validPartition(nums []int) bool {
	n := len(nums);
    combo2 := make([]bool, int(n))
	consecutive2 := make([]bool, int(n))
	for i := 1; i < n; i++{
		combo2[i] = nums[i-1] == nums[i];
		consecutive2[i] = nums[i-1] == nums[i] - 1;
	}

	combo3 := make([]bool, int(n))
	consecutive3 := make([]bool, int(n));
	for i := 2; i < n; i++{
		combo3[i] = nums[i-1] == nums[i] && combo2[i-1];
		consecutive3[i] = nums[i-1] == nums[i] - 1 && consecutive2[i-1];
	}

	res := make([]bool, int(n))
	res[1] = combo2[1];
	if n > 2{
		res[2] = combo3[2] || consecutive3[2];
	}
	for i := 3; i<n; i++{
		res[i] = res[i-2] && combo2[i] || res[i-3] && combo3[i] || res[i-3] && consecutive3[i];
	}
	return res[n-1];
}
// @lc code=end
