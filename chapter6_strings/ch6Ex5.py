strVal = "X-DSPAM-Confidence: 0.8475 "

fltVal = float(strVal[strVal.find(":") + 1:])
print(fltVal, type(fltVal))