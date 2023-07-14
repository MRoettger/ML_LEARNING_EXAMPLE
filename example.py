a = 5 * 4
a = a + 2
text = "Model prediction was: " + str(a)
f = open("result.txt", "w")
f.write(text)
f.close()
