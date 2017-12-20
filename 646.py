# 求可以构成一个合法串的最长长度. 本来题目提示使用
#  DP 的, 而且 DP 在本地测试也没有问题, 可能是时
#  间要求比较高, 或者是 python 有点坑, 死活过不
#  去一个 300 长度的测试. 只能换用贪心, 算是过了

class Solution:
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Solution 1 DP TLE
        # pairs = sorted(pairs, key=lambda x:x[1])
        # dp = [1] * len(pairs)

        # for i in range(0, len(pairs)):
        #     for j in range(0, i):
        #         if pairs[j][1] < pairs[i][0] and dp[j] >= dp[i]:
        #             dp[i] = dp[j]+1
        # return max(dp)

        # Solution 2 Greedy AC
        pairs = sorted(pairs, key=lambda x:x[1])
        cur = float('-inf')
        result = 0
        for p in pairs:
            if cur < p[0]:
                cur = p[1]
                result += 1
        return result

print(Solution().findLongestChain([[-61,13],[-952,-722],[-902,-120],[999,1000],[-493,842],[-39,798],[-892,856],[53,269],[-316,-85],[548,818],[-672,-533],[-762,886],[196,707],[184,441],[397,802],[39,58],[1,508],[-878,-46],[-241,-1],[-566,76],[-991,-457],[310,449],[72,869],[86,907],[875,945],[-817,-669],[-545,-414],[264,629],[-420,-243],[720,851],[154,644],[384,986],[-679,529],[-233,961],[693,838],[653,907],[676,814],[999,1000],[-474,-270],[35,410],[-690,-66],[664,981],[168,974],[53,246],[-779,183],[-431,788],[-157,910],[-527,794],[647,738],[393,726],[592,633],[349,975],[701,963],[-213,710],[945,959],[-478,-455],[-929,838],[274,490],[957,958],[-360,-197],[360,484],[662,861],[-843,651],[-285,789],[898,949],[-681,444],[677,947],[597,885],[156,840],[-819,-606],[778,945],[-563,230],[290,694],[-149,-87],[144,160],[33,383],[-775,900],[298,832],[-614,429],[-609,841],[211,931],[24,933],[-606,125],[-659,38],[-266,774],[107,303],[106,212],[-435,596],[-731,244],[-309,49],[329,683],[526,873],[140,866],[678,867],[-931,954],[992,998],[807,975],[369,866],[-431,39],[-169,387],[-777,-3],[341,522],[199,423],[489,506],[-408,-388],[-485,71],[381,512],[-298,855],[-916,864],[-155,656],[-146,266],[-80,599],[285,728],[-198,332],[-966,843],[-125,155],[-382,203],[837,855],[887,968],[-107,559],[799,852],[-150,712],[-164,4],[521,555],[154,205],[956,982],[9,388],[145,407],[633,837],[-73,739],[-938,975],[-516,450],[756,970],[-67,241],[216,370],[221,315],[-715,618],[336,776],[-512,929],[-633,536],[-796,489],[-380,-282],[945,951],[888,906],[-301,307],[-443,973],[-909,-85],[411,847],[96,747],[-954,340],[253,628],[-944,620],[-986,-720],[965,998],[506,526],[-130,339],[990,992],[8,449],[-521,433],[624,966],[274,828],[200,470],[-818,-691],[650,980],[735,779],[-78,637],[-523,16],[-389,330],[497,870],[614,823],[-783,632],[-767,350],[-56,81],[313,432],[-656,116],[-118,51],[319,839],[-16,610],[-328,811],[-583,150],[918,933],[988,998],[-314,664],[-198,111],[-152,582],[188,796],[417,641],[-325,773],[317,769],[579,587],[-344,-56],[-55,491],[-381,-299],[-565,-456],[-738,682],[131,838],[-771,-706],[-370,359],[-448,487],[-889,-110],[-287,-52],[-421,551],[612,819],[913,957],[-417,807],[-651,55],[134,243],[-972,-858],[-602,819],[485,726],[-939,-160],[-227,704],[-196,446],[985,986],[261,850],[226,935],[-910,-40],[-761,-736],[-968,309],[-818,817],[-775,-330],[662,731],[-517,-497],[431,773],[786,877],[-743,478],[-425,-237],[7,765],[480,814],[445,612],[86,178],[-605,-279],[-585,-278],[96,514],[13,709],[-603,726],[-582,-72],[628,838],[-744,-675],[-789,-676],[114,613],[413,838],[-360,350],[-585,100],[-707,-312],[520,991],[-835,-530],[-897,859],[312,808],[544,674],[295,686],[-553,-298],[467,840],[-674,729],[818,994],[-604,117],[719,726],[-550,-535],[382,904],[-668,263],[608,641],[728,926],[-618,-510],[-279,289],[621,692],[228,630],[640,708],[-956,-7],[-690,334],[-742,217],[987,1000],[-848,898],[-944,-812],[-96,114],[-487,933],[57,356],[-438,-357],[-750,-238],[808,995],[225,433],[249,459],[-14,585],[-36,737],[-260,272],[208,255],[283,641],[424,592],[-120,721],[831,910],[623,638],[-409,5],[-983,-211],[-50,594],[-629,-454],[-967,533],[851,937],[606,979],[-610,-328],[650,742]]))