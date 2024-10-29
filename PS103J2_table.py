
def closest(array, value):
    """Devuelve el índice del elemento más cercano en el array a un valor dado."""
    return min(range(len(array)), key=lambda i: abs(array[i] - value))

PS103J2_array = [
42326.42,
42214.99,
42103.88,
41993.11,
41882.65,
41772.53,
41662.73,
41553.25,
41444.09,
41335.25,
41226.74,
41118.54,
41010.66,
40903.10,
40795.85,
40688.92,
40582.30,
40476.00,
40370.00,
40264.32,
40158.95,
40053.88,
39949.12,
39844.67,
39740.53,
39636.69,
39533.15,
39429.92,
39326.99,
39224.36,
39122.03,
39020.00,
38918.27,
38816.83,
38715.69,
38614.85,
38514.29,
38414.04,
38314.07,
38214.40,
38115.02,
38015.92,
37917.12,
37818.60,
37720.37,
37622.42,
37524.76,
37427.39,
37330.29,
37233.48,
37136.95,
37040.70,
36944.73,
36849.04,
36753.63,
36658.49,
36563.63,
36469.04,
36374.73,
36280.69,
36186.93,
36093.43,
36000.21,
35907.25,
35814.57,
35722.15,
35630.00,
35538.12,
35446.50,
35355.14,
35264.06,
35173.23,
35082.66,
34992.36,
34902.32,
34812.54,
34723.01,
34633.75,
34544.74,
34455.99,
34366.50,
34278.30,
34190.36,
34102.68,
34015.24,
33928.06,
33841.13,
33754.45,
33668.02,
33581.83,
33495.90,
33410.21,
33324.77,
33239.57,
33154.62,
33069.91,
32985.44,
32901.22,
32817.24,
32733.50,
32650.00,
32566.74,
32483.72,
32400.93,
32318.38,
32236.07,
32154.00,
32072.16,
31990.55,
31909.18,
31828.03,
31747.12,
31666.45,
31586.00,
31505.78,
31425.79,
31346.03,
31266.50,
31187.19,
31108.11,
31029.25,
30950.62,
30872.22,
30794.03,
30716.07,
30638.33,
30560.81,
30483.52,
30406.44,
30329.58,
30252.94,
30176.52,
30100.31,
30024.32,
29948.55,
29872.99,
29797.64,
29722.51,
29647.59,
29572.89,
29498.39,
29424.11,
29350.04,
29276.18,
29202.52,
29129.08,
29055.84,
28982.81,
28909.98,
28837.36,
28764.95,
28692.74,
28620.73,
28548.93,
28477.33,
28405.93,
28334.74,
28263.74,
28192.94,
28122.35,
28051.95,
27981.75,
27911.75,
27841.94,
27772.34,
27702.92,
27633.70,
27564.68,
27495.85,
27427.22,
27358.77,
27290.52,
27222.46,
27154.59,
27086.91,
27019.43,
26952.13,
26885.02,
26818.09,
26751.36,
26684.81,
26618.45,
26552.27,
26486.28,
26420.47,
26354.85,
26289.41,
26224.15,
26159.08,
26094.18,
26029.47,
25964.94,
25900.59,
25836.42,
25772.42,
25708.61,
25644.97,
25581.51,
25518.23,
25455.13,
25392.19,
25329.44,
25266.86,
25204.45,
25142.22,
25080.16,
25018.27,
24956.55,
24895.01,
24833.63,
24772.43,
24711.39,
24650.53,
24589.83,
24529.31,
24468.95,
24408.75,
24348.73,
24288.87,
24229.17,
24169.64,
24110.28,
24051.08,
23992.04,
23933.17,
23874.46,
23815.91,
23757.52,
23699.30,
23641.23,
23583.33,
23525.58,
23468.00,
23410.57,
23353.30,
23296.19,
23239.23,
23182.44,
23125.80,
23069.31,
23012.98,
22956.81,
22900.79,
22844.92,
22789.21,
22733.65,
22678.24,
22622.99,
22567.88,
22512.93,
22458.13,
22403.48,
22348.98,
22294.63,
22240.42,
22186.37,
22132.46,
22078.70,
22025.09,
21971.63,
21918.31,
21865.13,
21812.11,
21759.22,
21706.48,
21653.89,
21601.44,
21549.13,
21496.97,
21444.94,
21393.06,
21341.32,
21289.73,
21238.27,
21186.95,
21135.77,
21084.73,
21033.83,
20983.07,
20932.45,
20881.97,
20831.62,
20781.41,
20731.33,
20681.39,
20631.59,
20581.92,
20532.39,
20482.99,
20433.72,
20384.59,
20335.59,
20286.73,
20238.00,
20189.39,
20140.93,
20092.59,
20044.38,
19996.30,
19948.36,
19900.54,
19852.85,
19805.29,
19757.86,
19710.56,
19663.38,
19616.33,
19569.41,
19522.62,
19475.95,
19429.41,
19382.99,
19336.70,
19290.53,
19244.49,
19198.57,
19152.78,
19107.10,
19061.56,
19016.13,
18970.82,
18925.64,
18880.58,
18835.64,
18790.82,
18746.12,
18701.54,
18657.08,
18612.74,
18568.52,
18524.41,
18480.43,
18436.56,
18392.81,
18349.18,
18305.66,
18262.26,
18218.98,
18175.81,
18132.76,
18089.82,
18047.00,
18004.29,
17961.70,
17919.22,
17876.85,
17834.60,
17792.46,
17750.43,
17708.51,
17666.71,
17625.01,
17583.43,
17541.96,
17500.60,
17459.35,
17418.20,
17377.17,
17336.25,
17295.43,
17254.73,
17214.13,
17173.64,
17133.26,
17092.98,
17052.82,
17012.75,
16972.80,
16932.95,
16893.20,
16853.57,
16814.03,
16774.60,
16735.28,
16696.06,
16656.94,
16617.93,
16579.02,
16540.21,
16501.51,
16462.90,
16424.40,
16386.01,
16347.71,
16309.51,
16271.42,
16233.42,
16195.53,
16157.73,
16120.04,
16082.44,
16044.94,
16007.55,
15970.25,
15933.04,
15895.94,
15858.94,
15822.03,
15785.21,
15748.50,
15711.88,
15675.36,
15638.93,
15602.60,
15566.37,
15530.23,
15494.18,
15458.23,
15422.37,
15386.61,
15350.94,
15315.37,
15279.88,
15244.49,
15209.20,
15173.99,
15138.88,
15103.86,
15068.93,
15034.09,
14999.34,
14964.69,
14930.12,
14895.65,
14861.26,
14826.97,
14792.76,
14758.64,
14724.61,
14690.67,
14656.82,
14623.06,
14589.38,
14555.80,
14522.30,
14488.88,
14455.56,
14422.32,
14389.17,
14356.10,
14323.12,
14290.22,
14257.41,
14224.69,
14192.05,
14159.49,
14127.02,
14094.64,
14062.33,
14030.12,
13997.98,
13965.93,
13933.96,
13902.07,
13870.27,
13838.55,
13806.91,
13775.35,
13743.87,
13712.48,
13681.17,
13649.93,
13618.78,
13587.71,
13556.72,
13525.81,
13494.97,
13464.22,
13433.55,
13402.95,
13372.44,
13342.00,
13311.64,
13281.36,
13251.16,
13221.04,
13190.99,
13161.02,
13131.13,
13101.31,
13071.57,
13041.91,
13012.32,
12982.81,
12953.37,
12924.01,
12894.73,
12865.52,
12836.38,
12807.33,
12778.34,
12749.43,
12720.59,
12691.83,
12663.14,
12634.52,
12605.98,
12577.51,
12549.11,
12520.79,
12492.53,
12464.35,
12436.24,
12408.21,
12380.24,
12352.35,
12324.52,
12296.77,
12269.09,
12241.48,
12213.94,
12186.47,
12159.07,
12131.74,
12104.48,
12077.29,
12050.17,
12023.11,
11996.13,
11969.21,
11942.36,
11915.58,
11888.87,
11862.23,
11835.65,
11809.14,
11782.70,
11756.33,
11730.02,
11703.78,
11677.60,
11651.50,
11625.45,
11599.48,
11573.57,
11547.72,
11521.94,
11496.23,
11470.58,
11445.00,
11419.48,
11394.02,
11368.63,
11343.30,
11318.04,
11292.84,
11267.70,
11242.63,
11217.62,
11192.67,
11167.79,
11142.97,
11118.21,
11093.52,
11068.88,
11044.31,
11019.80,
10995.35,
10970.96,
10946.64,
10922.37,
10898.17,
10874.03,
10849.94,
10825.92,
10801.96,
10778.06,
10754.22,
10730.44,
10706.71,
10683.05,
10659.45,
10635.90,
10612.42,
10588.99,
10565.62,
10542.31,
10519.06,
10495.87,
10472.73,
10449.66,
10426.64,
10403.67,
10380.77,
10357.92,
10335.13,
10312.40,
10289.72,
10267.10,
10244.53,
10222.02,
10199.57,
10177.18,
10154.84,
10132.55,
10110.32,
10088.15,
10066.03,
10043.96,
10021.95,
10000.00,
9978.10,
9956.25,
9934.46,
9912.73,
9891.04,
9869.41,
9847.84,
9826.31,
9804.85,
9783.43,
9762.07,
9740.76,
9719.50,
9698.29,
9677.14,
9656.04,
9634.99,
9614.00,
9593.06,
9572.16,
9551.32,
9530.53,
9509.80,
9489.11,
9468.48,
9447.89,
9427.36,
9406.87,
9386.44,
9366.06,
9345.73,
9325.45,
9305.21,
9285.03,
9264.90,
9244.82,
9224.78,
9204.80,
9184.86,
9164.98,
9145.14,
9125.35,
9105.61,
9085.92,
9066.28,
9046.68,
9027.13,
9007.64,
8988.18,
8968.78,
8949.42,
8930.12,
8910.85,
8891.64,
8872.47,
8853.35,
8834.28,
8815.25,
8796.27,
8777.34,
8758.45,
8739.61,
8720.81,
8702.06,
8683.36,
8664.70,
8646.09,
8627.52,
8609.00,
8590.52,
8572.09,
8553.70,
8535.36,
8517.06,
8498.81,
8480.60,
8462.44,
8444.32,
8426.24,
8408.21,
8390.22,
8372.28,
8354.38,
8336.52,
8318.70,
8300.93,
8283.21,
8265.52,
8247.88,
8230.28,
8212.72,
8195.21,
8177.74,
8160.31,
8142.92,
8125.58,
8108.27,
8091.01,
8073.79,
8056.61,
8039.48,
8022.38,
8005.33,
7988.32,
7971.35,
7954.42,
7937.53,
7920.68,
7903.87,
7887.10,
7870.37,
7853.69,
7837.04,
7820.43,
7803.87,
7787.34,
7770.85,
7754.41,
7738.00,
7721.63,
7705.30,
7689.01,
7672.76,
7656.55,
7640.38,
7624.24,
7608.15,
7592.09,
7576.07,
7560.09,
7544.15,
7528.25,
7512.39,
7496.56,
7480.77,
7465.02,
7449.31,
7433.63,
7417.99,
7402.39,
7386.83,
7371.30,
7355.81,
7340.36,
7324.94,
7309.56,
7294.22,
7278.92,
7263.65,
7248.42,
7233.22,
7218.06,
7202.94,
7187.85,
7172.80,
7157.78,
7142.80,
7127.86,
7112.95,
7098.07,
7083.24,
7068.43,
7053.67,
7038.93,
7024.24,
7009.57,
6994.95,
6980.35,
6965.79,
6951.27,
6936.78,
6922.33,
6907.90,
6893.52,
6879.17,
6864.85,
6850.56,
6836.31,
6822.09,
6807.91,
6793.76,
6779.64,
6765.56,
6751.51,
6737.49,
6723.51,
6709.56,
6695.64,
6681.76,
6667.91,
6654.09,
6640.30,
6626.55,
6612.82,
6599.14,
6585.48,
6571.85,
6558.26,
6544.70,
6531.17,
6517.67,
6504.21,
6490.77,
6477.37,
6464.00,
6450.66,
6437.35,
6424.08,
6410.83,
6397.62,
6384.43,
6371.28,
6358.16,
6345.07,
6332.01,
6318.98,
6305.98,
6293.01,
6280.07,
6267.17,
6254.29,
6241.44,
6228.62,
6215.83,
6203.08,
6190.35,
6177.65,
6164.98,
6152.34,
6139.73,
6127.15,
6114.60,
6102.08,
6089.59,
6077.13,
6064.69,
6052.29,
6039.91,
6027.56,
6015.25,
6002.96,
5990.70,
5978.46,
5966.26,
5954.08,
5941.93,
5929.82,
5917.72,
5905.66,
5893.63,
5881.62,
5869.64,
5857.69,
5845.76,
5833.87,
5822.00,
5810.16,
5798.35,
5786.56,
5774.80,
5763.07,
5751.36,
5739.69,
5728.04,
5716.41,
5704.82,
5693.25,
5681.70,
5670.19,
5658.70,
5647.23,
5635.80,
5624.39,
5613.00,
5601.65,
5590.31,
5579.01,
5567.73,
5556.48,
5545.25,
5534.05,
5522.87,
5511.72,
5500.60,
5489.50,
5478.42,
5467.38,
5456.35,
5445.36,
5434.38,
5423.44,
5412.52,
5401.62,
5390.75,
5379.90,
5369.08,
5358.28,
5347.51,
5336.76,
5326.04
]

