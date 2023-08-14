/*
 * @lc app=leetcode id=215 lang=cpp
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start

// O(nlogk)
int heap(vector<int> &nums, int k){
    priority_queue<int, vector<int>, greater<int>> pq;
    for (int num: nums){
        pq.push(num);
        if (pq.size() > k){
            pq.pop();
        }
    }
    return pq.top();
}

// O(nlogn)
int built_in_sort(vector<int> &nums, int k){
    sort(nums.begin(), nums.end());
    return nums[nums.size()-k];
}

void swap(int &a, int &b){
    int temp = a;
    a = b;
    b = temp;
}

int quick_sort(vector<int> &nums, const int start, const int end){
    int pivot = end;
    int left = start, right = start;
    while(right < end){
        if (nums[right] < nums[pivot]) {
            swap(nums[left++], nums[right]);
        }
        right++;
    }
    swap(nums[left], nums[pivot]);
    return left;
}

// int quick_sort(vector<int> &nums, const int start, const int end){
//     int pivot = start;
//     int left = end, right = end;
//     while(left > start){
//         if (nums[left] > nums[pivot]) {
//             swap(nums[left], nums[right--]);
//         }
//         left--;
//     }
//     swap(nums[right], nums[pivot]);
//     return right;
// }

// O(n)
int quick_select(vector<int> &nums, int k, int start, int end){
    int pivot = quick_sort(nums, start, end);
    if(pivot == k){
        return nums[k];
    }else if(pivot < k){
        return quick_select(nums, k, pivot+1, end);
    }else{
        return quick_select(nums, k, 0, pivot-1);
    }
}

class Solution{
public:
    int findKthLargest(vector<int> &nums, int k){
        return heap(nums, k);
        // return built_in_sort(nums, k);
        // return quick_select(nums, nums.size()-k, 0, nums.size()-1);
    }
};

// @lc code=end
