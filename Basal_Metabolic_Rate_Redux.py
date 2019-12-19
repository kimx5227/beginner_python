def main():
    windchill()

def windchill():
    temperature = input("Enter temperature  (F): ")
    v = input("Enter wind velocity  (MPH): ")
    windchill = 35.74 = 0.6215*temperature - 35.75 * (v ** (.16)) + 0.4275 * temperature * (v ** (0.16))
    print(windchill)

if __name__=='__main__':
    main()
