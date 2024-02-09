#
# @lc app=leetcode id=2501 lang=python3
#
# [2501] Longest Square Streak in an Array
#

# @lc code=start
class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        position = {}
        for i in range(len(nums)):
            position[nums[i]] = i

        dp = [1] * len(nums)
        longest = 1
        for i in range(len(nums)):
            if nums[i]**2 in position:
                dp[position[nums[i]**2]] = dp[i] + 1
                longest = max(longest, dp[position[nums[i]**2]])
        # print(nums, dp)
        return longest if longest is not 1 else -1
# @lc code=end

[83109,8425,36388,11909,4537,60326,18516,68291,71886,84270,87036,950,96756,38589,94565,21664,63169,56403,89356,46579,10285,37809,97675,86027,96008,5312,97791,81689,7185,29622,37744,11612,99064,34439,98395,90279,91577,10727,88556,33063,88729,40309,69342,3929,95656,20300,41665,97479,79136,28742,77561,75576,39488,18588,31381,51458,76035,31429,52540,79885,93833,15673,49658,94062,87184,64117,81747,49871,62858,72063,97733,54046,39649,57625,177,79940,131,21098,92225,4090,19565,54555,31255,76584,82161,44477,7967,10206,40744,78320,68899,59306,13521,38018,69966,63511,73680,21695,92477,48425,30545,13498,88606,56573,37701,12766,86159,72635,84012,91639,89638,13271,89390,65627,85948,54186,14714,8697,39116,28987,39476,88014,61489,90058,56831,83134,81917,98136,52656,95599,23612,50170,9316,22300,72801,9906,2271,87925,87333,44676,58664,98110,41398,77212,57715,59278,54222,9937,26634,2866,71690,60314,47194,87334,64047,67184,74073,48116,8446,51202,89286,87891,9228,3713,70774,24691,61700,38804,68530,47241,67964,3293,9991,38595,4126,71362,56403,75768,76843,90703,5368,55204,49661,50571,74684,37128,78999,19297,28985,74024,72338,43858,18115,90100,71400,91722,31465,78711,63309,75231,46021,18866,58835,13900,28995,45055,56515,11160,4539,83270,90050,6001,99631,94262,67773,7245,66617,29843,97398,71357,29054,96946,13754,78741,86997,80201,54710,21852,49304,27318,1155,94576,90050,22705,58477,67583,5728,26984,36492,80951,59641,8903,47185,28018,78081,87683,15406,42116,11714,5752,32960,51542,40407,99873,13396,2287,82235,44418,22672,87625,27530,5534,94512,36320,21965,9012,36689,83958,70634,15063,45525,65047,14985,39937,2165,36570,6032,92468,89894,72166,52185,20706,94075,25995,27169,3013,76186,82362,14487,7171,34390,7359,7822,85789,98288,7962,89965,43568,10975,79323,25691,94858,82565,61222,51681,51353,13033,92866,61154,87229,9806,27980,38897,55029,3539,8719,6655,14942,50934,69793,71328,19869,45425,954,15494,62875,59786,87043,75300,31840,20781,69130,26830,83135,16960,32747,41434,93085,67988,11371,17946,28386,95336,34134,67965,90130,8742,53473,93014,1649,70845,33187,73274,86831,625,55787,44495,50649,87416,14797,61175,73335,69663,595,16555,86596,35555,13641,17232,44782,81783,4045,31769,60788,62443,84725,91289,69018,12645,81285,56838,5171,97789,64329,64815,51429,87401,97422,72171,50565,55146,764,70157,60177,95519,17863,57448,68247,53417,67664,59717,59777,74735,88377,2045,72899,35187,55552,70268,94425,76999,45172,59777,4162,7730,46280,26870,62919,13078,15470,81744,73680,62972,84753,54923,31857,87828,99283,42332,83944,61829,81601,76713,87059,47993,51521,92883,26639,93410,25614,39675,68186,16485,68366,59418,67743,35856,3781,18702,22440,90461,76833,24819,63487,59485,24072,64267,89317,84020,47074,51956,11390,93438,67325,22403,50069,4021,13086,51993,83641,35189,30299,26370,81709,73218,15245,79781,78954,93746,70260,25837,67802,93638,71888,78587,5521,72550,40645,83618,48710,22195,3345,86744,47558,59192,67008,69848,49333,66420,50831,18965,93512,49653,67131,17929,32598,24109,59719,49976,22315,9062,47721,77622,93372,97669,48707,24875,9486,79636,28131,93958,21344,37355,50035,7984,55880,90406,91230,91641,69038,58926,43232,72984,73635,2535,4350,21769,1366,79004,70395,41679,89094,40630,36510,31219,93974,97857,86484,81128,45239,59766,68551,57184,48680,16519,51345,63133,61495,18162,56362,58108,9281,34343,96892,72135,28583,77597,9824,57279,99438,98349,10893,32767,22090,95875,29657,1498,15181,26179,59658,78955,75911,69334,96778,67103,74455,51596,75508,67657,80878,77877,15849,84411,69849,57640,42443,97161,15461,91195,43426,80676,10552,16592,1881,51290,78407,58598,61393,44206,80715,82534,89135,74559,1565,11389,17127,9234,87912,37025,33915,93864,57359,36148,63485,33403,24369,30516,92607,98958,99785,77165,85038,1569,27972,46996,71110,63722,30312,97288,13669,96146,2532,12544,75757,94002,44240,34633,9308,3131,32793,54163,13364,66823,57909,43528,18135,21482,66931,92388,21770,12747,62553,62678,69270,33409,47546,75879,28079,49858,1352,71186,52984,47034,99084,81611,1837,72493,29467,54682,4504,68948,32082,76034,76442,54914,4186,81683,5802,44576,90565,56871,78344,59621,44521,99744,72354,44258,71673,7478,51831,31842,78098,97855,72650,56416,63886,1511,94442,81805,64342,78641,76551,86927,78365,20806,62882,69712,36123,26030,96747,7554,83431,28213,69978,99305,86446,69187,39777,54321,66215,1027,38828,43357,32857,51546,2144,76878,36435,47334,3081,75252,30144,98666,39981,49186,75656,27179,48528,17693,78134,87749,10557,55697,72927,82290,5540,68734,10798,33682,66532,27440,49282,43361,3050,70283,6500,63071,23863,48151,32315,92068,46037,87846,46816,22534,67001,7225,74348,91347,30689,32343,98728,75980,68909,57364,22131,40338,18651,57234,84858,45283,38281,58961,78286,16690,80770,95062,9935,8838,73504,85137,17019,21272,74198,94402,9780,14463,96066,97190,49396,12207,9359,71730,19610,53491,65919,72010,26378,47472,13706,71896,65616,56072,52860,71732,51412,82898,84221,96622,808,94546,46997,40141,67360,68522,73504,87248,38336,37267,15633,56228,69421,14801,34311,45849,84954,48035,10273,39071,88743,98464,35668,71680,58662,97880,63081,75313,56014,21011,60177,4979,19429,3451,33589,17860,27393,13352,68580,31852,53904,82539,28754,26667,94650,6769,51640,95957,12211,56258,3507,44097,9406,70559,56706,3116,3152,42612,1417,11393,12242,6430,19259,69641,61192,19624,40502,13818,73188,22836,8884,2271,43435,32672,93625,10278,87827,75251,24599,42520,61507,23662,92496,93635,67477,47967,20272,39021,23756,62714,9707,78510,48748,73541,84201,76750,88121,74838,85138,47549,64273,45499,75450,49542,5601,74427,6600,69812,45485,20420,29110,19717,32382,38864,36112,81952,2097,2317,21199,33782,28836,94217,20203,96187,64980,86115,43305,35400,35279,86541,89593,36347,66843,36783,75591,75410,71517,46022,6684,84113,22528,19908,46795,56058,82226,72110,16773,56307,71415,72665,10764,49052,6287,10764,43683,32191,92037,94750,59067,50328,23074,37351,57311,91727,44558,55462,56551,63187,61657,56375,1669,59547,96727,73362,98444,21073,18955,2381,3112,6898,45653,77854,4076,97647,13701,57713,47614,44239,3041,49850,34875,67967,95139,96638,38192,18660,98685,23419,61966,31475,46661,65372,67278,45186,63657,42356,18314,939,78496,98135,78022,63692,33963,36884,85741,56508,87124,90339,66810,23147,38692,75980,82779,53721,75723,27099,31906,98498,19628,60173,92905,59654,86922,99375,72865,32753,98899,66143,4645,39666,883,46456,49847,74353,76997,76409,79340,84787,39025,19998,10062,3469,32233,8492,39578,96117,79735,40637,27861,28376,84312,60508,66078,91765,40246,96836,35057,93918,76651,28528,71925,87648,84750,82280,74292,16388,34496,91915,4207,29093,40244,10387,61539,60277,58505,56056,66482,22279,37444,8734,84974,37120,53140,8917,17420,5774,92913,29497,43273,34938,76152,95960,18875,56085,73214,90265,25996,34796,25725,50028,8472,67649,79121,27862,33673,10857,90017,80272,17680,2040,34147,40427,63246,93106,27192,74720,1006,67885,55328,54193,39106,40231,3252,91955,89954,45890,26081,14777,85394,31015,5916,37301,73369,32102,22547,11908,93282,91366,30549,22219,73775,71049,95431,47449,3020,39129,40227,99341,44902,74464,61167,1466,689,63447,55966,38704,63676,71870,30871,17180,66104,32937,46794,28393,90638,54695,74827,37645,25087,53106,77107,74045,49030,81109,53908,97051,34290,65881,48992,74182,7583,25892,39589,1879,1173,11136,62133,35414,72479,88371,27344,44587,38915,54191,31419,33176,64010,30811,60225,87377,91670,75703,31622,27956,67522,91265,84142,53189,46515,72441,24714,22767,52923,80189,63340,13269,34199,8874,4532,98807,82129,13803,66097,23218,45460,90868,63503,24700,53498,53788,6058,50040,46332,7498,82797,64471,34180,67579,27924,46314,34983,3819,7223,78358,40345,17941,57640,21613,57365,4527,97192,33535,76590,2167,18705,45389,32090,40145,16017,23345,22015,48153,85369,55179,69923,24104,18947,38159,27468,53550,43117,97645,36533,90186,91458,47289,55692,12565,87984,52513,66641,15338,81563,54345,72938,77596,55427,48629,47537,22440,31222,46233,6520,7056,23133,67804,40663,32326,6779,37058,56447,70396,33085,88314,88569,80107,25546,30624,27783,359,39870,15287,79188,64150,96538,7847,26734,36859,31502,23361,14238,45641,35636,5436,83693,50367,59179,24615,53562,1358,42239,17892,88075,34563,42083,81775,32146,48438,6274,68086,60850,60935,76730,31294,38704,66246,1742,24780,90943,31157,66145,47329,99305,11888,62188,10370,61426,88917,24050,1727,58539,35483,61507,91590,50575,51664,97311,28306,72849,51338,85944,47253,6200,91538,75731,30352,61549,86470,43548,16058,89871,33968,41637,11738,33089,63328,64375,67569,35449,70862,403,32275,32419,10621,54475,56102,34415,91531,37482,94946,28329,7432,70534,41169,25446,829,26148,11343,6832,22981,14729,62581,84329,48265,42953,45239,94328,63964,47836,45188,54693,11586,64872,16275,48680,95319,2367,88937,18685,22258,33472,60178,73218,28766,59842,37685,79068,69273,32823,37686,81342,13691,940,94406,60390,68563,7151,95932,35948,19767,71010,38245,40756,70837,44006,49565,39594,43603,6932,25607,91058,22704,17386,22307,45945,60404,38986,63986,6739,63782,40285,18139,43167,52899,40339,44736,36050,68233,15812,17430,2089,96591,51848,67587,30688,83616,16240,12650,93903,94315,49947,8528,9812,30974,32364,72489,33843,71372,43542,94076,37552,46207,1989,5354,74943,93997,65612,59315,10407,40543,38493,11863,7268,99635,47959,63351,28950,29509,16761,93099,87493,22732,67801,80300,17691,49590,14471,86347,23082,56117,95081,29567,4143,94291,94364,78076,58955,25088,14094,17247,48355,91484,22855,30291,18264,46051,32800,92529,1190,21759,108,653,99821,32832,94966,11025,69942,22095,67482,83879,2988,35661,71161,86225,74262,18420,54873,12979,34287,14573,56340,10047,19093,17970,82691,89936,39199,1270,2711,75683,64864,62686,44754,58793,16646,62345,75047,63775,67334,3223,29641,43103,20729,44685,82252,63580,6661,90388,80138,2212,56107,20686,66689,40858,56783,92758,20661,11986,32191,6706,22086,96973,58572,54128,97188,18756,12436,34399,42774,7506,25411,4956,77126,17738,56988,61272,5946,28469,72584,66693,87234,3781,45765,88223,56094,28704,16567,17286,86469,27205,49673,95007,85367,81816,59456,41016,16932,55002,41147,77648,7073,94842,24242,25396,43449,19313,25045,30799,33925,30824,44585,40836]