PS103J2_temp_array = [
-5.00,
-4.95,
-4.90,
-4.85,
-4.80,
-4.75,
-4.70,
-4.65,
-4.60,
-4.55,
-4.50,
-4.45,
-4.40,
-4.35,
-4.30,
-4.25,
-4.20,
-4.15,
-4.10,
-4.05,
-4.00,
-3.95,
-3.90,
-3.85,
-3.80,
-3.75,
-3.70,
-3.65,
-3.60,
-3.55,
-3.50,
-3.45,
-3.40,
-3.35,
-3.30,
-3.25,
-3.20,
-3.15,
-3.10,
-3.05,
-3.00,
-2.95,
-2.90,
-2.85,
-2.80,
-2.75,
-2.70,
-2.65,
-2.60,
-2.55,
-2.50,
-2.45,
-2.40,
-2.35,
-2.30,
-2.25,
-2.20,
-2.15,
-2.10,
-2.05,
-2.00,
-1.95,
-1.90,
-1.85,
-1.80,
-1.75,
-1.70,
-1.65,
-1.60,
-1.55,
-1.50,
-1.45,
-1.40,
-1.35,
-1.30,
-1.25,
-1.20,
-1.15,
-1.10,
-1.05,
-1.00,
-0.95,
-0.90,
-0.85,
-0.80,
-0.75,
-0.70,
-0.65,
-0.60,
-0.55,
-0.50,
-0.45,
-0.40,
-0.35,
-0.30,
-0.25,
-0.20,
-0.15,
-0.10,
-0.05,
0.00,
0.05,
0.10,
0.15,
0.20,
0.25,
0.30,
0.35,
0.40,
0.45,
0.50,
0.55,
0.60,
0.65,
0.70,
0.75,
0.80,
0.85,
0.90,
0.95,
1.00,
1.05,
1.10,
1.15,
1.20,
1.25,
1.30,
1.35,
1.40,
1.45,
1.50,
1.55,
1.60,
1.65,
1.70,
1.75,
1.80,
1.85,
1.90,
1.95,
2.00,
2.05,
2.10,
2.15,
2.20,
2.25,
2.30,
2.35,
2.40,
2.45,
2.50,
2.55,
2.60,
2.65,
2.70,
2.75,
2.80,
2.85,
2.90,
2.95,
3.00,
3.05,
3.10,
3.15,
3.20,
3.25,
3.30,
3.35,
3.40,
3.45,
3.50,
3.55,
3.60,
3.65,
3.70,
3.75,
3.80,
3.85,
3.90,
3.95,
4.00,
4.05,
4.10,
4.15,
4.20,
4.25,
4.30,
4.35,
4.40,
4.45,
4.50,
4.55,
4.60,
4.65,
4.70,
4.75,
4.80,
4.85,
4.90,
4.95,
5.00,
5.05,
5.10,
5.15,
5.20,
5.25,
5.30,
5.35,
5.40,
5.45,
5.50,
5.55,
5.60,
5.65,
5.70,
5.75,
5.80,
5.85,
5.90,
5.95,
6.00,
6.05,
6.10,
6.15,
6.20,
6.25,
6.30,
6.35,
6.40,
6.45,
6.50,
6.55,
6.60,
6.65,
6.70,
6.75,
6.80,
6.85,
6.90,
6.95,
7.00,
7.05,
7.10,
7.15,
7.20,
7.25,
7.30,
7.35,
7.40,
7.45,
7.50,
7.55,
7.60,
7.65,
7.70,
7.75,
7.80,
7.85,
7.90,
7.95,
8.00,
8.05,
8.10,
8.15,
8.20,
8.25,
8.30,
8.35,
8.40,
8.45,
8.50,
8.55,
8.60,
8.65,
8.70,
8.75,
8.80,
8.85,
8.90,
8.95,
9.00,
9.05,
9.10,
9.15,
9.20,
9.25,
9.30,
9.35,
9.40,
9.45,
9.50,
9.55,
9.60,
9.65,
9.70,
9.75,
9.80,
9.85,
9.90,
9.95,
10.00,
10.05,
10.10,
10.15,
10.20,
10.25,
10.30,
10.35,
10.40,
10.45,
10.50,
10.55,
10.60,
10.65,
10.70,
10.75,
10.80,
10.85,
10.90,
10.95,
11.00,
11.05,
11.10,
11.15,
11.20,
11.25,
11.30,
11.35,
11.40,
11.45,
11.50,
11.55,
11.60,
11.65,
11.70,
11.75,
11.80,
11.85,
11.90,
11.95,
12.00,
12.05,
12.10,
12.15,
12.20,
12.25,
12.30,
12.35,
12.40,
12.45,
12.50,
12.55,
12.60,
12.65,
12.70,
12.75,
12.80,
12.85,
12.90,
12.95,
13.00,
13.05,
13.10,
13.15,
13.20,
13.25,
13.30,
13.35,
13.40,
13.45,
13.50,
13.55,
13.60,
13.65,
13.70,
13.75,
13.80,
13.85,
13.90,
13.95,
14.00,
14.05,
14.10,
14.15,
14.20,
14.25,
14.30,
14.35,
14.40,
14.45,
14.50,
14.55,
14.60,
14.65,
14.70,
14.75,
14.80,
14.85,
14.90,
14.95,
15.00,
15.05,
15.10,
15.15,
15.20,
15.25,
15.30,
15.35,
15.40,
15.45,
15.50,
15.55,
15.60,
15.65,
15.70,
15.75,
15.80,
15.85,
15.90,
15.95,
16.00,
16.05,
16.10,
16.15,
16.20,
16.25,
16.30,
16.35,
16.40,
16.45,
16.50,
16.55,
16.60,
16.65,
16.70,
16.75,
16.80,
16.85,
16.90,
16.95,
17.00,
17.05,
17.10,
17.15,
17.20,
17.25,
17.30,
17.35,
17.40,
17.45,
17.50,
17.55,
17.60,
17.65,
17.70,
17.75,
17.80,
17.85,
17.90,
17.95,
18.00,
18.05,
18.10,
18.15,
18.20,
18.25,
18.30,
18.35,
18.40,
18.45,
18.50,
18.55,
18.60,
18.65,
18.70,
18.75,
18.80,
18.85,
18.90,
18.95,
19.00,
19.05,
19.10,
19.15,
19.20,
19.25,
19.30,
19.35,
19.40,
19.45,
19.50,
19.55,
19.60,
19.65,
19.70,
19.75,
19.80,
19.85,
19.90,
19.95,
20.00,
20.05,
20.10,
20.15,
20.20,
20.25,
20.30,
20.35,
20.40,
20.45,
20.50,
20.55,
20.60,
20.65,
20.70,
20.75,
20.80,
20.85,
20.90,
20.95,
21.00,
21.05,
21.10,
21.15,
21.20,
21.25,
21.30,
21.35,
21.40,
21.45,
21.50,
21.55,
21.60,
21.65,
21.70,
21.75,
21.80,
21.85,
21.90,
21.95,
22.00,
22.05,
22.10,
22.15,
22.20,
22.25,
22.30,
22.35,
22.40,
22.45,
22.50,
22.55,
22.60,
22.65,
22.70,
22.75,
22.80,
22.85,
22.90,
22.95,
23.00,
23.05,
23.10,
23.15,
23.20,
23.25,
23.30,
23.35,
23.40,
23.45,
23.50,
23.55,
23.60,
23.65,
23.70,
23.75,
23.80,
23.85,
23.90,
23.95,
24.00,
24.05,
24.10,
24.15,
24.20,
24.25,
24.30,
24.35,
24.40,
24.45,
24.50,
24.55,
24.60,
24.65,
24.70,
24.75,
24.80,
24.85,
24.90,
24.95,
25.00,
25.05,
25.10,
25.15,
25.20,
25.25,
25.30,
25.35,
25.40,
25.45,
25.50,
25.55,
25.60,
25.65,
25.70,
25.75,
25.80,
25.85,
25.90,
25.95,
26.00,
26.05,
26.10,
26.15,
26.20,
26.25,
26.30,
26.35,
26.40,
26.45,
26.50,
26.55,
26.60,
26.65,
26.70,
26.75,
26.80,
26.85,
26.90,
26.95,
27.00,
27.05,
27.10,
27.15,
27.20,
27.25,
27.30,
27.35,
27.40,
27.45,
27.50,
27.55,
27.60,
27.65,
27.70,
27.75,
27.80,
27.85,
27.90,
27.95,
28.00,
28.05,
28.10,
28.15,
28.20,
28.25,
28.30,
28.35,
28.40,
28.45,
28.50,
28.55,
28.60,
28.65,
28.70,
28.75,
28.80,
28.85,
28.90,
28.95,
29.00,
29.05,
29.10,
29.15,
29.20,
29.25,
29.30,
29.35,
29.40,
29.45,
29.50,
29.55,
29.60,
29.65,
29.70,
29.75,
29.80,
29.85,
29.90,
29.95,
30.00,
30.05,
30.10,
30.15,
30.20,
30.25,
30.30,
30.35,
30.40,
30.45,
30.50,
30.55,
30.60,
30.65,
30.70,
30.75,
30.80,
30.85,
30.90,
30.95,
31.00,
31.05,
31.10,
31.15,
31.20,
31.25,
31.30,
31.35,
31.40,
31.45,
31.50,
31.55,
31.60,
31.65,
31.70,
31.75,
31.80,
31.85,
31.90,
31.95,
32.00,
32.05,
32.10,
32.15,
32.20,
32.25,
32.30,
32.35,
32.40,
32.45,
32.50,
32.55,
32.60,
32.65,
32.70,
32.75,
32.80,
32.85,
32.90,
32.95,
33.00,
33.05,
33.10,
33.15,
33.20,
33.25,
33.30,
33.35,
33.40,
33.45,
33.50,
33.55,
33.60,
33.65,
33.70,
33.75,
33.80,
33.85,
33.90,
33.95,
34.00,
34.05,
34.10,
34.15,
34.20,
34.25,
34.30,
34.35,
34.40,
34.45,
34.50,
34.55,
34.60,
34.65,
34.70,
34.75,
34.80,
34.85,
34.90,
34.95,
35.00,
35.05,
35.10,
35.15,
35.20,
35.25,
35.30,
35.35,
35.40,
35.45,
35.50,
35.55,
35.60,
35.65,
35.70,
35.75,
35.80,
35.85,
35.90,
35.95,
36.00,
36.05,
36.10,
36.15,
36.20,
36.25,
36.30,
36.35,
36.40,
36.45,
36.50,
36.55,
36.60,
36.65,
36.70,
36.75,
36.80,
36.85,
36.90,
36.95,
37.00,
37.05,
37.10,
37.15,
37.20,
37.25,
37.30,
37.35,
37.40,
37.45,
37.50,
37.55,
37.60,
37.65,
37.70,
37.75,
37.80,
37.85,
37.90,
37.95,
38.00,
38.05,
38.10,
38.15,
38.20,
38.25,
38.30,
38.35,
38.40,
38.45,
38.50,
38.55,
38.60,
38.65,
38.70,
38.75,
38.80,
38.85,
38.90,
38.95,
39.00,
39.05,
39.10,
39.15,
39.20,
39.25,
39.30,
39.35,
39.40,
39.45,
39.50,
39.55,
39.60,
39.65,
39.70,
39.75,
39.80,
39.85,
39.90,
39.95,
40.00
]
#print(array)

#value = 42326.42

#print('The value:', value)
#print('Final temperature is:', PS103J2_temp_array[closest(PS103J2_array, value)])