from main_frame import checkWinner

testBoard1 = [["X","-","-"],
            ["-","X","-"],
            ["-","-","X"]]
testBoard2 = [["-","-","X"],
            ["-","X","-"],
            ["X","-","-"]]
testBoard3 = [["X","-","-"],
            ["X","-","-"],
            ["X","-","-"]]
testBoard4 = [["O","X","-"],
            ["X","X","-"],
            ["X","X","-"]]
testBoard5 = [["X","X","X"],
            ["-","-","-"],
            ["-","-","-"]]
testBoard6 = [["-","-","-"],
            ["X","X","X"],
            ["-","-","-"]]
test = [""] * 6
test[0] = checkWinner(testBoard1)
test[1] = checkWinner(testBoard2)
test[2] = checkWinner(testBoard3)
test[3] = checkWinner(testBoard4)
test[4] = checkWinner(testBoard5)
test[5] = checkWinner(testBoard6)
for i in range(len(test)):
    if test[i] != "X":
        print("testboard #" + str(i + 1) + "failed.")
print("----- Tests Complete -----")