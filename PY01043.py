a = [22, 44, 66, 88, 2002, 2222, 2442, 2662, 2882, 4004, 4224, 4444, 4664, 4884, 6006, 6226, 6446, 6666, 6886, 8008, 8228, 8448, 8668, 8888, 200002, 202202, 204402, 206602, 208802, 220022, 222222, 224422, 226622, 228822, 240042, 242242, 244442, 246642, 248842, 260062, 262262, 264462, 266662, 268862, 
280082, 282282, 284482, 286682, 288882, 400004, 402204, 404404, 406604, 408804, 420024, 422224, 424424, 426624, 428824, 440044, 442244, 444444, 446644, 448844, 460064, 462264, 464464, 466664, 468864, 480084, 482284, 484484, 486684, 488884, 600006, 602206, 604406, 606606, 608806, 620026, 622226, 
624426, 626626, 628826, 640046, 642246, 644446, 646646, 648846, 660066, 662266, 664466, 666666, 668866, 680086, 682286, 684486, 686686, 688886, 800008, 802208, 804408, 806608, 808808, 820028, 822228, 824428, 826628, 828828, 840048, 842248, 844448, 846648, 848848, 860068, 862268, 864468, 866668, 
868868, 880088, 882288, 884488, 886688, 888888]
for i in range(int(input())):
    n = int(input())
    for i in a:
        if i<n: print(i, end=" ")
        else: break
    print()