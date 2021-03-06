## GIS Validation v0.1
## Author: Gurjot Sidhu
## License: MIT
## Acknowledgement: James Halliday (https://github.com/substack/point-in-polygon)
## Description: This script checks whether a geospatial coordinate (long, lat) falls within the boundaries defined by a (multi-shape) polygon. It uses the PNPOLY - Point Inclusion in Polygon Test by W. Randolph Franklin (WRF). It contains wrapper functions to support purposes of geospatial shapes.

def PointInMultiShapePolygon(point, vs):
    # check how many levels the shape has
    levels = 0
    temp = vs
    while type(temp[0]) == list:
        temp = temp[0]
        levels += 1

    if (levels == 1):
        print('Level 1')
        # Flat shape
        return PointInPolygon(point, vs)

    if (levels == 2):
        print('Level 2')
        if len(vs[0]) > 0 and len(vs[0][0]) == 2:
            # Regular case
            return PointInPolygon(point, vs)
    
    if (levels == 3):
        print('Level 3')
        if len(vs) > 1 and len(vs[0][0]) > 1 and len(vs[0][0][0]) == 2:
            # Gosaba case
            # Check for all constituent polygons
            for i in range(len(vs)):
                # Break when point is found inside any shape
                if PointInPolygon(point, vs[i][0]):
                    return True

def PointInPolygon(point, vs):
    if (len(vs) > 0) and (type(vs[0]) == list):
        print('Nested')
        return PointInPolygonNested(point,vs)
    else:
        print('Flat')
        return PointInPolygonFlat(point,vs)

def PointInPolygonFlat(point, vs):
    x = point[0]
    y = point[1]
    inside = False
    start = 0
    end = len(vs)
    length = int((end-start)/2)
    j = length-1
    for i in range(length):
        xi = vs[start+i*2+0]
        yi = vs[start+i*2+1]
        xj = vs[start+j*2+0]
        yj = vs[start+j*2+1]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside

def PointInPolygonNested(point, vs):
    x = point[0]
    y = point[1]
    inside = False
    start = 0
    end = len(vs)
    length = end-start
    j = length-1
    for i in range(length):
        xi = vs[i+start][0]
        yi = vs[i+start][1]
        xj = vs[j+start][0]
        yj = vs[j+start][1]
        if ((yi > y) != (yj > y)) and (x < (xj - xi) * (y - yi) / (yj - yi) + xi):
            inside = not inside
        j = i
    return inside

def test():
    polygon = [[87.4877313853952,21.732207516563676],[87.47345462003489,21.745342141126912],[87.45137000002552,21.732409999821698],[87.47083400008916,21.70718000005712],[87.46826100014516,21.677271000356427],[87.45865000029733,21.64493900043459],[87.4677659998012,21.645649999947523],[87.48208600006888,21.6258689996547],[87.48175800023165,21.609462000271208],[87.5602809997684,21.63300499958109],[87.62799800010777,21.646161000130178],[87.64073669364353,21.6576099219605],[87.63302839124731,21.670561332139812],[87.61032833368569,21.676700341847322],[87.58491568970737,21.671275170812635],[87.57834837787539,21.681268906834646],[87.56537460425466,21.689441208145297],[87.56164456084787,21.692547551928044],[87.56175785114397,21.689847930137944],[87.55550555203973,21.679983997763372],[87.53137781713264,21.69640227914192],[87.51357174873726,21.710781081581672],[87.51588565220112,21.71536720763055],[87.49958110178648,21.72592573948134],[87.48939293143872,21.730373178379523],[87.4877313853952,21.732207516563676]]

    point = [87.5085,21.6865]

    if (PointInPolygon(point,polygon)):
        return "Test successful."
    else:
        return "Test failed."

