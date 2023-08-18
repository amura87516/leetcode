/*
 * @lc app=leetcode id=1615 lang=golang
 *
 * [1615] Maximal Network Rank
 */

// @lc code=start
func maximalNetworkRank(n int, roads [][]int) int {
    roadIdsByCity := make([][]int, n);
	for id, road := range roads{
		roadIdsByCity[road[0]] = append(roadIdsByCity[road[0]], id)
		roadIdsByCity[road[1]] = append(roadIdsByCity[road[1]], id)
	}

	res := 0;
	for i := 0;i<n;i++{
		for j:=i+1;j<n;j++{
			set := make(map[string]bool)
			for _, roadId := range roadIdsByCity[i]{
				set[string(roadId)] = true;
			}
			for _, roadId := range roadIdsByCity[j]{
				set[string(roadId)] = true;
			}
			res = int(math.Max(float64(res), float64(len(set))))
		}
	}

	return res
}
// @lc code=end

