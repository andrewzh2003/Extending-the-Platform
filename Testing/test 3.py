string1 = "@weather today is so great and @weather"
final = string1.split("@weather")
x = "sunny"
finalString = ''
print(len(final))
i = 0
while i < len(final):
    if i < len(final) - 1:
        finalString += final[i]
        finalString += x
        i += 1
    else:
        finalString += final[i]
        i += 1

print(finalString)