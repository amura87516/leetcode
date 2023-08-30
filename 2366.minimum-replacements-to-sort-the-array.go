/*
 * @lc app=leetcode id=2366 lang=golang
 *
 * [2366] Minimum Replacements to Sort the Array
 */

// @lc code=start
func minimumReplacement(nums []int) int64 {
    var res int64 = 0;
	prev := int(nums[len(nums)-1]);
	for i:= len(nums)-2; i>=0; i--{
		if nums[i] < prev {
			prev = nums[i];
		}
		if nums[i] > prev {
			cnt := int(math.Ceil(float64(nums[i]) / float64(prev)));
			res += int64(cnt) - 1;
			
			shortage := prev * cnt - nums[i];
			prev = prev - int(math.Ceil(float64(shortage) / float64(cnt)));
		}
	}
	return res;
}
// @lc code=end

