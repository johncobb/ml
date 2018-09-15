import sys
transliterationString = "0123456789.ABCDEFGH..JKLMN.P.R..STUVWXYZ"
valWeights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

def calculateCheckDigit(vin):
     return sum([x[0] * x[1] for x in zip([transliterationString.find(c) % 10 for c in vin], valWeights)]) % 11


def ValidateVIN(vin, many=False):
    if many:
        results = []
        for v in vin:
            results.append(ValidateVIN(v))
        return results

    else:
        if len(vin) != 17:
            return (False, vin, "Invalid Length")

        for c in vin:
            if c not in transliterationString:
                return (False, vin, "Invalid Character")

        if vin[8] not in "0123456789X":
            return (False, vin, "Invalid Checksum Character")

        if vin[8] == "X":
            cd = 10
        else:
            cd = int(vin[8])

        if  calculateCheckDigit(vin) == cd:
            return (True, vin, "Valid VIN")
        else:
            return (False, vin, "Invalid Checksum calculation")

if __name__ == "__main__":
    print(ValidateVIN(sys.argv[1]))