def testMulti():
    polygon = [[[[88.83472300026631,21.60722200039504],[88.82833000042922,21.576942999819664],[88.85388900007734,21.550002000292125],[88.89250200006728,21.57944600013286],[88.83472300026631,21.60722200039504]]],[[[88.72885100037342,21.637080999588534],[88.70802400040736,21.590070999976717],[88.75709599978063,21.59957500028611],[88.72885100037342,21.637080999588534]]],[[[88.77194200002333,21.653062000011346],[88.73558099956352,21.644635999951504],[88.74888699983524,21.57944099990226],[88.79805700013048,21.59194500006174],[88.77194200002333,21.653062000011346]]],[[[88.98449000001352,21.70568899964769],[88.95244499983693,21.70149100030949],[88.9649960003652,21.6440390002997],[88.99289800014265,21.64335999956438],[89.00026599997597,21.60209100029948],[89.02876200016624,21.604822000335105],[89.02205000000754,21.654599999890138],[88.99430200013728,21.64898199981951],[88.98449000001352,21.70568899964769]]],[[[88.80665600007438,21.706672000012816],[88.7491690002492,21.673334999610574],[88.79666899997443,21.655560000094],[88.80665600007438,21.706672000012816]]],[[[89.05920500021062,21.72180299990856],[89.0184850001827,21.708207999799413],[89.02605400029194,21.64392699963139],[89.04943800036347,21.620226000229763],[89.09285799989686,21.6369299998197],[89.09189599960075,21.666670999866824],[89.05920500021062,21.72180299990856]]],[[[88.88305699978076,21.745279999772208],[88.87305399984228,21.694443999990654],[88.88582599977013,21.661108999680664],[88.92194399981582,21.63291199978903],[88.94194799960059,21.68972199987047],[88.88305699978076,21.745279999772208]]],[[[88.92710100021105,21.761949999592844],[88.92250000027485,21.721112000418543],[88.97222099989926,21.698609999651808],[88.96527000041027,21.7499639999387],[88.92710100021105,21.761949999592844]]],[[[88.83167199986298,21.76610899983052],[88.78193600044614,21.732501000420882],[88.8191679997035,21.703332999818144],[88.80899900020376,21.63993199976204],[88.85994000033082,21.643066000395663],[88.83167199986298,21.76610899983052]]],[[[88.99967100041641,21.78546999964084],[88.96676700019697,21.772185000337572],[88.97667000002053,21.728610999997727],[89.00483800037347,21.71613200009176],[88.99967100041641,21.78546999964084]]],[[[88.71620099977639,21.807380000086994],[88.6949989996042,21.74389000042322],[88.71111199981897,21.69018000030684],[88.7602549997685,21.685001999842484],[88.75911800039546,21.758598999744095],[88.71620099977639,21.807380000086994]]],[[[88.9158330003927,21.825834000338887],[88.88555900004786,21.810290000283317],[88.90555699955593,21.75166600018582],[88.93723199975705,21.81750100007116],[88.9158330003927,21.825834000338887]]],[[[88.85611100002268,21.865281000118102],[88.83915599964973,21.848609000205272],[88.83499900040363,21.781666999632364],[88.89111399991123,21.762500999821327],[88.87722000040276,21.85167000017043],[88.85611100002268,21.865281000118102]]],[[[88.78917000039525,21.878609999651815],[88.76583199974704,21.830554000366874],[88.82110499999584,21.824999999650288],[88.82888900012733,21.863333000217835],[88.78917000039525,21.878609999651815]]],[[[88.9790560003342,21.893489999663814],[88.95124000002602,21.84174200009329],[88.9763420001832,21.804285000352536],[89.02024000017593,21.817832000046792],[89.030958999858,21.862780999943254],[88.9790560003342,21.893489999663814]]],[[[88.71805699993064,21.907221999795524],[88.69610600029176,21.842220999699407],[88.72583099960099,21.794445999883067],[88.77722099974937,21.821669999870664],[88.77500099989629,21.86499899970414],[88.71805699993064,21.907221999795524]]],[[[88.83655600025924,21.91789299996202],[88.88999899975408,21.812221000298962],[88.97667000002053,21.86750099997124],[88.97164899960171,21.899169999895605],[88.91456600042062,21.9281190002917],[88.88659600020532,21.914457999836884],[88.83655600025924,21.91789299996202]]],[[[88.7236109997479,21.931944000415342],[88.72915600004944,21.89972100012409],[88.79666899997443,21.87667000012044],[88.79944700037885,21.919720999724404],[88.7236109997479,21.931944000415342]]],[[[88.81276600035068,22.019442000148217],[88.76149700038633,22.014520999844308],[88.7516630001474,21.958890000173426],[88.82483600028127,21.93984999987765],[88.85658300020538,21.919059999819183],[88.9072730004487,21.929537000032553],[88.89972000017792,22.013059999919108],[88.81276600035068,22.019442000148217]]],[[[89.01619699989169,22.05092100030396],[88.98610599989206,22.04909999996505],[88.97432699989122,21.994551999874943],[89.01806599974617,21.97553399969439],[88.99945899963319,21.949819000046887],[89.03032800043695,21.926444000390347],[89.06328600044861,21.934512000128734],[89.0780189999769,21.98641699974479],[89.0403520004445,22.049162000126273],[89.01619699989169,22.05092100030396]]],[[[88.80346699960239,22.08527299984911],[88.77899799985789,22.10300199994242],[88.74794100027702,22.059302000087257],[88.78076899968966,22.048619000266683],[88.80346699960239,22.08527299984911]]],[[[88.81790099973142,22.123028999888504],[88.8055120003786,22.085080999988236],[88.86585199957017,22.081455000048265],[88.84718300019534,22.117250999633995],[88.81790099973142,22.123028999888504]]],[[[88.86514300014937,22.1669910001346],[88.84645900008286,22.121301000241033],[88.8722539998223,22.087804999701007],[88.922745999928,22.10895300008093],[88.88608600006893,22.164830000304335],[88.86514300014937,22.1669910001346]]],[[[88.94996599973115,22.189191999611126],[88.90943799956409,22.13364500021663],[88.93071799973598,22.09809999961533],[88.90170299989359,22.063865000069768],[88.93147300037873,21.942077000053587],[88.99233200012179,21.906945999658205],[88.9938889999774,21.970281000268017],[88.97249700003658,21.987792000200727],[88.97709599988053,22.03839299993706],[88.95807699965388,22.06024100022205],[88.98497800003474,22.1481200004377],[88.94996599973115,22.189191999611126]]],[[[89.00193000026934,22.19917200028766],[88.97268599975916,22.19343800026354],[88.99661299969023,22.140120000237857],[88.98036899972959,22.0792829997107],[89.0388719996431,22.055459000032897],[89.03111199971909,22.093889999723785],[89.04910999962686,22.132920000057993],[89.02242400016752,22.14836399999865],[89.00193000026934,22.19917200028766]]],[[[88.84474900036611,22.189191999611126],[88.80649599989056,22.17801100020756],[88.70253800012864,22.077952000384585],[88.74958899983255,22.081055999634714],[88.79843000024437,22.12495200043452],[88.849844999747,22.142732000181695],[88.84474900036611,22.189191999611126]]],[[[88.87937800009468,22.271681000377896],[88.91586299997755,22.23035300019086],[88.9308779999198,22.266969999865637],[88.87937800009468,22.271681000377896]]],[[[88.82000000029984,22.269720999924232],[88.85958200000937,22.205431000240537],[88.90249599959077,22.176645000166673],[88.91398699980027,22.215773999670375],[88.8874970003863,22.264450999713915],[88.85529300007198,22.28090000013492],[88.82000000029984,22.269720999924232]]],[[[88.81259999989015,22.283390999894777],[88.75218900012231,22.230390000098453],[88.74724599970318,22.198629999574848],[88.81519299985712,22.181169000149282],[88.80100999961184,22.228002999738692],[88.82541800014064,22.240911999689104],[88.81259999989015,22.283390999894777]]]]

    point = [88.9137, 21.6727]

    if (PointInMultiShapePolygon(point,polygon)):
        return "Test successful."
    else:
        return "Test failed."